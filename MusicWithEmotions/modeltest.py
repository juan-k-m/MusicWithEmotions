#from numpy.lib.type_check import nan_to_num
import pandas as pd
from tensorflow.keras import Sequential, layers
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping
#from tensorflow.keras.layers.experimental.preprocessing import Rescaling
#from tensorflow.keras.optimizers.schedules import ExponentialDecay
#from MusicWithEmotions.data import get_train_test_data
import joblib
import mlflow
#from memoized_property import memoized_property
from google.cloud import storage
import numpy as np
from tensorflow.keras.utils import to_categorical


BUCKET_NAME = 'musicwithemotions'


def get_data_from_gcp(local = False):
    '''method to get the training data (or a portion of it) from google cloud bucket'''
    # Add Client() here
    client = storage.Client('lewagon-bootcamp-310515')
    if local:
        path = '../raw_data/icml_face_data.csv'
    else:
        path = 'gs://musicwithemotions/Data/icml_face_data.csv'

    df = pd.read_csv(path)
    return df


def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.reset_index(drop = True, inplace = True)
    df.columns=['emotion', 'usage', 'pixels']
    for i in range(len(df.pixels)):
        test_str = df.pixels[i]
        test_list = test_str.split(' ')
        df.pixels[i] = np.asarray(test_list).reshape(48,48).astype(int)

    return df

def get_train_test_data(df):
    df_train = df[df['usage']=='Training']
    df_train.reset_index(drop = True, inplace = True)
    print(f'TRAIN{len(df_train)}')
    df_test = df[df['usage']=='PublicTest']
    print(f'first test{len(df_test)}')
    df_test = df_test.append(df[df['usage']=='PrivateTest'])
    df_test.reset_index(drop = True, inplace = True)
    print(len(df_test))
    df_train.drop(columns = 'usage', inplace = True)
    df_test.drop(columns = 'usage', inplace = True)
    print(len(df_test))
    X_train = df_train.pixels
    y_train = df_train.emotion
    print(f'TRAIN{len(df_train)}')
    X_test = df_test.pixels
    y_test = df_test.emotion
    print(len(X_test))
    X_train = [X_train[i] for i in range(len(X_train))]
    X_train = np.dstack(X_train)
    X_train = np.rollaxis(X_train, -1)
    print(f'XXXTRAIN{len(X_train)}')
    X_test = [X_test[i] for i in range(len(X_test))]
    print(len(X_test))
    X_test = np.dstack(X_test)
    X_test = np.rollaxis(X_test, -1)

    y_train = to_categorical(y_train, num_classes=7)
    y_test = to_categorical(y_test, num_classes=7)

    X_train = np.expand_dims(X_train, axis = -1)
    X_train = np.expand_dims(X_train, axis = -1)
    
    X_train = X_train / 255.
    X_test = X_test / 255.

    

    return (X_train, X_test, y_train, y_test)



def create_model():
    model = Sequential()
    #model.add(Rescaling(1./255, input_shape=(48,48,1)))

    #reg_l1 = regularizers.L1(0.01)
    #reg_l2 = regularizers.L2(0.01)
    #reg_l1_l2 = regularizers.l1_l2(l1=0.005, l2=0.0005)

    model.add(layers.Conv2D(32, kernel_size=(3,3), padding='same',activation='relu', input_shape=(48,48,1)))
    model.add(layers.Conv2D(32, kernel_size=(3,3), padding='same',activation='relu'))
    model.add(layers.MaxPooling2D(3))


    model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same',activation="relu"))
    model.add(layers.MaxPooling2D(3))
    model.add(layers.Dropout(0.2))

    model.add(layers.Conv2D(128, kernel_size=(3,3), padding='same',activation="relu"))
    model.add(layers.MaxPooling2D(2))
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dropout(0.5))

    model.add(layers.Dense(7, activation='softmax'))
    
    return model


def compile_model(model):
    opt = optimizers.Adam(learning_rate=1e-4)
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    return model


def fit_model(model, X_train, y_train):
    es = EarlyStopping(monitor='val_accuracy', mode='max', patience=60, verbose=1, restore_best_weights=True)

    history = model.fit(X_train[:1000], y_train[:1000],
         batch_size=32, 
         epochs=1000, 
         validation_split=0.3,
         callbacks=[es])

    return history, model

def evaluate_model(model, X_test, y_test):
    results = model.evaluate(X_test[:300], y_test[:300])

    return results

def upload_model_to_gcp():

    STORAGE_LOCATION = 'models/musicwithemotions/model.joblib'
    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(STORAGE_LOCATION)

    blob.upload_from_filename('model.joblib')
    
def save_model(reg):

    STORAGE_LOCATION = 'models/musicwithemotions/model.joblib'

    joblib.dump(reg, 'model.joblib')
    print("saved model.joblib locally")

    upload_model_to_gcp()
    print(f"uploaded model.joblib to gcp cloud storage under \n => {STORAGE_LOCATION}")

if __name__ == "__main__":
    # Get and clean data
    df = get_data_from_gcp()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = get_train_test_data(df)
    # Train and save model, locally and
    #trainer = Trainer(X=X_train, y=y_train)
    #trainer.set_experiment_name('xp2')
    #trainer.run()
    #rmse = trainer.evaluate(X_test, y_test)
    #print(f"rmse: {rmse}")
    #trainer.save_model(trainer)
    model = create_model()
    model = compile_model(model)
    history, model = fit_model(model, X_train, y_train)
    results = evaluate_model(model, X_test, y_test)
    print(results)
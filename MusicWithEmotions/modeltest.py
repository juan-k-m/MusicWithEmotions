#from numpy.lib.type_check import nan_to_num
import pandas as pd
from tensorflow.keras import Sequential, layers
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping
#from tensorflow.keras.layers.experimental.preprocessing import Rescaling
#from tensorflow.keras.optimizers.schedules import ExponentialDecay
#from MusicWithEmotions.data import get_train_test_data
#import joblib
#import mlflow
#from memoized_property import memoized_property
from google.cloud import storage
import numpy as np
from tensorflow.keras.utils import to_categorical
#from mlflow.tracking import MlflowClient
from sklearn.externals import joblib


BUCKET_NAME = 'musicwithemotions'
#MODEL_NAME = nan
#MODEL_VERSION = nan
#MLFLOW_URI = "https://mlflow.lewagon.co/"
#EXPERIMENT_NAME = "[DE] [Berlin] [AlexBabkf] muswemot + v1"

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
    df_test = df[df['usage']=='PublicTest']
    df_test = df_test.append(df[df['usage']=='PrivateTest'])
    df_test.reset_index(drop = True, inplace = True)
    df_train.drop(columns = 'usage', inplace = True)
    df_test.drop(columns = 'usage', inplace = True)
    X_train = df_train.pixels
    y_train = df_train.emotion
    X_test = df_test.pixels
    y_test = df_test.emotion
    X_train = [X_train[i] for i in range(len(X_train))]
    X_train = np.dstack(X_train)
    X_train = np.rollaxis(X_train, -1)
    X_test = [X_test[i] for i in range(len(X_test))]
    X_test = np.dstack(X_test)
    X_test = np.rollaxis(X_test, -1)

    y_train = to_categorical(y_train, num_classes=7)
    y_test = to_categorical(y_test, num_classes=7)

    X_train = np.expand_dims(X_train, axis = -1)
    X_test = np.expand_dims(X_test, axis = -1)

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
    model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same',activation='relu'))
    model.add(layers.MaxPooling2D(3))


    model.add(layers.Conv2D(128, kernel_size=(3,3), padding='same',activation="relu"))
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
    es = EarlyStopping(patience=1, verbose=1, restore_best_weights=True)

    history = model.fit(X_train[:100], y_train[:100],
         batch_size=16, 
         epochs=1, 
         validation_split=0.3,
         callbacks=[es])

    return history, model

def evaluate_model(model, X_test, y_test):
    results = model.evaluate(X_test[:30], y_test[:30])

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

def save_model_to_gcp(reg):
    """Save the model into a .joblib and upload it on Google Storage /models folder
    HINTS : use sklearn.joblib (or jbolib) libraries and google-cloud-storage"""
    
    local_model_name = 'model.joblib'
    joblib.dump(reg, local_model_name)
    print("saved model.joblib locally")
    client = storage.Client().bucket(BUCKET_NAME)
    storage_location = f"models/{modelwithemotions}/{v0}/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(local_model_name)
    print("uploaded model.joblib to gcp cloud storage under \n => {}".format(storage_location))

def storage_upload():
    client = storage.Client().bucket(BUCKET_NAME)
    MODEL_NAME = 'musicwithemotions'
    MODEL_VERSION = 'ifworks'
    storage_location = 'models/{}/versions/{}/{}'.format(
        MODEL_NAME,
        MODEL_VERSION,
        'model.joblib')
    blob = client.blob(storage_location)
    blob.upload_from_filename('model.joblib')
    print("=> model.joblib uploaded to bucket {} inside {}".format(BUCKET_NAME, storage_location))

# @memoized_property
# def mlflow_client():
#     mlflow.set_tracking_uri(MLFLOW_URI)

#     return MlflowClient()

# @memoized_property
# def mlflow_experiment_id():
#     try:
#         return mlflow_client.create_experiment(EXPERIMENT_NAME)
#     except BaseException:
#         return mlflow_client.get_experiment_by_name(
#     EXPERIMENT_NAME).experiment_id

# @memoized_property
# def mlflow_run():
#     return mlflow_client.create_run(mlflow_experiment_id)

# def mlflow_log_param(key, value):
#     mlflow_client.log_param(mlflow_run.info.run_id, key, value)

# def mlflow_log_metric(key, value):
#     mlflow_client.log_metric(mlflow_run.info.run_id, key, value)

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
    storage_upload()
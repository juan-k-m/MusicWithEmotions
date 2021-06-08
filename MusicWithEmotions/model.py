import numpy as np
import pandas as pd

from tensorflow.keras import Sequential, layers, regularizers
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from keras.layers.normalization import BatchNormalization

from MusicWithEmotions.data import get_data_from_gcp, clean_data, get_train_test_data


from google.cloud import storage
import keras

from termcolor import colored
from sklearn.externals import joblib
import mlflow
from memoized_property import memoized_property
from mlflow.tracking import MlflowClient
import multiprocessing
import time
from psutil import virtual_memory
from MusicWithEmotions.utils import simple_time_tracker


BUCKET_NAME = 'musicwithemotions'
#MODEL_NAME = ''
#MODEL_VERSION = ''
MLFLOW_URI = "https://mlflow.lewagon.co/"
EXPERIMENT_NAME = "[DE] [Berlin] [AlexBabkf] muswemot + v1"

def create_model():
    model = Sequential()

    reg_l2 = regularizers.L2(0.01)

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

    model.add(layers.Dense(6, activation='softmax'))

    model= Sequential()
    model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(48, 48,1)))
    model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same', activation='relu' ))
    model.add(BatchNormalization())
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, kernel_size=(5,5), padding='same', activation='relu', kernel_regularizer=reg_l2))
    model.add(BatchNormalization())
    model.add(layers.MaxPool2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Conv2D(512, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=reg_l2))
    model.add(BatchNormalization())
    model.add(layers.MaxPool2D(pool_size=(3)))
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(512, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=reg_l2))
    model.add(BatchNormalization())
    model.add(layers.MaxPool2D(pool_size=(3)))
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten()) 
    model.add(layers.Dense(256, activation = 'relu'))
    model.add(BatchNormalization())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Dense(1408,activation = 'relu'))
    model.add(BatchNormalization())
    model.add(layers.Dropout(0.5))

    model.add(layers.Dense(6, activation='softmax'))
    
    return model


def compile_model(model):


    model.compile(optimizer='Adam', loss='categorical_crossentropy',metrics='accuracy')

    return model


def fit_model(model, X_train, y_train):
    lrd = ReduceLROnPlateau(monitor = 'val_loss',patience = 3,verbose = 1,factor = 0.20, min_lr = 1e-10)

    mcp = ModelCheckpoint(filepath = 'model.h5',
        save_weights_only=True,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)

    es = EarlyStopping(patience=20, restore_best_weights = True)

    #model.load_weights('model.h5')   uncomment to use pretrained weights

    history = model.fit(X_train, y_train,
            batch_size=64, 
            epochs=200, 
            validation_split=0.3,
            callbacks=[lrd, mcp, es])

    return history, model

def evaluate_model(model, X_test, y_test):
    results = model.evaluate(X_test[:10], y_test[:10])

    return results


def predict(model, X_test):
    prediction = model.predict(X_test)

    return prediction

#Upload, Train and Save in GCP

def model_to_gcp():
    local_model_name = 'model.joblib'
    model.save('test_model')
    model2 = keras.models.load_model('test_model')
    print("saved model locally")
    client = storage.Client('lewagon-bootcamp-310515').bucket(BUCKET_NAME)
    storage_location = f"models/modelwithemotions/v0/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(local_model_name)
    print("uploaded model.joblib to gcp cloud storage under \n => {}".format(storage_location))


#MLflow

@simple_time_tracker
def train():
    tic = time.time()
    create_model()
    compile_model(model)
    fit_model(model, X_train, y_train)
    # mlflow logs
    mlflow_log_metric("train_time", int(time.time() - tic))

def evaluate():
    results = model.evaluate(X_test, y_test)
    print(colored("accuracy: {}".format(results[1]), "blue"))

def save_model():
    """Save the model into a .joblib format"""
    joblib.dump(model, 'model.joblib')
    print(colored("model.joblib saved locally", "green"))


@memoized_property
def mlflow_client():
    mlflow.set_tracking_uri(MLFLOW_URI)
    return MlflowClient()

@memoized_property
def mlflow_experiment_id():
    try:
        return mlflow_client.create_experiment(EXPERIMENT_NAME)
    except BaseException:
        return mlflow_client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

@memoized_property
def mlflow_run():
    return mlflow_client.create_run(mlflow_experiment_id)

def mlflow_log_param(key, value):
    mlflow_client.log_param(mlflow_run.info.run_id, key, value)

def mlflow_log_metric(key, value):
    mlflow_client.log_metric(mlflow_run.info.run_id, key, value)

# def log_estimator_params():
#     reg = get_estimator()
#     mlflow_log_param('estimator_name', reg.__class__.__name__)
#     params = reg.get_params()
#     for k, v in params.items():
#         mlflow_log_param(k, v)

# def log_kwargs_params():
#     if mlflow:
#         for k, v in kwargs.items():
#             mlflow_log_param(k, v)

def log_machine_specs():
    cpus = multiprocessing.cpu_count()
    mem = virtual_memory()
    ram = int(mem.total / 1000000000)
    mlflow_log_param("ram", ram)
    mlflow_log_param("cpus", cpus)


if __name__ == "__main__":
    # Get and clean data

    df = get_data_from_gcp()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = get_train_test_data(df)

    #Model Creation

    model = create_model()
    model = compile_model(model)
    history, model = fit_model(model, X_train, y_train)

    #GCP

    model_to_gcp()

    #MLflow

    print(colored("############  Training model   ############", "red"))
    train()
    print(colored("############  Evaluating model ############", "blue"))
    evaluate()
    print(colored("############   Saving model    ############", "green"))
    save_model()

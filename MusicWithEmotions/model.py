import numpy as np
from numpy.lib.type_check import nan_to_num
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential, layers
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
#from tensorflow.keras.optimizers.schedules import ExponentialDecay
from MusicWithEmotions.data import get_train_test_data
import joblib
import mlflow
#from memoized_property import memoized_property
from google.cloud import storage


MLFLOW_URI = nan
EXPERIMENT_NAME = nan
BUCKET_NAME = nan
BUCKET_TRAIN_DATA_PATH = nan
MODEL_NAME = nan
MODEL_VERSION = nan

def create_model(X_train, y_train):
    model = Sequential()
    model.add(Rescaling(1./255, input_shape=(48,48,1)))

    #reg_l1 = regularizers.L1(0.01)
    #reg_l2 = regularizers.L2(0.01)
    #reg_l1_l2 = regularizers.l1_l2(l1=0.005, l2=0.0005)

    model.add(layers.Conv2D(32, kernel_size=(3,3), padding='same',activation='relu'))
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
    es = EarlyStopping(monitor='val_accuracy', mode='max', patience=50, verbose=1, restore_best_weights=True)

    model.fit(X_train, y_train,
         batch_size=32, 
         epochs=1000, 
         validation_split=0.3,
         callbacks=[es])

    return model

def evaluate_model(model, X_test, y_test):
    model.evaluate(X_test, y_test)

    return model

def upload_model_to_gcp():

    STORAGE_LOCATION = ''
    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(STORAGE_LOCATION)

    blob.upload_from_filename('')
    
def save_model(self, reg):

    STORAGE_LOCATION = ''

    joblib.dump(reg, 'model.joblib')
    print("saved model.joblib locally")

    upload_model_to_gcp()
    print(f"uploaded model.joblib to gcp cloud storage under \n => {STORAGE_LOCATION}")

@memoized_property
def mlflow_client():
    mlflow.set_tracking_uri(MLFLOW_URI)

    return MlflowClient()

@memoized_property
def mlflow_experiment_id():
    try:
        return mlflow_client.create_experiment(experiment_name)
    except BaseException:
        return mlflow_client.get_experiment_by_name(
    experiment_name).experiment_id

@memoized_property
def mlflow_run():
    return mlflow_client.create_run(mlflow_experiment_id)

def mlflow_log_param(key, value):
    mlflow_client.log_param(mlflow_run.info.run_id, key, value)

def mlflow_log_metric(key, value):
    mlflow_client.log_metric(mlflow_run.info.run_id, key, value)



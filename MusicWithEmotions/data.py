import pandas as pd
import numpy as np
from tensorflow.keras.utils import to_categorical
from google.cloud import storage

def get_data():
    
    bucket_name = 'wagon-data-606-totino'  #  to be set to personal bucket
    source_blob_name = 'MusicWithEmotions/export.csv'  #  to be set to personal path to file_to_load
    destination_file_name = '/tmp/tmp_download.csv'
       
    if len(bucket_name) > 0 and len(source_blob_name) > 0 :
        storage_client = storage.Client('wagon-bootcamp-310515')  #  to be set to personal project ID
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        
        df = pd.read_csv(destination_file_name)
    else:
        df = pd.read_csv('../raw_data/icml_face_data.csv')
        
    return df


def clean_data(df):
    df = df.drop_duplicates(inplace=True, ignore_index=True)
    df = df.columns=['emotion', 'usage', 'pixels']
    for i in range(len(df.pixels)):
        test_str = df.pixels[i]
        test_list = test_str.split(' ')
        df.pixels[i] = np.asarray(test_list).reshape(48,48).astype(int)

    return df

def get_train_test_data(df):
    df_train = df[df['usage']=='Training']
    df_test = df[df['usage']=='PublicTest']
    df_test = df_test.append(df[df['usage']=='PrivateTest'], ignore_index = True)
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

    return (X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    df = get_data()

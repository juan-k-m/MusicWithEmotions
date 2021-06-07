import pandas as pd
import numpy as np
#from tensorflow.keras.utils import to_categorical
from google.cloud import storage
import os



def get_data_from_gcp(local = False):

    client = storage.Client('lewagon-bootcamp-310515')
    if local:
        fd = os.open("/home/alexbabkf/code/AlexBabkf/MusicWithEmotions/", os.O_RDONLY )
        os.fchdir(fd)
        pwd = os.getcwd()
        path = os.path.join(pwd,"raw_data", 'icml_face_data.csv')
    else:
        path = 'gs://musicwithemotions/Data/icml_face_data.csv'

    df = pd.read_csv(path)
    return df


def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.reset_index(drop = True, inplace = True)
    df.columns=['emotion', 'usage', 'pixels']
    # we remove an motion that had little data
    df = df[df.emotion != 1]
    df.reset_index(drop = True, inplace = True)
    # turning string to an array
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
    # stacking X_train and X_test to become 3-d
    X_train = [X_train[i] for i in range(len(X_train))]
    X_train = np.dstack(X_train)
    X_train = np.rollaxis(X_train, -1)
    X_test = [X_test[i] for i in range(len(X_test))]
    X_test = np.dstack(X_test)
    X_test = np.rollaxis(X_test, -1)

    y_train = y_train - 1
    y_test = y_test - 1
    #y_train = to_categorical(y_train, num_classes=6)
    #y_test = to_categorical(y_test, num_classes=6)

    X_train = np.expand_dims(X_train, axis = -1)
    X_test = np.expand_dims(X_test, axis = -1)

    X_train = X_train / 255.
    X_test = X_test / 255.

    

    return (X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    df = get_data_from_gcp(local = True)
    #df = clean_data(df)
    #X_train, X_test, y_train, y_test = get_train_test_data(df)
    print(df.head())
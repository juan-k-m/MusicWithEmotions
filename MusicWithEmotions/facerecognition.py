import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

'''Class for make all the processing of the image'''
class Facerecognition:
    def __init__(self):
        pass

    def get_root_dir(self):
        cwd = os.getcwd()
        return os.path.join(cwd)

    def image_to_emotion(self, image):
        img = self.user_pic_preproc(image)
        path = os.path.join(self.get_root_dir(),"raw_data","model_65")
        model = self.load_trained_model(path)
        emotion = self.predict_emotion(model, img)
        return emotion


    def user_pic_preproc(self,img, bor=0):
        '''convert user picture to grayscale, identify and extract the face and compress to 48 x 48 pixels'''
        path = os.path.join(self.get_root_dir(),"MusicWithEmotions","haarcascade_frontalface_default.xml")
        face_model = cv2.CascadeClassifier(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_model.detectMultiScale(gray, 1.2, 15)
    
        # set additional border to face detection for picture extraction 
        x, y, w, h = faces[0]
        x2 = int(round((x - bor * w), 0))  # x 
        y2 = int(round((y - bor * h), 0))  # y
        w2 = int(round((w * (1 + 2 * bor)), 0))  # width of extraction
        h2 = int(round((h * (1 + 2 * bor)), 0))  # height of extraction
    
        img_face = gray[y2 : y2 + h2, x2 : x2 + w2]
        img_resized = cv2.resize(img_face, (48, 48), interpolation = cv2.INTER_AREA)
        img_expanded = np.expand_dims(img_resized, axis = [0, -1])
    
        return img_expanded

    def load_trained_model(self, path):
         return keras.models.load_model(path)

    def predict_emotion(self,model, img):
        emotions_2 = {0:'angry', 1:'scared', 2:'happy', 3:'sad', 4:'surprised', 5:'neutral'}
        results = model.predict(img)
        if len(results) > 0:
            ind = np.argmax(results[0])
            predicted_emotion = emotions_2.get(ind)
        else: 
            predicted_emotion = 'happy'  # hard coded in case no face recognition for the sake of testing
        return predicted_emotion

    def test_model_load(self):
        pass


if __name__ == '__main__':
    #cwd = os.getcwd()
    #os.path.join(cwd)


    img = cv2.imread('../raw_data/simopic.jpg')  #  example of picture load
    test = Facerecognition()
    img_preproc = test.user_pic_preproc(img) 
    print(img_preproc.shape)
    model = test.load_trained_model('../raw_data/model_65') # to be checked cause no tensorflow on my machine
    emotion = test.predict_emotion(model, img_preproc)
    print(emotion)
import cv2
import numpy as np
import keras
# img = cv2.imread('../rawdata/simogeopic.jpg')  #  example of picture load

def user_pic_preproc(img, bor=0):
    '''convert user picture to grayscale, identify and extract the face and compress to 48 x 48 pixels'''
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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

def load_trained_model(path):
    return keras.models.load_model(path)

def predict_emotion(model, img):
    emotions_2 = {0:'Angry', 1:'Fear', 2:'Happy', 3:'Sad', 4:'Surprise', 5:'Neutral'}
    results = model.predict(img)
    if results:
        ind = np.argmax(results)
        predicted_emotion = emotions_2.get(ind)
    else: 
        predicted_emotion = 'Happy'  # hard coded in case no face recognition for the sake of testing
    return predicted_emotion

if __name__ == '__main__':
    img = cv2.imread('../raw_data/simopic.jpg')  #  example of picture load
    img_preproc = user_pic_preproc(img) 
    print(img_preproc.shape)
    model = load_trained_model('../rawdata/model_65') # to be checked cause no tensorflow on my machine
    print(model)
    # res = predict_emotion(model, img_preproc)
    # print(res)
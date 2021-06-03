import cv2
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
    
    return img_resized  

if __name__ == '__main__':
    img = cv2.imread('../raw_data/simopic.jpg')  #  example of picture load
    img_resized = user_pic_preproc(img) 
    print(img_resized.shape)
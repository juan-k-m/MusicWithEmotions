from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.encoderemotion import Encoderemotion
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.services.pictureprocess import Pictureprocess


'''This class is going to control the entire application process'''
class Runprograma:
   
    def __init__(self, picture):
        self.fer = Facerecognition()
        self.encoder = Encoderemotion()
        self.musicgeneration = Musicgeneration()
        self.picturehelper = Pictureprocess()
        self.emotion = None
        self.picture = picture
        self.initialnotes = None
        self.cleanedpicture = None


   #RUN
    def run(self):
        self.process_picture()
        self.predict_emotion() 
        self.get_initial_notes() 
        return self.make_music()
        


   #TODO clean the picture
    def process_picture(self):
        self.cleanedpicture = self.picturehelper.cleanpicture(self.picture) 

   #TODO pass the picture to the model for predict the emotion
    def predict_emotion(self):
        self.emotion = self.fer.predict_emotion(self.cleanedpicture)

   #TODO pass the predicted emotion to the encoder to retieve the first 
   #musical notes
    def get_initial_notes(self):
        self.initialnotes = self.encoder.encode_emotion(self.emotion)

   #TODO pass the first notes to de model to retrieve the composition
    def make_music(self):
        return self.musicgeneration.callmagenta(self.initialnotes,self.emotion)

if __name__ == '__main__':
    picture = ''
    test = Runprograma(picture)
    test.run()
    print('done!')

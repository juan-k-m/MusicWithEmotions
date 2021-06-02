from MusicWithEmotions.fer import Fer
from MusicWithEmotions.encoder import Encoder
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.services.pictureprocess import Pictureprocess


'''This class is going to control the entire application process'''
class Runprogram:
   
    def __init__(self, picture):
        self.fer = Fer()
        self.encoder = Encoder()
        self.musicgeneration = Musicgeneration()
        self.picturehelper = Pictureprocess()
        self.emotion = None
        self.picture = picture
        self.initialnotes = None
        self.cleanedpicture = None


   #RUN
    def run(self):
        self.process_picture()
        print(self.cleanedpicture) 
        print(self.fer.test())
        #self.predict_emotion() 
        #self.get_initial_notes() 
        #return self.make_music() 
        return 'runing...'


   #TODO clean the picture
    def process_picture(self):
        self.cleanedpicture = self.picturehelper.cleanpicture(self.picture) 

   #TODO pass the picture to the model for predict the emotion
    def predict_emotion(self):
        self.emotion = self.fer.predict_emotion(self.cleanedpicture)

   #TODO pass the predicted emotion to the encoder to retieve the first 
   #musical notes
    def get_initial_notes(self):
        self.initialnotes = self.encoder(self.emotion)

   #TODO pass the first notes to de model to retrieve the composition
    def make_music(self):
        return self.musicgeneration.callmagenta(self.initialnotes)

if __name__ == '__main__':
    picture = ''
    test = Runprogram(picture)
    print(test.run())

from MusicWithEmotions.services.music import Music
from MusicWithEmotions.services.magentamodel import Magentamodel

'''Class to process the input from the encoder part and
generate the music composition '''
class Musicgeneration:
    def __init__(self):
        self.music_helper = Music()
        self.magentamodel = Magentamodel()

    def get_notes_from_emotion(self, emotion):
        return self.music_helper.list_of_notes(emotion)
    '''generates the composition with the base notes
    and also pass the emotion'''
    def callmagenta(self, initialnotes, emotion):
        #define attr in the magentamodel: -> emotion,
        self.magentamodel.initialnotes = initialnotes 
        self.magentamodel.emotion = emotion 
        return self.magentamodel.get_generated_midi_file()
    
if __name__ == '__main__':
	test = Musicgeneration()
	print (test.get_notes_from_emotion('happy'))
from MusicWithEmotions.services.music import Music
from MusicWithEmotions.services.magentamodel import Magentamodel

'''Class to process the input from the encoder part and
generate the music composition '''
class Musicgeneration:
    def __init__(self):
        self.music_helper = Music()
        self.magentamodel = Magentamodel()

    def get_notes_from_emotion(self, emotion):
        return self.music_helper.get_modes_to_chords()

    def callmagenta(self, initialnotes):
        return self.magentamodel.get_generated_midi_file()
    
if __name__ == '__main__':
	test = Musicgeneration()
	print (test.get_notes_from_emotion('happy'))
from MusicWithEmotions.services import Music

'''Class to process the input from the encoder part and
generate the music composition '''
class Musicgeneration:
    def __init__(self):
        self.music_helper = Music()
    def get_notes_from_emotion(self, emotion):
        notes = self.music_helper.get_modes_to_chords()
    
if __name__ == '__main__':
	test = Musicgeneration()
	print (test.get_notes_from_emotion('happy'))
from MusicWithEmotions.services.music import Music

'''This class is going to tranlate the concept of the emotion into
notes '''
class Encoderemotion:
    def __init__(self):
        self.music_helper = Music()
    def encode_emotion(self, emotion):
        return f'emotion being encoding {emotion}'

    
if __name__ == '__main__':
	test = Encoderemotion()
	print (test.encode_emotion('happy'))

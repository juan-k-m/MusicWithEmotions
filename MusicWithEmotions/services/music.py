

'''Class containing all the process for the processing of the 
music; transform the concept of the emotion into musical parts'''
class Music:
    '''Match the musical modes with diffent modes and 
    storages the notes in them
    emotion_to_modes: this variable matchs every emotion with differnet
    modes and their musical notes

    modes_to_notes: this variable contains the modes and their musical
    notes

    modes_to_chords: this variable prepare some chords to set the base 
    of the progression of the musical composition

    '''
    def __init__(self):
        self.emotion_to_modes  = {
                     "happy": {"ionian": ["C", "D", "E", "F", "G", "A", "B"],
                               "dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
                               "lydian": ["C", "D", "E", "F#", "G", "A", "B"],
                               "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"]},
                     
                     "sad": {"aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"]},

                     "scared": {"locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]}, 

                     "angry": {"phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
                              "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"]}, 

                     "neutral": {"dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"]}, 

                     "surprised": {"ionian": ["C", "D", "E", "F", "G", "A", "B"],
                                   "lydian": ["C", "D", "E", "F#", "G", "A", "B"]}, 

                     "disgusted": {"locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]}
                     } 

        self.modes_to_notes =  {
                  "ionian": ["C", "D", "E", "F", "G", "A", "B"],
                  "aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],  
                  "dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
                  "phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
                  "lydian": ["C", "D", "E", "F#", "G", "A", "B"],
                  "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"],
                  "locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"] 
                 }

        self.modes_to_chords = {
                  "ionian": {"a": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]},

                  "aeolian": {"a": ["Cm", "Fm", "Gm", "Cm"],
                              "b": ["Cm", "Bb", "Ab", "Gm", "Cm"],        
                              "c": ["Cm", "Bb", "Ab", "Bb", "Eb", "Gm", "Cm"],
                              "d": ["Cm", "Ab", "Eb", "Fm", "Cm"]},


                  "dorian": {"a": ["Cm", "F", "Cm", "Bb", "Cm", "Gm", "Cm"],
                             "b": ["Cm", "Bb", "F", "Gm", "Cm"],
                             "c": ["Cm", "Gm", "Cm", "F", "Bb", "Eb", "Bb", "Cm"]},

                  "phrygian": {"a": ["Cm", "Db", "Cm", "Ab", "Cm", "Eb", "Fm", "Cm"]},

                  "lydian": {"a": ["C", "D", "G", "C", "Am", "D", "G", "C"],
                             "b": ["C", "D", "Em", "Bm", "C", "D", "C"]},

                  "mixolydian": {"a": ["C", "F", "Gm", "C"],
                                 "b": ["C", "F", "Dm", "Gm", "Am", "Gm", "C"],
                                 "c": ["C", "Bb", "C", "F", "Gm", "Bb", "C"],
                                 "d": ["C", "Bb", "C", "F", "Gm", "Bb", "C"]},

                  "locrian": {"a": ["Bdim", "C", "Dm", "Em", "F", "G", "Am"]} 
                  
                  }
    def get_modes_to_chords(self):
        return self.modes_to_chords

    def get_modes_to_notes(self):
        return self.modes_to_notes

    def get_modes(self):
        return self.emotion_to_modes

    def get_notes_from_emotion(self, emotion):
        if emotion in self.emotion_to_modes:
            return self.emotion_to_modes[emotion]

if __name__ == '__main__':
	test = Music()
	print (test.get_notes_from_emotion('happy'))
import random

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

        #chods progressions
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

    def get_first_mode(self, mode_dict):
        '''returns first key of the dictionary'''
        return list(mode_dict.keys())[0]
    
    def list_of_notes(self,emotion):
        if emotion in self.emotion_to_modes:
            notes = self.emotion_to_modes[emotion]
            notes = self.get_first_mode(notes)
            notes = self.modes_to_notes[notes]

            list_notes =  [self.match_notes_to_midi_numbers()[number_notes] for number_notes in notes]
            return self.get_middle_val_list(list_notes)

    def get_middle_val_list(self,list_notes):
        return [self.findMiddle(notes) for notes in list_notes]

    def findMiddle(self, input_list):
        middle = float(len(input_list))/2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return (input_list[int(middle)], input_list[int(middle-1)])    

    def match_notes_to_midi_numbers(self):
        return  {
                 'C' : [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120], 
                 'C#' : [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121], 
                 'Db' : [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121], 
                 'D' : [2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122], 
                 'D#' : [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123], 
                 'Eb' : [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123], 
                 'E' : [4, 16, 28, 40, 52, 64, 76, 88, 100, 112, 124], 
                 'F' : [5, 17, 29, 41, 53, 65, 77, 89, 101, 113, 125], 
                 'F#' : [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                 'Gb' : [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                 'G' : [7, 19, 31, 43, 55, 67, 79, 91, 103, 115, 127],
                 'G#' : [8, 20, 32, 44, 56, 68, 80, 92, 104, 116], 
                 'Ab' : [8, 20, 32, 44, 56, 68, 80, 92, 104, 116], 
                 'A' : [9, 21, 33, 45, 57, 69, 81, 93, 105, 117],
                 'A#' : [10, 22, 34, 46, 58, 70, 82, 94, 106, 118],
                 'Bb' : [10, 22, 34, 46, 58, 70, 82, 94, 106, 118],
                 'B' : [11, 23, 35, 47, 59, 71, 83, 95, 107, 119]
                 } 




if __name__ == '__main__':
	test = Music()
	print (test.list_of_notes('angry'))
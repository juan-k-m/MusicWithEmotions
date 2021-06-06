from note_seq.protobuf import music_pb2
from MusicWithEmotions.services.music import Music
import random
'''Class responsible to create the starting sequences 
for the emotions base on the modes'''
class Sequencemaker:

    def __init__(self):
        self.emotions = {0:'angry', 1:'scared', 2:'happy', 3:'sad', 4:'surprised', 5:'neutral'}
        self.music_helper = Music()
    
    def create(self,emotion):
        
        if emotion == 'angry':
            return self.angry()
        elif emotion == 'scared':
            return self.scared()
        elif emotion == 'happy':
            return self.happy()
        elif emotion == 'sad':
            return self.sad()
        elif emotion == 'surprised':
            return self.surprised()
        elif emotion == 'neutral':
            return self.neutral()
        else:
        	return self.happy()



    def angry(self):
        scale = ["C", "Db", "Eb", "F", "G", "Ab", "Bb"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(2,4) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=0.40, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=0.40, end_time=0.8, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=0.8, end_time=0.85, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=0.85, end_time=1, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=1, end_time=2, velocity=90)


        sequence.total_time = 2
        sequence.tempos.add(qpm=60);
        return sequence

    def happy(self):
        scale = ["C", "D", "E", "F", "G", "A", "B"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(3,7) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=0.20, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=0.20, end_time=0.3, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=0.3, end_time=0.4, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=0.4, end_time=0.5, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=0.5, end_time=1, velocity=90)


        sequence.total_time = 1
        sequence.tempos.add(qpm=60);
        return sequence

    def scared(self):
        scale = ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(2,4) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=0.20, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=0.20, end_time=0.3, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=0.3, end_time=0.35, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=0.35, end_time=0.4, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=0.4, end_time=0.6, velocity=90)


        sequence.total_time = .6
        sequence.tempos.add(qpm=60);
        return sequence


    def surprised(self):
        scale = ["C", "D", "E", "F#", "G", "A", "B"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(2,9) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=.1, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=.1, end_time=.2, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=.2, end_time=.5, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=.5, end_time=1, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=1, end_time=2, velocity=90)


        sequence.total_time = 2
        sequence.tempos.add(qpm=60);
        return sequence

    def sad(self):
        scale = ["C", "D", "Eb", "F", "G", "Ab", "Bb"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(2,8) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=1, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=1, end_time=2, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=2, end_time=2.5, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=2.5, end_time=3.5, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=3.5, end_time=5, velocity=90)


        sequence.total_time = 5
        sequence.tempos.add(qpm=60);
        return sequence

    def neutral(self):
        scale = ["C", "D", "Eb", "F", "G", "A", "Bb"]
        note = self.match_notes_to_midi_numbers()
        random_list = []
        random_list2 = []
        for i in range(5):
            r=random.randint(0,len(scale)-1) #notes in scale
            random_list.append(r)
        for i in range(5):
            r=random.randint(3,6) #octaves
            random_list2.append(r)

        sequence = music_pb2.NoteSequence()
        index1 = scale[random_list[0]]
        index2 = scale[random_list[1]]
        index3 = scale[random_list[2]]
        index4 = scale[random_list[3]]
        index5 = scale[random_list[4]]
        sequence.notes.add(pitch=note[index1][random_list2[0]], start_time=0.0, end_time=1, velocity=90)
        sequence.notes.add(pitch=note[index2][random_list2[1]], start_time=1, end_time=1.5, velocity=90)
        sequence.notes.add(pitch=note[index3][random_list2[2]], start_time=1.5, end_time=2.5, velocity=90)
        sequence.notes.add(pitch=note[index4][random_list2[3]], start_time=2.5, end_time=3, velocity=90)
        sequence.notes.add(pitch=note[index5][random_list2[4]], start_time=3, end_time=4, velocity=90)


        sequence.total_time = 4
        sequence.tempos.add(qpm=60);
        return sequence

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
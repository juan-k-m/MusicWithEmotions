from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.improv_rnn import improv_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2

from magenta.models.shared import sequence_generator
from magenta.pipelines import chord_pipelines
from magenta.pipelines import melody_pipelines


from MusicWithEmotions.services.sequencemaker import Sequencemaker
import datetime
import note_seq
from midi2audio import FluidSynth
import os

'''Class for load and create music with improv_rnn magenta model'''
# Import dependencies.
class Magentaimprov:

    def __init__(self):
        self.initialnotes = None 
        self.model = None
        self.midicreated = None
        self.emotion = 'default'
        self.sequence = None
        self.sequencemaker = Sequencemaker()

    def get_root_dir(self):
        cwd = os.getcwd()
        return os.path.join(cwd)
    
    def get_generated_midi_file(self):
        self.create_sequence()
        self.load_model()
        self.generate_music()
        return self.transform_seq_to_midi()



    def generate_music(self):
        self.create_sequence_testing()
        input_sequence = self.initialnotes # 
        print(input_sequence)
        num_steps = 80 #was 128 change this for shorter or longer sequences
        temperature = 1.2
        # Set the start time to begin on the next step after the last note ends.
        last_end_time = (max(n.end_time for n in input_sequence.notes)
                          if input_sequence.notes else 0)
        qpm = input_sequence.tempos[0].qpm 
        seconds_per_step = 60.0 / qpm / self.model.steps_per_quarter
        total_seconds = num_steps * seconds_per_step
        print(last_end_time + seconds_per_step)
        generator_options = generator_pb2.GeneratorOptions()
        generator_options.args['temperature'].float_value = temperature
        #generator_options.args['backing_chords'].string_value = 'C Am'
        #generator_options.args['primer_melody'].int_value = 60#[60, -2, 60, -2, 67, -2, 67, -2]
        #generate_section = generator_options.generate_sections.add(start_time=0, end_time=20)
        generate_section = generator_options.generate_sections.add(backing_chords='C Am', primer_melody=[60, -2, 60, -2, 67, -2, 67, -2])
        generate_section = generator_options.generate_sections.add(
          start_time=last_end_time + seconds_per_step,
          end_time=total_seconds)

        # Ask the model to continue the sequence.
        self.midicreated =  self.model.generate(input_sequence, generator_options)
        

    def load_model(self):
        root_dir = self.get_root_dir()
        model_location = os.path.join(root_dir,"MusicWithEmotions","services","magmodels","chord_pitches_improv.mag")
    
        bundle = sequence_generator_bundle.read_bundle_file(model_location)
        generator_map = improv_rnn_sequence_generator.get_generator_map()
        melody_rnn = generator_map['chord_pitches_improv'](checkpoint=None, bundle=bundle)
        melody_rnn.initialize()
        self.model = melody_rnn
    
    def create_sequence_testing(self, basicnotes=None):
        twinkle_twinkle = music_pb2.NoteSequence()
        twinkle_twinkle.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=60, start_time=0.5, end_time=1.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=67, start_time=1.0, end_time=1.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=67, start_time=1.5, end_time=2.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=69, start_time=2.0, end_time=2.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=69, start_time=2.5, end_time=3.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=67, start_time=3.0, end_time=4.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=65, start_time=4.0, end_time=4.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=65, start_time=4.5, end_time=5.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=64, start_time=5.0, end_time=5.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=64, start_time=5.5, end_time=6.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=62, start_time=6.0, end_time=6.5, velocity=80)
        twinkle_twinkle.notes.add(pitch=62, start_time=6.5, end_time=7.0, velocity=80)
        twinkle_twinkle.notes.add(pitch=60, start_time=7.0, end_time=8.0, velocity=80) 
        twinkle_twinkle.total_time = 8

        twinkle_twinkle.tempos.add(qpm=60)
        self.initialnotes =  twinkle_twinkle

    def create_sequence(self, basicnotes=None):
        sequence = music_pb2.NoteSequence()
        
        for index,note in enumerate(self.initialnotes):

        	#put each note into the squence
        	#if it is the first note:
        	if index == 0:
        	    sequence.notes.add(pitch=note, start_time=0.0, end_time=0.5, velocity=90)
        	else:
        		sequence.notes.add(pitch=note, start_time=float(index-1), end_time=float(index-0.5), velocity=90)
        

        sequence.total_time = int(len(self.initialnotes)/2)
        sequence.tempos.add(qpm=60);
        
        self.sequence = sequence

    def transform_seq_to_midi(self):

        e = datetime.datetime.now()

        root_dir = self.get_root_dir()
       
        today = str(e.strftime("%Y-%m-%d-%H-%M-%S"))
        basename = self.emotion + today + '.mid'
        midi_location = os.path.join(root_dir,"ui","midi", basename)

        note_seq.sequence_proto_to_midi_file(self.midicreated, midi_location)
        return basename
        #return self.midicreated

    def test_utils(self):
        for number in range(8):
            print(float(number-1), float(number-0.5))

if __name__ == '__main__':

    test = Magentaimprov()
    #test.test_utils()
    #test.create_sequence()
    #test.load_model()
    #print(type(test.create_sequence()))
    #seq = test.create_sequence()
    midi = test.load_model()
    test.generate_music()
    print(midi)




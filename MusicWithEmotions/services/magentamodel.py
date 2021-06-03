# Import dependencies.
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2

from note_seq.protobuf import music_pb2
import note_seq
from midi2audio import FluidSynth
import os


'''class created tpo interact with the magenta model'''
class Magentamodel:

    def __init__(self):
    	self.basicsequence = None
    	self.model = None
    	self.midicreated = None
    
    def get_generated_midi_file(self):
        self.create_sequence()
        self.load_model()
        self.generate_music()
        return self.transform_seq_to_midi()



    def generate_music(self):
        input_sequence = self.basicsequence # change this to teapot if you want
        num_steps = 128 # change this for shorter or longer sequences
        temperature = 1.0 # the higher the temperature the more random the sequence.

        # Set the start time to begin on the next step after the last note ends.
        last_end_time = (max(n.end_time for n in input_sequence.notes)
                          if input_sequence.notes else 0)
        qpm = input_sequence.tempos[0].qpm 
        seconds_per_step = 60.0 / qpm / self.model.steps_per_quarter
        total_seconds = num_steps * seconds_per_step

        generator_options = generator_pb2.GeneratorOptions()
        generator_options.args['temperature'].float_value = temperature
        generate_section = generator_options.generate_sections.add(
          start_time=last_end_time + seconds_per_step,
          end_time=total_seconds)

        # Ask the model to continue the sequence.
        self.midicreated =  self.model.generate(input_sequence, generator_options)
        

    def load_model(self):
        cwd = os.getcwd()
        root_dir = os.path.join(cwd)
   
        model_location = os.path.join(root_dir,"MusicWithEmotions","services","magmodels","basic_rnn.mag")
        #bundle = sequence_generator_bundle.read_bundle_file('services/magmodels/basic_rnn.mag')
        bundle = sequence_generator_bundle.read_bundle_file(model_location)
        generator_map = melody_rnn_sequence_generator.get_generator_map()
        melody_rnn = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
        melody_rnn.initialize()
        self.model = melody_rnn
    
    def create_sequence(self, basicnotes=None):
        twinkle_twinkle = music_pb2.NoteSequence()
        # Add the notes to the sequence.
        twinkle_twinkle.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=90)
        twinkle_twinkle.notes.add(pitch=70, start_time=0.5, end_time=1.0, velocity=90)
        twinkle_twinkle.notes.add(pitch=80, start_time=1.0, end_time=1.5, velocity=90)
        twinkle_twinkle.notes.add(pitch=90, start_time=1.5, end_time=2.0, velocity=90)
        twinkle_twinkle.total_time = 8
        twinkle_twinkle.tempos.add(qpm=60)
        self.basicsequence =  twinkle_twinkle

    def transform_seq_to_midi(self):
    	return note_seq.sequence_proto_to_midi_file(self.midicreated,'test_2.mid')


if __name__ == '__main__':

    test = Magentamodel()
    test.create_sequence()
    test.load_model()
    print(type(test.create_sequence()))
    #seq = test.create_sequence()
    #midi = test.transform_seq_to_midi(test.basicsequence)

    
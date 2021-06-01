from MusicWithEmotions.services.music import Music
from note_seq.protobuf import music_pb2
import note_seq
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2


'''Class to process the input from the encoder part and
generate the music composition '''
class Musicgeneration:
    def __init__(self):
        self.music_helper = Music()
    def get_notes_from_emotion(self, emotion):
        return self.music_helper.get_modes_to_chords()
    
    def make_music(self):
    	sequence = self.create_sequence()
    	model = self.load_model()
    	print(type(model))
    	print(model.__dict__)
    	#self.create_music_from_sequence(sequence,model)
    	print('done!')

    def create_sequence(self):
        twinkle_twinkle = music_pb2.NoteSequence()

        # Add the notes to the sequence.
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
        twinkle_twinkle.notes.add(pitch=60, start_time=7.0, end_time=8.0, velocity=80) 
        twinkle_twinkle.notes.add(pitch=62, start_time=6.5, end_time=7.0, velocity=80)
        twinkle_twinkle.total_time = 8

        twinkle_twinkle.tempos.add(qpm=60);
        return twinkle_twinkle

    def load_model(self):
        bundle = sequence_generator_bundle.read_bundle_file('./basic_rnn.mag')
        generator_map = melody_rnn_sequence_generator.get_generator_map()
        melody_rnn = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
        melody_rnn.initialize()
        return melody_rnn

    def create_music_from_sequence(self, sequence, model):
        # Model options. Change these to get different generated sequences! 
        input_sequence = sequence # change this to teapot if you want
        num_steps = 128 # change this for shorter or longer sequences
        temperature = 1.0 # the higher the temperature the more random the sequence.

        # Set the start time to begin on the next step after the last note ends.
        last_end_time = (max(n.end_time for n in input_sequence.notes)
                          if input_sequence.notes else 0)
        qpm = input_sequence.tempos[0].qpm 
        seconds_per_step = 60.0 / qpm / model.steps_per_quarter
        total_seconds = num_steps * seconds_per_step

        generator_options = generator_pb2.GeneratorOptions()
        generator_options.args['temperature'].float_value = temperature
        generate_section = generator_options.generate_sections.add(
          start_time=last_end_time + seconds_per_step,
          end_time=total_seconds)

        # Ask the model to continue the sequence.
        sequence = model.generate(input_sequence, generator_options)

        

        return type(sequence)

if __name__ == '__main__':
	test = Musicgeneration()
	print (test.make_music())
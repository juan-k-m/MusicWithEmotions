import streamlit as st
from MusicWithEmotions.runprograma import Runprograma
from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.encoderemotion import Encoderemotion

from magenta.contrib import training as contrib_training
from midi2audio import FluidSynth

import os
from PIL import Image
import numpy as np
import pandas as pd

image = Image.open('ui/mwe_logo.PNG')
st.image(image, use_column_width=True)

st.markdown("""
## Lets create some music
#### just upload an image or shoot a foto to create your **individual** song
###
###
""")

# And within an expander

form = st.form(key='my-form')
picture = form.file_uploader("your image", type="jpg")
#name = form.text_input('Enter your name')
submit = form.form_submit_button('Create music with emotions!')

if picture:

    image = Image.open(picture)
    img = np.array(image)
    st.image(image, caption='Your Image.', width=300, use_column_width=False)
    test_ = Runprograma(img)
    midi, emotion = test_.run()
    st.write('')
    st.write(f"Detected emotion: {emotion}")
    st.write('')
    #st.write(midi.lower())

if submit:

    #run_program = Runprogram(picture)
    #st.write(run_program.run())
    #st.image(run_program.picture, caption='Your Image.', width=100,  use_column_width=False)

    midi_file_path = f"ui/midi/{midi}"
    wave_file_path = midi_file_path.replace(".mid", ".wav")

    fs = FluidSynth()
    fs.midi_to_audio(midi_file_path, wave_file_path)

    st.audio(wave_file_path, format='audio/ogg', start_time=0)

    # removing files after playing it

    #if os.path.exists(midi_file_path):
    os.remove(midi_file_path)

    #if os.path.exists(wave_file_path):
    os.remove(wave_file_path)
    st.markdown(".mid and .wav files are deleted")
import streamlit as st
from MusicWithEmotions.runprograma import Runprograma
from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.encoderemotion import Encoderemotion

from midi2audio import FluidSynth

from PIL import Image
import numpy as np
import pandas as pd

image = Image.open('image/logo.png')
st.image(image, use_column_width=True)

st.header("**Lets create music**")

st.markdown("""
#
#
#### Upload your image to create your **individual** song
###
""")

# And within an expander

form = st.form(key='my-form')
picture = form.file_uploader("", type="jpg")
#name = form.text_input('Enter your name')
submit = form.form_submit_button('Create music with emotions!')

if picture:

    image = Image.open(picture)
    img = np.array(image)
    st.image(image, caption='', width=300, use_column_width=False)

if submit and picture:

    app = Runprograma(img)
    ui_reply = app.run()
    if ui_reply == 'No face detected':
        st.warning("No face detected. Please upload a different picture")
        #st.write("No face detected. Please upload a different picture")
    else:
        midi, emotion = ui_reply
        #st.write('')
        #st.header(f"Detected emotion: **{emotion}**")
        st.success(f"Detected emotion: **{emotion}**")
        st.write('')
        midi_file_path = f"midi/{midi}"
        wave_file_path = midi_file_path.replace(".mid", ".wav")

        fs = FluidSynth()
        fs.midi_to_audio(midi_file_path, wave_file_path)

        st.audio(wave_file_path, format='audio/wav', start_time=0)
        st.markdown(
            "   You like the song? Download it by right-clicking on the player"
        )

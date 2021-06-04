import streamlit as st
# from MusicWithEmotions.runprograma import Runprograma
# from MusicWithEmotions.facerecognition import Facerecognition
# from MusicWithEmotions.musicgeneration import Musicgeneration
# from MusicWithEmotions.encoderemotion import Encoderemotion

from midi2audio import FluidSynth 

from PIL import Image
import numpy as np
import pandas as pd



image = Image.open('ui/mwe_logo.PNG')
st.image(image, use_column_width=True)



# dataframe that stores potential emotions
# emotions_df = pd.DataFrame({
#           "emotion": ["happy", "sad", "scared", "angry", "neutral", "surprised", "disgusted"]
#         })

#emotions_list = ["happy", "sad", "scared", "angry", "neutral", "surprised", "disgusted"]

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
    st.image(image, caption='Your Image.', width=100,  use_column_width=False)
    test_ = Runprograma(image)
    midi = test_.run()
    st.write(type(midi))
    st.write(midi.lower())
 


if submit:

    #run_program = Runprogram(picture)
    #st.write(run_program.run())
    #st.image(run_program.picture, caption='Your Image.', width=100,  use_column_width=False)

    midi_file_path = f"ui/midi/{midi}"
    wave_file_path = midi_file_path.replace(".mid",".wav")

    fs = FluidSynth()
    fs.midi_to_audio(midi_file_path, wave_file_path)

    st.write("here we test the easy way")
    st.audio(wave_file_path, format='audio/ogg', start_time=0)
    st.markdown("   You like the song? Download it by right-clicking on the player")

    st.write("here we test the way with the opener")
    audio_file_wav = open(wave_file_path, 'rb')
    audio_bytes_wav = audio_file_wav.read()
    st.audio(audio_bytes_wav, format='audio/wav', start_time=0)
    



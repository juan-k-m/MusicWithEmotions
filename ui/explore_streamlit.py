import streamlit as st
from MusicWithEmotions.runprograma import Runprograma
from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.encoderemotion import Encoderemotion
import altair as alt


from PIL import Image
import numpy as np
import pandas as pd
from numpy import random



image = Image.open('mwe_logo.PNG')
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
    st.write(test_.run())
if submit:

    #run_program = Runprogram(picture)
    #st.write(run_program.run())
    #st.image(run_program.picture, caption='Your Image.', width=100,  use_column_width=False)
    audio_file = open('chopin.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')



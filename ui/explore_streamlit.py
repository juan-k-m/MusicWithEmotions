import streamlit as st
from MusicWithEmotions.musicgeneration import Musicgeneration

import altair as alt


from PIL import Image
import numpy as np
import pandas as pd
from numpy import random


test = Musicgeneration()

image = Image.open('mwe_logo.PNG')
st.image(image, use_column_width=True)



# dataframe that stores potential emotions
# emotions_df = pd.DataFrame({
#           "emotion": ["happy", "sad", "scared", "angry", "neutral", "surprised", "disgusted"]
#         })

emotions_list = ["happy", "sad", "scared", "angry", "neutral", "surprised", "disgusted"]

st.markdown("""

## Lets create some music

#### just upload an image or shoot a foto to create your **individual** song
###
###

""")

##### Initialize flags
flag = False
flag_call_program = False
our_test = None
flag_play = False

# And within an expander
my_expander = st.beta_expander("Upload a foto...", expanded=False)
with my_expander:
    uploaded_file = st.file_uploader("your image", type="jpg")



if uploaded_file is not None:
    #TODO clean the input from the userxc
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Image.', width=100,  use_column_width=False)
    flag = True
    
if flag is True:
    st.button('Create music from foto!')
    flag_call_program = True
    #st.balloons()

if flag_call_program is True:
   our_test = test.get_notes_from_emotion('happy')
   #returns a MIDI file
   flag_play = True
  
if flag_play is True:
    st.button('Play music from foto!')
    audio_file = open('chopin.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')


import streamlit as st

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

emotions_list = ["happy", "sad", "scared", "angry", "neutral", "surprised", "disgusted"]

st.markdown("""

## Lets create some music

#### just upload an image or shoot a foto to create your **individual** song
###
###

""")


# And within an expander
my_expander = st.beta_expander("Upload a foto...", expanded=False)
with my_expander:
    uploaded_file = st.file_uploader("your image", type="jpg")


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Image.', width=500,  use_column_width=False)
    st.write("Recognizing emotion...")

    # fake algorithm
    #@st.cache
    random_number = random.randint(0, 7)
    your_emotion = emotions_list[random_number]
    #your_emotion = predict(uploaded_file)

    st.write(f'i see you feel {your_emotion}')

# into sidebar for elements
# add_selectbox = st.sidebar.selectbox(
#     "'choose instruments'",
#     ('Guitar', 'Drums', 'Piano', 'Violin')
# )

instruments = st.sidebar.multiselect("choose instrument", 
        ('Guitar', 'Drums', 'Piano', 'Violin')
        )

# instruments = ['Guitar', 'Drums', 'Piano', 'Violin']
# options = st.multiselect(
#    'choose instruments',
#    instruments,
#    instruments[:2]
#    )
#st.write('You selected:', options)

if st.button('Create music from foto!'):
    st.balloons()

if st.button('Play music from foto!'):
    audio_file = open('chopin.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')


# select your emotional state without foto

st.markdown("""
##
## You don't want to deal with pictures?
#### Just select three emotional states that would describe how you feel right now
# 
""")

# your_emotion = st.selectbox(
#      'How do you feel right now?',
#      emotions_list
#         )

options = st.multiselect(
   'how do you feel?',
   emotions_list,
   emotions_list[:2]
   )
#st.write('You selected:', your_emotion)
st.markdown("""
##
""")

st.write(f'i see you feel **{options[0]}**, **{options[1]}** and **{options[2]}**')

st.markdown("""
##
""")


if st.button('Create music from selected emotions!'):
    st.balloons()

if st.button('Play music from selected emotions!'):
    audio_file = open('chopin.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')



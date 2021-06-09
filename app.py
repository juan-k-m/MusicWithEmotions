import streamlit as st
from MusicWithEmotions.runprograma import Runprograma
from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.encoderemotion import Encoderemotion

from midi2audio import FluidSynth

from PIL import Image
import numpy as np
import pandas as pd

# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded

# header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
#     img_to_bytes("header.png")
# )
# st.markdown(
#     header_html, unsafe_allow_html=True,
# )

# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# path = "..."
# image = Image.open(path)

# st.image(image, width = 150)

webpage = st.sidebar.radio("Navigation",
                           ["Music generator", "How it works", "Team"])

if webpage == 'Music generator':

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

elif webpage == 'How it works':
    image = Image.open('image/how_it_works.PNG')
    st.image(image, use_column_width=True)

elif webpage == 'Team':
    st.header("Project Team")
    st.write('')
    st.write('')

    st.markdown("### Juan Carlos Mayoral Molina")
    image_1 = Image.open('image/juan.jpg')
    text_1 = """I find extremely interesting the possibilities that Data Science 
    offers to relate areas such as: programming, statistics, a lgebra, probability, 
    among others, which for me are of great interest. And that through techniques 
    of analysis of large amounts of data we can find relationships that allow us 
    to see these large amounts of data from different perspectives and thus help us 
    to obtain new information. I am very interested in the topic of artificial 
    intelligence, its areas of study and application. I intend to learn more about some of 
    these areas such as Machine Learning and Deep Learning. I am interested in working on 
    a project to apply this knowledge, so I will find a job after this course."""
    st.image(image_1, width=170, use_column_width=False)
    st.write(text_1)
    st.write("")

    st.markdown("### Georgios-Alexandros Christodoulou")
    image_2 = Image.open('image/georgios.jpg')
    text_2 = """I find the whole concept of Data Science fascinating, i allways liked 
    Statistics so that went well... I don't have a background in Data Science or 
    Web Dev, i studied Agriculture in University, though i never finished my studies. 
    I did a lot of statistics there, so here goes that...If i remember something else i will update :)"""
    st.image(image_2, width=170, use_column_width=False)
    st.write(text_2)
    st.write("")

    st.markdown("### Simone Totino")
    image_3 = Image.open('image/totino.jpg')
    text_3 = """Management consultant (energy business) currently on a sabbatical year. 
    Decided to cure my digital illiteracy and very curious to discover where this BootCamp 
    will lead me… Committed to apply my current and future skills to have a more sustainable 
    impact. Passionate about travelling, enthusiastic about outdoor activities, in love with the sea."""
    st.image(image_3, width=170, use_column_width=False)
    st.write(text_3)
    st.write("")

    st.markdown("### Daniil Volf")
    image_4 = Image.open('image/danja.jpg')
    text_4 = """Hi Im Daniel, my background is innovation management and engineering. Usually my role in 
    IT projects was project or product manager and now i want to dive deeper into programming and Data Science!"""
    st.image(image_4, width=170, use_column_width=False)
    st.write(text_4)
    st.write("")

# col1, col2, col3 = st.beta_columns([1,6,1])

# with col1:
# st.write("")

# with col2:
# st.image("https://i.imgflip.com/amucx.jpg")

# with col3:
# st.write("")
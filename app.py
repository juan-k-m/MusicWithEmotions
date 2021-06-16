import streamlit as st
from MusicWithEmotions.runprograma import Runprograma
from MusicWithEmotions.facerecognition import Facerecognition
from MusicWithEmotions.musicgeneration import Musicgeneration
from MusicWithEmotions.encoderemotion import Encoderemotion

from midi2audio import FluidSynth

from PIL import Image
import numpy as np
import pandas as pd

CSS = """

    button.css-keg18t.edgvbvh5
    {
    width: 90%;
    margin: 10px auto;
    display: block;
    text-decoration: none;
    background-color: #245ade;
    color: white;
    font-weight: bold;
    padding: 15px 40px;
    border-radius: 4px;
    transition: all 0.2s ease-in-out;
    }
    button.css-10kp2cd.edgvbvh5 {
    width: 90%;
    margin: 10px auto;
    display: block;
    background: #04C2AF;
    padding: 9px;
    opacity: .9
    }
    .css-1lcbmhc{
    background-color: white
    }


    button.css-10kp2cd.edgvbvh5:hover {

    color: white;
    opacity: 1

    }
    section.main.css-1v3fvcr.eknhn3m1 {
    background: rgb(34, 89, 155);
}

    button.css-keg18t.edgvbvh5:hover 
    {
    color: rgba(255, 255, 255, 1);
    box-shadow: 0 5px 15px rgba(145, 92, 182, .4);
    }


    section.css-6h50dk.exg6vvm0 {
    background: transparent;
    }

    .css-1v0mbdj.etr89bj1 {
    border-radius: 50%;
    }
    section[data-testid="stSidebar"] > div{
    background: rgb(50, 50, 62);
    }

    .block-container{
    background-color: transparent
    }

    .st-cl.st-bl.st-bm.st-bn.st-bo.st-cf.st-b2.st-bz.st-cg:hover {
    background: transparent;
   }
    .st-cl.st-bl.st-bm.st-bn.st-bo.st-cf.st-b2.st-bz.st-cg {
    background: rgb(50, 50, 62);
   }

   div[data-testid="stBlock"] img{

   border-radius:50%;

   }
   button.css-10kp2cd.edgvbvh1:hover {
    border-color: white;
    color: #e9e9e9;
}

button.css-10kp2cd.edgvbvh1 {
    background: transparent;
}

.element-container.css-1e5imcs.e1tzin5v1:nth-child(2) img {
    border-radius: 0 !important;
}
.st-bw.st-cb.st-cc.st-ae.st-af.st-ag.st-ah.st-ai.st-aj {
    color: white;
}
label.css-145kmo2.effi0qh0 {
    color: white;
}
.st-bh.st-bk.st-bl.st-bm.st-bn.st-bo.st-az.st-b4.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by.st-b2.st-bz:active {
    background: rgb(34, 89, 155);
}
.st-bh.st-bk.st-bl.st-bm.st-bn.st-bo.st-az.st-b4.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by.st-b2.st-bz {
    background: rgb(34, 89, 155);
}
section.main.css-1v3fvcr.eknhn3m1 {
    color: white;
}
h3 {
    color: white;
}
small.css-t2ek9a.euu6i2w0 {
    color: white;
}
button.css-qbe2hs.edgvbvh5 {
    width: 90%;
    padding: 17px;
    border-radius: 8px;
    background: gray;
    margin: 0 auto;
    display: block;
    background:#04C2AF;
}

.css-qbe2hs:active {
    border-color: transparent
}
.css-qbe2hs:hover {
    border-color: white;
    color: #f9f9f9;
}

button.css-qbe2hs.edgvbvh1 {
    background: transparent;
    padding: 12px 62px;
    margin-right: 20px;
    border-color: yellowgreen;
}

.css-1ekf893.e16nr0p30 p {
    color: white;
}
.css-j2eyvp.epcbefy1 {
    padding: 8px 19px 40px;
}

.block-container.css-hi6a2p.eknhn3m2 div:nth-child(8) div {
    margin: 23px auto;
}

.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-cv.st-am.st-b8.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-cw.st-av.st-aw.st-ax.st-ay.st-az.st-b9.st-b1.st-b2.st-b3.st-b4.st-b5.st-cx {
    padding: 22px 37px;
    color: white;
    font-size: 23px !important;
    border-radius: 12px;
}
.css-1ekf893.e16nr0p30 p {
    font-size: 20px !important;
}

.css-qbe2hs:active {
    
    border-color: white !important;

}

.css-qbe2hs:focus {
    box-shadow: none;
    outline: none;
}

.css-qbe2hs:focus:not(:active) {
    border-color: white;
    color: white;
}

.css-1syfshr:focus {
    box-shadow:none;
}
span.css-10trblm.e16nr0p33 {
    color: white;
}
element.style {
    width: 300px;
}

element.style {
    position: relative;
}
div[data-testid="stForm"] {
    border-color: lightgray;
    /* border-width: thin; */
}
section[data-testid="stFileUploadDropzone"] {
    background: transparent;
    color: white;
}

strong {
    color: white;
}

.block-container.css-hi6a2p.eknhn3m2 div:nth-child(6) img {
    border-radius: 50% !important;
    margin: 10px 0 10px 0;
}

.block-container.css-hi6a2p.eknhn3m2 div:nth-child(6) div div div {
    margin: 0 auto !important;
}


.block-container.css-hi6a2p.eknhn3m2 div:nth-child(8) div img{
    border-radius:50%;
}
.stMarkdown {
    margin-top: 15px;
}
button.css-1iyw2u1.edgvbvh6 {
    color: white;
    border: none;
}

h3 {
    padding: 8px;
}

Element {

    margin-top: -25px;

}

    """

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

webpage = st.sidebar.radio("Music with emotions",
                           ["Music generator", "How it works", "Team"])

if webpage == 'Music generator':

    image = Image.open('image/logo_.png')
    st.image(image, width=420, use_column_width=False)
    st.write('')
    st.write('')
    st.header("**Let's create music**")

    st.markdown("""

    #### Upload your image to create your **individual** song
    ###
    """)
    
    # UPLOADER
    form = st.form(key='my-form')
    picture = form.file_uploader("", type="jpg")
    #name = form.text_input('Enter your name')
    submit = form.form_submit_button('Create music with emotions!')

    if picture:

        # PICTURE DISPLAY

        image = Image.open(picture)
        img = np.array(image)

        #col1, col2, col3 = st.beta_columns([1, 1, 1])
        #
        #with col2:
        st.image(image, width=300, use_column_width=False)

        #with col3:
        #    st.write("")

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
    st.markdown("### Georgios-Alexandros Christodoulou")
    image_2 = Image.open('image/georgios.jpg')
    text_2 = """I find the whole concept of Data Science fascinating, i allways liked 
    Statistics so that went well... I don't have a background in Data Science or 
    Web Dev, i studied Agriculture in University, though i never finished my studies. 
    I did a lot of statistics there, so here goes that...If i remember something else i will update :)"""

    col1, col2, col3 = st.beta_columns([4, 10, 1])
    with col1:
        st.image(image_2, width=150, use_column_width=False)

    with col2:
        st.write(text_2)

    with col3:
        st.write("")
    st.write("")

    st.markdown("### Simone Totino")
    image_3 = Image.open('image/totino.jpg')
    text_3 = """Management consultant (energy business) currently on a sabbatical year. 
    Decided to cure my digital illiteracy and very curious to discover where this BootCamp 
    will lead me… Committed to apply my current and future skills to have a more sustainable 
    impact. Passionate about travelling, enthusiastic about outdoor activities, in love with the sea."""

    col1, col2, col3 = st.beta_columns([4, 10, 1])
    with col1:
        st.image(image_3, width=150, use_column_width=False)

    with col2:
        st.write(text_3)

    with col3:
        st.write("")
    st.write("")

    st.markdown("### Daniil Volf")
    image_4 = Image.open('image/danja.jpg')
    text_4 = """Hi Im Daniel, my background is innovation management and engineering. Usually my role in 
    IT projects was project or product manager and now i want to dive deeper into programming and Data Science!"""

    col1, col2, col3 = st.beta_columns([4, 10, 1])
    with col1:
        st.image(image_4, width=150, use_column_width=False)

    with col2:
        st.write(text_4)

    with col3:
        st.write("")
    st.write("")


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

    col1, col2, col3 = st.beta_columns([4, 10, 1])
    with col1:
        st.image(image_1, width=150, use_column_width=False)

    with col2:
        st.write(text_1)

    with col3:
        st.write("")
    st.write("")

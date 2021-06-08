FROM python:3.8-buster

COPY MusicWithEmotions /MusicWithEmotions

COPY ui /ui

COPY raw_data /raw_data

COPY app.py /app.py

COPY requirements.txt /requirements.txt

COPY setup.py /setup.py

COPY scripts /scripts

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install --use-feature=in-tree-build .
 
RUN apt-get update && apt-get install -y apt-transport-https -y

RUN apt-get install libjack-dev -y

RUN apt-get install libasound2-dev -y

RUN apt-get install portaudio19-dev -y

RUN apt-get install autoconf -y

RUN apt-get install build-essential -y

RUN apt-get install autogen -y

RUN apt-get install automake -y

RUN apt-get install libflac-dev -y

RUN apt-get install libogg-dev -y

RUN apt-get install libtool -y

RUN apt-get install libvorbis-dev -y

RUN apt-get install libopus-dev -y

RUN apt-get install libmp3lame-dev -y

RUN apt-get install libmpg123-dev -y

RUN apt-get install pkg-config -y

RUN apt-get install ffmpeg libsm6 libxext6 fluidsynth -y

RUN pip install opencv-python

################last part or command that is going to be run for Docker:
#EXPOSE 8501
#ENTRYPOINT ["streamlit","run"]
#CMD ["runtest.py"]
CMD streamlit run app.py
FROM python:386-buster

COPY MusicWithEmotions /MusicWithEmotions

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

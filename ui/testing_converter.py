import io

import numpy as np
import pretty_midi
import streamlit as st
from scipy.io import wavfile
from midi2audio import FluidSynth


fs = FluidSynth()
fs.midi_to_audio('abba_dq.mid', 'abba_dq.wav')

st.audio('abba_dq.wav', format='audio/ogg', start_time=0)
st.markdown("   You like the song? Download it by right-clicking on the player")
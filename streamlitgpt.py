import streamlit as st 
import os
import streamlit.components.v1 as components


def audio_test():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    st.title('Audio Test')
    st.write('\n \n')
    
    instance=st_audiorec()
    
audio_test()
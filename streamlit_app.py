import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon='tada', layout='wide')

st.header("Are you the xXDRAGONSLAYERXx?")
st.subheader("Enter your name to find out if you are the DRAGONSLAYER")
name = st.text_input("What is your name?")

def dragon(name):
    if name == "Jake":
        st.write("You are the DRAGONSLAYER")
    elif name == "jake":
        st.write("You are the DRAGONSLAYER")
    else:
        st.write("You are not the dragonslayer.")

if name:
    answer = dragon(name)


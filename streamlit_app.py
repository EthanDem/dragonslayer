import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon='tada', layout='wide')

st.header("Are you the xXDRAGONSLAYERXx?")
st.subheader("Enter your name to find out if you are the one true Dragon Slayer")
name = st.text_input("What is your name?").lower()

def dragon(name):
    if name == "Jake":
        st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "jake":
        st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "Jake Golden":
        st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "jake golden":
        st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "Jake ":
            st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "jake ":
            st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "Jake Golden ":
            st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    elif name == "jake golden ":
            st.header("Congrats, You are the 🐲⚔️ DRAGONSLAYER ⚔️🐲")
    else:
        st.header(name + " , you are not the dragonslayer.")

if name:
    answer = dragon(name)


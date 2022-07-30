import streamlit as st
from streamlit_option_menu import option_menu

#Hide logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home, Projects", "Contact Me"],
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact Me":
    st.title(f"You have selected {selected}")
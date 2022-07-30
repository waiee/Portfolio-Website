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
        menu_title=None,
        options=["Home", "Projects", "Contact Me"],
        icons=["house", "book", "telephone"],
        default_index=0, #set homepage
    )

if selected == "Home":
    st.title(f"{selected}")
if selected == "Projects":
    st.title(f"{selected}")
if selected == "Contact Me":
    st.title(f"{selected}")
from tkinter import font
from tkinter.messagebox import NO
from turtle import right
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="waieezainol.com", page_icon=":computer:", layout="wide")
dp_image = Image.open("image/removebgWaiee.png")

#Call LOTTIE Animation
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- LOAD ASSET ---
lottie_file = load_lottie("https://assets7.lottiefiles.com/packages/lf20_dlw10cqe.json")

#Insert BG URL
import base64
def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: contain;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

#### HORIZONTAL MENU#####
# selected = option_menu(
#         menu_title=None,
#         options=["Home", "Projects", "Contact"],
#         icons=["house", "book", "telephone"],
#         default_index=0, #set homepage
#         orientation="horizontal",
#         styles={      
#             #will add later
#         }
#     )

#Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "telephone"],
        default_index=0, #set homepage
    )

# --- HOME ---
if selected == "Home":
    with st.container():
        add_bg('image/wallpaper1.png')
    # st.title(f"{selected}")
        image_column, right_column = st.columns((1,2))
        with image_column:
            #insert images
                st.image(dp_image, caption="")
        with right_column:
            st.subheader("Hi, I am Waiee :wave:")
            st.title("Bachelor of Computer Science in Data Science")
            st.write("I am passionate in Data Science, Machine Learning, and Artificial Intelligence.")
            st.write("[Visit My Github >](https://github.com/waiee)")
        #st_lottie(lottie_file,height=500 ,key="coding")

### WHAT I DO ###
    with st.container():
        st.write("---")
        st.header("What I Do")
        st.write("##")
        st.write(
                """
                Do follow my LinkedIn!
                """
            )
        st.write("[LinkedIn Account >](https://www.linkedin.com/in/waiee-zainol-9b00461ab/)")

# --- PROJECTS ---
if selected == "Projects":
    # st.title(f"{selected}")
    with st.container():
        # st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        # with image_column:

        with text_column:
            st.subheader("This is my fucking project!")
            st.write(
                """
                Learn how to use this fucking streamlit.           
                """
            )
            st.markdown("[Tutorial Video...]()")
        #new project section
        


# --- CONTACT ---
if selected == "Contact":
    # st.title(f"{selected}")
    with st.container():
        # st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        #Documentation
        contact_form = """
        <form action="https://formsubmit.co/waiee_z@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form> 
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
from turtle import right
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="waieezainol.com", page_icon=":computer:", layout="wide")
dp_image = Image.open("image/IMG_4825.jpeg")

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

#Hide logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
    # st.title(f"{selected}")
        st.subheader("Hi, I am Waiee :wave:")
        st.title("Bachelor of Computer Science in Data Science")
        st.write("I am passionate in Data Science, Machine Learning, and Artificial Intelligence.")
        st.write("[Learn More >](https://github.com/waiee)")

    ### WHAT I DO ###
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
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
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert images
                st.image(dp_image, caption="")
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
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        #Documentation
        contact_form = """
        <form action="https://formsubmit.co/your@email.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" required>
            <button type="submit">Send</button>
        </form> 
     """
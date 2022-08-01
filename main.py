from turtle import right
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="waieezainol.com", page_icon=":computer:", layout="wide")

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

#HomePage
if selected == "Home":
    with st.container():
    # st.title(f"{selected}")
        st.subheader("Hi, I am Waiee :wave:")
        st.title("Bachelor of Computer Science in Data Science")
        st.write("I am passionate in Data Science, Machine Learning, and Artificial Intelligence.")
        st.write("[Learn More >](https://github.com/waiee)")

    # img = Image.open("IMG_4825.jpeg")
    # st.image(img, width=500, caption="")

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
        

#Projects
if selected == "Projects":
    st.title(f"{selected}")
    st.write("This is my project section")

#Contact
if selected == "Contact":
    st.title(f"{selected}")
    st.write("This is my contact number - 0126275758")
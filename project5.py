import streamlit as st

# Text title
st.title("Testing Streamlit")

#Header/subHeader
st.header("This is header")
st.subheader("This is a subheader")

#Text
st.text("Hello world")

#Markdown
st.markdown("### This is a markdown")

#Error/colourful text
st.success("Successful!")
#information
st.info("Information")
#warning
st.warning("This is a warning.")
#error
st.error("This is a n error!")
#exception
st.exception("NameError(name three not defined)")

#Get help info about python
st.help(range)

#writing text
st.write("Text with write")
st.write(range(10))

#Images
from PIL import Image
img = Image.open("IMG_4825.jpeg")
st.image(img)
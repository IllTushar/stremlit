import streamlit as st
import pandas
from PIL import Image as pil


def hello_streamlit():
    # set title
    st.title("Hello Streamlit")

    # Header and Sub-Header
    st.header("Machine Learning Project")

    st.subheader("This is sub header")  # h1, h2, h3..

    # Text
    st.text("This is the text")

    # Mark down
    st.markdown(" # This is our first markdown")

    st.markdown(" ### This is our first markdown")

    # Error / Colorful text
    st.success("Successful Done")
    st.error("Error message!!")

    # information
    st.info("This is information")

    # warning
    st.warning("This is warning")

    # exception
    st.exception("This is exception")

    # help
    st.help(pandas)

    # write text super function
    st.write("Text with write")

    # image
    image = pil.open(r"C:\Users\gtush\Desktop\water_mark_image\Logo.png")
    st.image(image)
    st.image(image, width=200, caption="Simple Image")


if __name__ == '__main__':
    hello_streamlit()

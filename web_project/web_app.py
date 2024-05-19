import datetime

import streamlit as st
from PIL import Image as pil
import time


def web_app():
    st.title("First Web")
    image = pil.open(r"C:\Users\gtush\Desktop\water_mark_image\ninja.jpg")
    st.image(image, width=300, caption="Ninja")

    # video
    video = open(r"C:\Users\gtush\Desktop\water_mark_image\3209828-uhd_3840_2160_25fps.mp4", "rb")
    video_byte = video.read()
    st.video(video_byte)

    # Audio
    audio = open(r"C:\Users\gtush\Desktop\water_mark_image\wave.mp3", "rb").read()
    st.audio(audio)

    # Check box
    check_box = st.checkbox(label="Show your text")
    if check_box:
        st.text("Your text is visible!!")

    # Radio Button
    radio_btn = st.radio("Voice", ("Active", "InActive"))

    if radio_btn == "Active":
        st.success("You are active now !!")
    else:
        st.warning("You are not active !!")

    drop_down = st.selectbox("Your name", ["Aman", "Rohit", "Tushar"])
    st.write(drop_down)

    st.multiselect("Where your location", ("Delhi", "Mumbai", "Noida", "Lucknow"))

    # Slider
    st.slider("What's your level", 1, 5)

    # Button
    success_btn = st.button("Click Here")
    if success_btn:
        st.success("Click Successful")

    # Input field
    name = st.text_input("Enter your name", "Typing..")
    if st.button("Submit", key="1"):
        st.success(f"Successful Submit {name}")

    # Input area
    area = st.text_area("Enter your message", "Typing..")
    if st.button("Submit", key="2"):
        st.success(f"Your Message {area}")

    # day
    today = st.date_input("Enter your date", datetime.date.today())

    # time
    times = st.time_input("Enter your time", datetime.time())

    # import code
    st.text("Code")
    lib = st.code("import numpy as np")

    # Progress bar
    my_bar = st.progress(0)
    for p in range(10):
        my_bar.progress(p + 1)

    # Spinner Progressbar
    with st.spinner("Waiting.."):
        time.sleep(5)
    st.success("Finished!!")


if __name__ == '__main__':
    web_app()

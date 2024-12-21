from ultralytics import YOLO
from argparse import ArgumentParser
import streamlit as st
import numpy as np
from PIL import Image
from utils.centralize import centered_title, centered_subheader

def get_args():
    parser = ArgumentParser(description="Helmet Detection with YOLOv10")
    parser.add_argument(
        "--title", "-t", type=str, default="Helmet Detection with YOLOv10"
    )
    parser.add_argument(
        "--model-path", "-mp", type=str, default="./pretrained_models/best.pt"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    st.set_page_config(layout="wide")
    centered_title(args.title)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        col1, col2 = st.columns(spec=2, gap="small")
        with col1:
            centered_subheader("Original Image")
            st.image(img, caption="Uploaded Image")

        if st.button("Detect"):
            model = YOLO(args.model_path)
            output = model(img)
            for result in output:
                im = result.plot()
                im = im[:,:, ::-1] # Convert BGR2RGB
            with col2:
                centered_subheader("Detected Image")
                st.image(im, caption="Detected Image")

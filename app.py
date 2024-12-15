from ultralytics import YOLO
from argparse import ArgumentParser
import streamlit as st
import numpy as np
import cv2


def get_args():
	parser = ArgumentParser(
		description="Helmet Detection with YOLOv10")
	parser.add_argument('--image-path', '-ip', type=str, default=None)
	parser.add_argument('--model-path', '-mp', type=str, default='./pretrained_models/best.pt')
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	st.title("Helmet Detection with YOLOv10")
	print(np.__version__)
	args = get_args()
	model = YOLO(args.model_path)
	if args.image_path is None:
		print("Please give the image path")
		exit(0)
	else:
		img = cv2.imread(args.image_path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		output = model(img)
		for result in output:
			im = result.plot()
			im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
			cv2.imshow('result', im)
			cv2.waitKey(0)
	
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyOCR - Simple ocr in Python"""
__author__      = "Rafael Laurindo"
__version__ = "1.0.0"
__maintainer__ = "Rafael Laurindo"
__email__ = "rafaelfilholm@gmail.com"

import sys
import pytesseract # OCR Module
import clipboard # Module to send text to clipboard
from PIL import Image # Import Pillow to open the image

if len(sys.argv) > 1: # Check if has send path
	path_image = sys.argv[1] # Get path to image from arguments
else: 
	exit('You need to pass the path to the image!\nExample: pyocr.py /home/user/image.png')

try:
	def get_option():
		option = 0
		try:
			option = int(input("Select one option:\n1. View Text\n2. Copy to clipboard\n3. Exit\n"))
		except NameError:
			print("Option needs to be a number!")
		return option

	try:
		text = pytesseract.image_to_string(Image.open(path_image)) # Extract the text
		if len(text) > 0: # Check if has text 
			option = 0
			while option == 0:
				option = get_option()
				if option == 1:
					print(text) # Show text from image
				elif option == 2:
					clipboard.copy(str(text.encode('utf-8'))) # Send text to clipboard
					print("\nText is on clipboard!")
				elif option == 3:
					exit('You decided to leave.')
				else:
					print("\n{} is a invalid option.".format(option))
		else:
			print("This image may not contain any text.")

	except IOError, err: # Handle errors
		if err.errno == 2:
			print("Image not found!\nCheck the path and try again.")
		elif err.errno == None:
			print("The file must be a valid image.")
		else:
			print("We had a problem reading the file.\nPlease try again.")
except KeyboardInterrupt:
	exit('\nYou decided to leave.')
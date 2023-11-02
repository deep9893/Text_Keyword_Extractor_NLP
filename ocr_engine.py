# this library is used for OCR to extract text from the images

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image # this library is used to open and manipulate images
import os

class OCREngine:
    @staticmethod
    def extract_text(file_path):
        try:
            image = Image.open(file_path) # open the image
            
            text = pytesseract.image_to_string(image) # extract the text from the image
            
            return text #return the extracted text as the result
        
        except Exception as e:
            return str(e)

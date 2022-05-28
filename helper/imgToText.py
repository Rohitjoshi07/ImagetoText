from pytesseract import pytesseract

class OCR:
    def __init__(self):
        self.path = '/app/.apt/usr/bin/tesseract'

    def extract(self, filename):

        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)
            return text

        except Exception as e:
            print(e)
            return "Error"

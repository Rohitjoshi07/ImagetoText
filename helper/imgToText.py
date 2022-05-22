from pytesseract import pytesseract

class OCR:
    def __init__(self):
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #change this if installed in amother path

    def extract(self, filename):

        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)
            return text

        except Exception as e:
            print(e)
            return "Error"



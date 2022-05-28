from pytesseract import pytesseract

class OCR:
    def __init__(self):
        self.path = '<tesseract-path>'

    def extract(self, filename):

        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)
            return text

        except Exception as e:
            print(e)
            return "Error"

if __name__ == '__main__':
        image_path = input("Enter the image path: ")
        img_text = OCR.extract(image_path)
        print("Your extracted text is:\n",img_text)
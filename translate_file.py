from translate import Translator
import tkinter as tk
from tkinter import filedialog
import io
from pdfminer.high_level import extract_text
from docx import Document

root = tk.Tk()
root.withdraw()
root.lift()
root.focus_force()


class Translate:
    def __init__(self):
        self.translate()
    
    def translate(self):
        path = filedialog.askopenfilename(parent=root)
        #with io.open(path,"r") as f:
        #    text = f.read()
        #f.close()
 
        text = extract_text(path)

        translator= Translator(from_lang= "english",to_lang='hi')
        translation = translator.translate(text)
        print(translation)
        
        #txtfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        #txtfile.write(translation)
        #txtfile.close()
        document = Document()
        document.add_paragraph(translation)
        document.save('text_files/translated_text.docx')
        
class test:
    a = Translate()
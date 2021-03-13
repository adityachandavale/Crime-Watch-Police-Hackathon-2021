from translate import Translator
import tkinter as tk
from tkinter import filedialog
import io

root = tk.Tk()
root.withdraw()
#root.deiconify()
root.lift()
root.focus_force()


class Translate:
    def __init__(self):
        self.translate()
    
    def translate(self):
        path = filedialog.askopenfilename(parent=root)
        with io.open(path,"r") as f:
            text = f.read()
        f.close()

        
        language = input("Language: ")

        translator= Translator(from_lang= "english",to_lang=language)
        translation = translator.translate(text)
        print(translation)
        
        txtfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        txtfile.write(translation)
        txtfile.close()
        
class test:
    a = Translate()
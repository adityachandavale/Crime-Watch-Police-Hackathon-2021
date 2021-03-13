from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import shutil
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
root.lift()
root.focus_force()


class Transcribe:
    def __init__(self):
        self.transcribe()
        
    def transcribe(self):
        r = sr.Recognizer()
        sound = AudioSegment.from_wav("output.wav")  

        chunks = split_on_silence(sound,min_silence_len = 5000,silence_thresh = sound.dBFS-14,keep_silence=5000)
        folder_name = "audio-chunks"

        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""

        for i, audio_chunk in enumerate(chunks, start=1):

            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")

            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)

                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print(str(e))
                except HTTPError as er:
                    print('Recognize function error')
                else:
                    text = f"{text.capitalize()}. "
                    whole_text += text
        txtfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        txtfile.write(whole_text)
        txtfile.close()
        shutil.rmtree(folder_name)

        
class test:
    a = Transcribe()
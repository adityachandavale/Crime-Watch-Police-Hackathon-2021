from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import shutil
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
import wave
import librosa
import soundfile as sf
from docx import Document
root = tk.Tk()
root.withdraw()
root.lift()
root.focus_force()


class Transcribe:
    def __init__(self):
        self.transcribe()
        
    def transcribe(self):
        r = sr.Recognizer()
        path = filedialog.askopenfilename(parent=root)
        sound = AudioSegment.from_wav(path)
        #x = librosa.load(path, sr=16000)
        #sf.write('tmp.wav', x, 16000)
        
        #with wave.open(path,mode='rb') as sound:

        chunks = split_on_silence(sound,min_silence_len = 500,silence_thresh = sound.dBFS-14,keep_silence=5000)
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
        #with open('text_files/transcribed_text.docx', 'w', encoding="utf-8") as f:
            #f.write(whole_text)
            #f.close()
        document = Document()
        document.add_paragraph(whole_text)
        document.save('text_files/transcribed_text.docx')
        shutil.rmtree(folder_name)

        
class test:
    a = Transcribe()
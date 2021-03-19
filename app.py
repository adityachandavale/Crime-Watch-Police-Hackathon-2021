from flask import Flask, render_template, request, jsonify, send_file
import base64
import os
import sys
from docx2pdf import convert

wdFormatPDF = 17

ENCODING_FORMAT = 'utf-8'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['GET', 'POST'])
def transcribe():
    return render_template('transcribe.html')

@app.route('/crimeWatch', methods=['GET', 'POST'])
def crimeWatch():
    return render_template('crimeWatch.html')

@app.route('/test')
def hello():
    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)

@app.route('/saveMessage', methods=['POST'])
def create_audio():
    audioContent = request.get_json(silent=True)  # this is a string
    audio = base64.b64decode(bytes(audioContent["message"], ENCODING_FORMAT))  # this is of type bytes
    currentCount = getCurrentCount()
    with open("audio_files/audioToSave_" + str(currentCount) + ".wav", "wb") as fh:
        fh.write(audio)
    status = 'done'
    return status

# Clearing browser cache on refresh
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/convert_to_text')
def convert_to_text():
    os.system('python transcribe.py')
    convert('text_files/transcribed_text.docx', 'text_files/transcribed_pdf.pdf')
    try:
	    return send_file('text_files/transcribed_pdf.pdf', attachment_filename='transcribed_pdf.pdf')
    except Exception as e:
        return str(e)

@app.route('/translate_text')
def translate_text():
    os.system('python translate_file.py')
    convert('text_files/translated_text.docx', 'text_files/translated_pdf.pdf')
    try:
	    return send_file('text_files/translated_pdf.pdf', attachment_filename='translated_pdf.pdf')
    except Exception as e:
        return str(e)

def getCurrentCount():
    count = 0
    with open("count.txt", "r+") as countFile:
        count = int(countFile.read())
        countFile.seek(0)
        countFile.write(str(count+1))
        countFile.truncate()
    return count

if __name__ == '__main__':
    app.run(debug=True)

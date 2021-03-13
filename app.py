from flask import Flask, render_template, request, jsonify
import base64

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
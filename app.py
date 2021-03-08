from flask import Flask, render_template, request, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
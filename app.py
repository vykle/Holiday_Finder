from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "TEsUK8PqA29HlbnR7csU3nbFLsOCMQCM"
URL = "https://calendarific.com/api/v2"

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/holidays')
@app.route('/holidays.html')
def index():
    return render_template('holidays.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/test')
@app.route('/test.html')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

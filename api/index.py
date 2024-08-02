from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello this is sunil thakur.'

@app.route('/about')
def about():
    return 'Hello this is sunil thakur.from agra uttar pradesh.'

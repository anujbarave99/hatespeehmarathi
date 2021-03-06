from flask import Flask, render_template, request
from googletrans import Translator
from textblob import TextBlob

app = Flask(__name__)


def detect(speech):
    prediction = TextBlob(speech).polarity
    if prediction < 0:
        output = ('Negative')
    else:
        output = ('Neutral')

    return output


def hate_speech_predictor(speech):
    prediction = detect(speech)
    return prediction


# Defining the site route


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        translater = Translator()
        message1 = translater.translate(message, dest="en")
        pred = hate_speech_predictor(message1.text)
        return render_template('index.html', prediction=pred, text=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

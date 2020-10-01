from flask import Flask, render_template, request

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import re
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')

pipeline = pickle.load(open('best_pipeline.pkl', 'rb'))
lemma = WordNetLemmatizer()

# Preprocessing the input message
def clean_message(msg):
    msg = re.sub('[^a-zA-Z]', ' ', msg)
    msg = msg.lower()
    msg = word_tokenize(msg)
    msg = [lemma.lemmatize(word) for word in msg if word not in stopwords.words('english')]
    msg = " ".join(msg)
    return msg
    
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['msg']
    # Preprocessing the input message
    msg = clean_message(msg)
    # Computing the probablity of your message being SPAM
    spam_proba = pipeline.predict_proba([msg])[0] 
    spam = pipeline.predict([msg])
    if spam == 1:
        return render_template('index.html', op_msg='The message has {}% chances of being spam.'.format(np.round(spam_proba[1], 2)*100))
    if spam == 0:
        return render_template('index.html', op_msg='The message you entered is not spam')

if __name__ == "__main__":
    app.debug = True
    app.run()
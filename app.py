import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('punkt')




from flask import Flask, render_template, url_for,redirect,send_file
from flask import request

from werkzeug.utils import secure_filename

def sentiment_analyses(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg>pos:
        return 'Negative Sentiment'
    elif pos > neg:
        return  'Positive Sentiment'
    else:
        return 'Neutral Sentiment'




app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret"
app.config['Secret_Key'] = '123'




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def uploads():
    Text_Data = request.form['taskid']
    if request.method =='POST':
        lower_case = Text_Data.lower() #lower case
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation)) #Remove Punctuation
        tokenized_words = word_tokenize(cleaned_text, "english")            #Tokenize Word
        Tw_woutStpwrds = []
        ex_words = []
        for word in tokenized_words:
            if word not in stopwords.words("english"):
                Tw_woutStpwrds.append(word)
            else:
                ex_words.append(word)
        score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
        neg = score['neg']
        pos = score['pos']
        neu = score['neu']
        compund_ = score['compound']
        if neg > pos:
            return f'It is a Negative Statement. Negative Score is {neg}.'
        elif pos > neg:
            return f'It is a Positive Statement. Positive Score is {pos}.'
        else:
            return f'It is a Neutral Statement. Neutral Score is {neu}.'
    else:
        return 'Please select Files!'


if __name__ == "__main__":
    app.run(debug=True)







import nltk
import nltk.data
from nltk.tokenize import word_tokenize

tokenizer = nltk.data.load('nltk_data/tokenizers/punkt/english.pickle')

from flask import Flask
from flask import request
from flask import render_template

application = app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("myform.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    
    lineas=tokenizer.tokenize(text)
    
    words = nltk.word_tokenize(text)
    
    week= words[7:11]

    linea1=lineas[8:10]+[', according to government data for the']+week
    
    linea2=lineas[4:6]

    linea3=lineas[10:11]+lineas[12:13]

    linea4=lineas[1:2]

    final=''.join("<p>%s<p> %s<p> %s<p> %s<p>" % (linea1, linea2, linea3, linea4)).replace('[',' ').replace(']',' ')
    
    final2= ", ".join( repr(e) for e in final ) 
    
    strfinal=str(final2).decode('unicode_escape').encode('ascii','ignore')
    
    front_page = render_template('myform.html', scroll='result')
    
    return  front_page+strfinal
    
if __name__ == '__main__':
    application.debug = True
    application.run()

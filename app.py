
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_trmplate, request,
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = "그래그래 나도나도 니도니도 코딩코딩 전부전부전부 코딩코딩 코딩 이다 이다"
    counter = dict=(Counter(user_string))
    result = json.dumpy(counter)
    return result


@app.get("/count/")
def count():
    result render_template('count')

@app.post("/result/")
def result():
    user_input = request.form['userinput']
    word_dict = dict(Count(user_input.split()))
    result =json.dumps(word_dict)
    return Response(result,
                    mimetype='application/json',
                    headers={
    'Content-disposition': 'attachment;filename=count,josn'})


# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = "그래그래 나도나도 니도니도 코딩코딩 전부전부전부 코딩코딩 코딩 이다 이다"
    counter = dict=(Counter(user_string0))
    result = json.dumpy(counter)

    return result



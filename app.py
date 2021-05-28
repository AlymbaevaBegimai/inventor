from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('goods.txt', 'r', encoding='utf8')
    txt = f.readlines()
    return render_template('index.html', goods=txt) 
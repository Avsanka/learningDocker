from random import random, randint

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('form.html')

@app.route('/num', methods=['GET'])
def giveNum():
    return str(randint(1, 100))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)

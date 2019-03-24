from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('username', 'Nobody')

    if name:
        greeting = f'hello, {name}'

    else:
        greeting = 'hello stranger'

    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run()

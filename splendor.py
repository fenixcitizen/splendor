from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def splendor(name = None):
    return render_template('splendor.html', name=name)

if __name__ == '__main__':
    app.run()

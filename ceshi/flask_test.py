from flask import Flask
import time

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    time.sleep(3)
    return name


if __name__ == '__main__':
    app.run(debug=True)

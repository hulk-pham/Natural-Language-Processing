from flask import Flask
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def name(name):
    return "Hello world {}".format(name)


if __name__ == '__main__':
    app.run()
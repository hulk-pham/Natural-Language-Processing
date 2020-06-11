from flask import Flask
from underthesea import sentiment
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def name(name):
    return "Hello world {}".format(name)


@app.route('/api/sentiment-analysis')
def sentiments():
    text = sentiment(
        'hàng kém chất lg,chăn đắp lên dính lông lá khắp người. thất vọng')
    print(text)
    print(sentiment(
        'Sản phẩm hơi nhỏ so với tưởng tượng nhưng chất lượng tốt, đóng gói cẩn thận.'))
    return "Check Log"


if __name__ == '__main__':
    app.run()

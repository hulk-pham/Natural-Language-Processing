from flask import Flask
from underthesea import sentiment
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from module.SentimentAnalysis import SentimentAnalysis
from module.NER import NER

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Welcome to NLP Server !"


api.add_resource(SentimentAnalysis, '/api/sentiment-analysis')
api.add_resource(NER, '/api/ner')


if __name__ == '__main__':
    app.run()

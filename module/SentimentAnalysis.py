from flask_restful import Resource, reqparse
from underthesea import sentiment
from langdetect import detect
from nltk.sentiment.vader import SentimentIntensityAnalyzer

parser = reqparse.RequestParser()
sid = SentimentIntensityAnalyzer()
# https://medium.com/@b.terryjack/nlp-pre-trained-sentiment-analysis-1eb52a9d742c


class SentimentAnalysis(Resource):
    def post(self):
        parser.add_argument('content', type=str)
        args = parser.parse_args()

        language = detect(args.content)
        if language == "vi":
            sentiment_result = sentiment(args.content)
        else:
            sentiment_course = sid.polarity_scores(args.content)
            sentiment_result = None

            if sentiment_course["pos"] > 0.5 or sentiment_course["neu"] > 0.5:
                sentiment_result = 'positive'
            else:
                sentiment_result = 'negative'

        return {
            'status': 200,
            'params': args,
            'result': {
                'label': sentiment_result,
                'language': language
            }
        }

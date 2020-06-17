import nltk
from flask_restful import Resource, reqparse
from underthesea import sentiment, pos_tag, ner
from langdetect import detect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag as nltk_pos_tag

parser = reqparse.RequestParser()
sid = SentimentIntensityAnalyzer()
# https://medium.com/@b.terryjack/nlp-pre-trained-sentiment-analysis-1eb52a9d742c

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)


def preprocess_vi(sent):
    entity = [chunk[0].lower()
              for chunk in ner(sent) if chunk[1].startswith('N')]
    result = list(set(entity))
    return result


def preprocess_non_vi(sent):

    tokenized = word_tokenize(sent)
    entity = [chunk[0].lower()
              for chunk in nltk_pos_tag(tokenized) if chunk[1].startswith('NN')]
    result = list(set(entity))
    return result


class NER(Resource):
    def post(self):
        parser.add_argument('content', type=str)
        args = parser.parse_args()

        language = detect(args.content)
        if language == "vi":
            sentiment_result = preprocess_vi(args.content)
        else:
            sentiment_result = preprocess_non_vi(args.content)

        return {
            'status': 200,
            'params': args,
            'result': {
                'label': sentiment_result,
                'language': language
            }
        }

from flask_restplus import Resource,Api,fields,abort
from flask import request
from . import bp
from app.utils import gen_word_dict,gen_words,word_check

api = Api(app=bp,doc='/docs',
            title='Letters to words',
                description='A converter of letters to words')


letterOption = {
    'letters': fields.String(required=True,description='letters to convert')
}

letterModel = api.model(name='letterModel',model=letterOption)
word_dict = gen_word_dict()


@api.route('/words')
class WordGen(Resource):

    @api.doc(responses={200:'ok',400:'Client-side error',500:'Server-side error'},
                params={'letters':'Specify letters'})
    @api.expect(letterModel,validation=True)
    def post(self):
        try:
            letters = request.json.get('letters')
            if not letters:
                return {
                    'status': 'not ok',
                    'message':'Fill in letters'
                    }

            words = gen_words(letters)
            wordsFormed = word_check(words,word_dict)
            if not wordsFormed:
                return {'message':'No words found'}

            return {
                'status': 'ok',
                'words': wordsFormed
                }

        except Exception:
            abort(400)

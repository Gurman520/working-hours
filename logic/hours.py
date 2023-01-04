from flask import jsonify, request
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.tables import Work


def add_hours(Resource):
    def post(self):
        session = db_session.create_session()
        new = News(
            title=request.json['title'],
            author=request.json['author'],
            text=request.json['text'],
        )
        session.add(new)
        session.commit()
        return jsonify({'success': 'OK'})


    #
    # new = session.query(Work).get(user_id)
    # return jsonify(
    #         [{'id': item.id, 'title': item.title, 'author': item.author,
    #           'author_name': session.query(User).get(item.author).name,
    #           'text': item.text, 'data': item.create_date} for item in new])
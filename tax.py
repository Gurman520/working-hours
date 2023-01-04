from datetime import datetime

from flask import jsonify, request
from flask_restful import Resource
from data import db_session
from data.tables import Tax, User

percent = {'ИП': 6, 'Физическое лицо': 4, "ГПХ": 13}


class Tax(Resource):

    def get(self):
        return jsonify({'success': 'OK'})

    def put(self):
        session = db_session.create_session()
        tax = session.query(Tax).get(request.json['userId'])
        if not tax:
            use = session.query(User).get(request.json['userId'])
            new = Tax(
                sum=float(request.json['hours']) * use,
                profit=request.json['desc'],
                tax=,
                userId=request.json['userId'],
                start_date=datetime.date(request.json['create_data'])
                finish_date=datetime.date(request.json['create_data'])
            )
            session.add(new)
            session.commit()
        else:





        return jsonify({'success': 'OK'})

    # def put(self):
    #     return jsonify({'success': 'OK'})

from datetime import datetime

from flask import jsonify, request
from flask_restful import Resource
from data import db_session
from data.tables import Work
# import logic.hours as H

percent = {'ИП': 6, 'Физическое лицо': 4, "ГПХ": 13}


class Hours(Resource):

    def get(self):
        # if H.add_hours() == 'OK':
        #     return jsonify({'success': 'OK'})
        return jsonify({'success': 'OK'})

    def post(self):
        session = db_session.create_session()
        p = request.json['where']
        per = percent[str(p[0])]
        new = Work(
            hours=request.json['hours'],
            description=request.json['desc'],
            percent=per,
            userId=request.json['userId'],
            create_date=datetime.strptime(request.json['create_data'], '%Y-%m-%d')
        )
        session.add(new)
        session.commit()

        return jsonify({'success': 'OK'})

    def put(self):
        return jsonify({'success': 'OK'})

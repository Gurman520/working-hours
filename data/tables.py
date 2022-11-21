import datetime
import sqlalchemy
from sqlalchemy import orm, Table, Column, ForeignKey
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class Tax(SqlAlchemyBase):
    __tablename__ = 'tax'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    userId = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('user.id'))
    sum = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    profit = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    tax = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    start_data = sqlalchemy.Column(sqlalchemy.DateTime)
    finish_data = sqlalchemy.Column(sqlalchemy.DateTime)
    user = orm.relation('User')


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    reportPeriod = sqlalchemy.Column(sqlalchemy.DateTime)
    salaryPeriod = sqlalchemy.Column(sqlalchemy.DateTime)
    period = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Work(SqlAlchemyBase):
    __tablename__ = 'work'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    userId = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('user.id'))
    hours = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    percent = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    user = orm.relation('User')
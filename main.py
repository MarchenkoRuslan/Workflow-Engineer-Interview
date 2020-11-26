from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import yaml
import json
import requests

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ToyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    status_updated = db.Column(db.Date, nullable=False)
    games = db.relationship('GameModel', backref='toy', lazy='dynamic')

    def __repr__(self):
        return f"Toy(name = {name}, status = {status}, status_updated = {status_updated}, games = {games})"


# class GameModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     note = db.Column(db.Text, nullable=True)
#     toy_id = db.Column(db.Integer, db.ForeignKey('toy.id'))


# db.create_all()


toy_put_args = reqparse.RequestParser()
toy_put_args.add_argument("name", type=str, help="Name of the toy is required", required=True)
toy_put_args.add_argument("status", type=str, help="Status of the toy", required=True)
toy_put_args.add_argument("status_updated", type=str, help="Last update of the toy status", required=True)
toy_put_args.add_argument("games", type=str, help="Games where toy has participate", required=True)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'status': fields.String,
    'status_updated': fields.DateTime,
    'games': fields.List

}


class Toys(Resource):
    @marshal_with(resource_fields)
    def get(self, toy_id):
        result = ToyModel.query.filter_by(id=toy_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, toy_id):
        args = toy_put_args.parse_args()
        result = ToyModel.query.filter_by(id=toy_id).first()
        if result:
            abort(409, message='Toy ID taken...')
        toy = ToyModel(id=toy_id,
                       name=args['name'],
                       status=args['status'],
                       status_updated=args['status_updated'],
                       games=args['games'])
        db.session.add(toy)
        db.session.commit()
        return toy, 201

    # def delete(self, toy_id):
    #     id_is_not_exist(toy_id)
    #     del toys[toy_id]
    #     return '', 204


# class Games(Resource):
#     def get(self):
#         return {
#             "id": "id",
#             "name": "name",
#             "date": "date",
#         }
#
#
# class Note(Resource):
#     def get(self):
#         return {
#             "id": "id",
#         }


api.add_resource(Toys, "/toys/<int:toy_id>")
# api.add_resource(Games, "/games")


if __name__ == "__main__":
    app.run(debug=True)

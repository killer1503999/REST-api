import sqlite3
from flask_restful import Resource, Api, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field can not be left blank"

    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field can not be left blank"

    )
    # parser goes through all the json text in the postman body

    def post(self):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        data = UserRegister.parser.parse_args()
      # data will be a dictionary
        if UserModel.find_by_username(data['username']) is None:

            #user = UserModel(data['username'], data['password'])
            user = UserModel(**data)
            user.save_to_db()

            return {'message': 'User created successfully'}, 201

        return {"message": "user already present in database"}, 404

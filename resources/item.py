from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

items = []


class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field can not be left blank"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every items needs a store id"
    )
    # parser helps us to control the information to be changes in the data base by using add_args

    @jwt_required()
    def get(self, name):
        # for item in items:
        #   if item["name"] == name:
        #      return item
        # item = next(filter(lambda x: x["name"] == name, items), None)
        # return {"message": "error"}, 404
        # return item, 200 if item else 401
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 201
        return {'message': "Item not found in database"}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return{"name": "An item already '{}' exit.".format(name)}, 400

        newItem = Items.parser.parse_args()
        print(newItem)
        print(122)
        item = ItemModel(name, newItem["price"], newItem["store_id"])
        # items.append(item)
        #print(2, item.json())
        try:
            item.save_to_db()
        except:
            # internal server error
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):

        # global items
        # items = list(filter(lambda x: x["name"] != name, items))
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()

        #query = "DELETE FROM items WHERE name = ? "
        #cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Items.parser.parse_args()
        # item = next(filter(lambda x: x["name"] != name, None))
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data["price"])
        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, data["price"], data["store_id"])

        item.save_to_db()
        return item.json()
        # items.append(item)


class Itemlist(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'name': row[1], 'price': row[2]})
        connection.close()

        # return {'items': items}
        return {'items': [item.json() for item in ItemModel.query.all()]}

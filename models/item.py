from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
#     stores.id=stores is table name and id is column name

# this will allow items table to see stores table
#       FOREIGN KEY
# The FOREIGN KEY constraint is a key used to link two tables together.

# A FOREIGN KEY is a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table.
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price, "store_id": self.store_id}

    @classmethod
    def find_by_name(cls, namee):
        # Select * from user where name = name Limit = 1 and return itemmodel object
        return cls.query.filter_by(name=namee).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

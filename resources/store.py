from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store Not Found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'Message':'A Store With Name {} Already Exists'.format(name)}, 400

        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'Message':' An error occured when trying to create store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db(name)

        return {'Message': 'Store Deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

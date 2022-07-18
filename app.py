
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from http import HTTPStatus


app = Flask(__name__)
api = Api(app)

items = [
    {
        'name': 'debashish',
        'age': 20
    },
        {
        'name': 'subashish',
        'age': 15
    },
            {
        'name': 'Suparna',
        'age': 16
    }
]
class Items(Resource):
    def get(self, *args, **kwargs):
        # data = next((item for item in items), None)
        return items
    
    def post(self, *args, **kwargs):
        data = request.get_json()
        print(data)
        items.append(data)
        return items, HTTPStatus.CREATED
    
    
class Item(Resource):
    def get(self, name, **kwargs):
        item = next((item for item in items if item['name'] == name), None)
        if item is None:
            return {"message": "no item found"}, HTTPStatus.NOT_FOUND
        return item
    
    def put(self, name, **kwargs):
        data = request.get_json()
        item = next((item for item in items if item['name'] == name), None)
        if item is None:
            return {"message": "no item found"}, HTTPStatus.NOT_FOUND
        item['name'] = data['name']
        item['age'] = data['age']
        return item, HTTPStatus.CREATED
        
                    
        
    def post(self, *args, **kwargs):
        pass
    
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<name>')


if __name__=='__main__':
    app.run(debug=True)
        
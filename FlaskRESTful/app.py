print("hello")
from flask import Flask,request
# from numpy import identity
# from FlaskRESTful.security import authenticate
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

app = Flask(__name__)
app.secret_key ='jose'
api = Api(app)

jwt = JWT(app,authenticate,identity)

class Student(Resource):
    def get(self,name):
        return {'student': name}
items=[]
class Item(Resource):
    # def get(self,name):
    #     for item in items:
    #         if item['name'] == name:
    #             return item ,404
    #     return {"item":None}


    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required =True,
        help="This field cannot be left blank!"
        )

    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']==name,items),None)

        return {"item":item},200 if item else 404
    def post(self,name):
        if next(filter(lambda x:x['name'] == name ,items),None):
            return {'message':"An item with name '{}' alredy exists".formate(name) },400
        data = Item.parser.parse_args()
        # data = request.get_json(silent=True)

        item ={'name':name,'price':12.00}
        items.append(item)
        return item ,201
    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name'] !=name,items))
        return {'message':'Item deleted'}

    def put(self,name):
        # data =request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x:x['name'] == name ,item),None)
        if item is None:
            item = {'name':name ,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
        
class ItemList(Resource):
    def get(self):
        return {'item':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Student,'/student/<string:name>')
app.run(debug=True,port=5000)
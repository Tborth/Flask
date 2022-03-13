from flask import Flask, jsonify,request,render_template

app = Flask(__name__)
import logging
logger = logging.getLogger('__name__')
stores=[{
    'name':'My Wonderful Store',
    'items':[
        {
            'name':'My Item',
            'price':15.99
        }
    ]
    }]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apps')
def apps():
    return render_template('app.html')
@app.route('/model')
def model():
    return render_template('model.html')
# @app.route('/')
# def hello_world():
#     return 'Hello world!'

@app.route('/store',methods=['POST'])
def create_store():
    app.logger.error('testing error log')
    request_data = request.get_json()
    app.logger.error(request_data)
    new_store ={
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store no data'})

    pass

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']== name:
            return jsonify(store['items'])

# POST /store/<string:name>/item {name:,price:}

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data =request.get_json()
    for store in stores:
        new_item ={
            'name': request_data['name'],
            'price':request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True,host="127.0.0.1",port=5000)

from flask import Flask, jsonify, request
from flask import make_response
from flask.ext.httpauth import HTTPBasicAuth
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://nitin:1234@ds119748.mlab.com:19748/wingify")
db = client.wingify
product = db.product

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'nitin':
        return 'nitin'
    if username == "vipin":
        return "vipin"
    if username == "sunil":
        return "sunil"
    if username == "amit":
        return "amit"
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



# get function to retrieve all products
@app.route('/wingify/api/v1.0/product/', methods=['GET'])
@auth.login_required
def get_product():

    output=[]
    for ins in product.find():
        output.append({"pid":ins["pid"],"name":ins["name"],"description":ins["description"],"supplier_name":ins["supplier_name"],"status":ins["status"],"price":ins["price"]})
    return jsonify({"result": output})


# get function to retrieve a specific product depending on pid
@app.route('/wingify/api/v1.0/product/<pid>', methods=['GET'])
@auth.login_required
def get_one_product(pid):
    item = product.find_one({"pid":pid})
    output=[]
    if item:
        output.append({"pid": item["pid"], "name": item["name"], "description": item["description"],"supplier_name": item["supplier_name"], "status": item["status"], "price": item["price"]})
    else:
        output = "No Result Found"
    return jsonify({"result":output})


# post function to add a product
@app.route('/wingify/api/v1.0/product/', methods=['POST'])
@auth.login_required
def post_product():
    try:
        pid = request.json['pid']
    except:
        pid = ""

    if pid == "":
        output = "Kindly mention pid"
        return jsonify({"result":output})

    if product.find_one({"pid":request.json['pid']}):
        output = "product with pid " + request.json['pid'] + " already exist. Kindly update it."

        return jsonify({"result":output})

    try:
        pid = request.json['pid']
    except:
        pid = ""

    if pid == "":
        output = "Kindly enter pid"
        return jsonify({"result":output})

    try:
        name = request.json['name']
    except:
        name = ""

    try:
        description = request.json['description']
    except:
        description = ""

    try:
        supplier_name = request.json['supplier_name']
    except:
        supplier_name = ""

    try:
        status = request.json['status']
    except:
        status = ""


    try:
        price = request.json['price']
    except:
        price = ""

   
    product_id = product.insert({"pid": pid, "name": name, "description": description,"supplier_name": supplier_name, "status": status, "price": price})
    new_product = product.find_one({"_id": product_id})


    output=[]
    output.append({"pid": new_product["pid"], "name": new_product["name"], "description": new_product["description"],"supplier_name": new_product["supplier_name"], "status": new_product["status"],"price": new_product["price"]})

    return jsonify({"result":output,"status":"Successfully added the product"})

# post function to update a specific product depending on pid
@app.route('/wingify/api/v1.0/product/<pid>', methods=['POST'])
@auth.login_required
def update_product(pid):

    check = product.find_one({"pid":pid})

    if not check :

        output = "No product find with pid " + pid
        return jsonify({"result":output})


    else:
        try:
            pid1 = request.json['pid']
        except:
            pid1 = check["pid"]

        try:
            name = request.json['name']
        except:
            name = check["name"]

        try:
            description = request.json['description']
        except:
            description = check["description"]
        try:
            supplier_name = request.json['supplier_name']
        except:
            supplier_name = check["supplier_name"]

        try:
            status = request.json['status']
        except:
            status = check["status"]


        try:
            price = request.json['price']
        except:
            price = check["price"]

        product.update({"pid":pid},{"pid": pid1, "name": name, "description": description,"supplier_name": supplier_name, "status": status, "price": price })
        new_product = product.find_one({"pid": pid1})
        output=[]
        output.append({"pid": new_product["pid"], "name": new_product["name"], "description": new_product["description"],"supplier_name": new_product["supplier_name"], "status": new_product["status"],"price": new_product["price"]})

    return jsonify({"result":output,"status":"Successfully updated product"})


@app.route('/wingify/api/v1.0/product/<pid>', methods=['DELETE'])
@auth.login_required
def delete_product(pid):
    item = product.find_one({"pid":pid})
    if item :
        product.remove({"pid":pid})
        output = "successfully deleted product with pid " + pid
    else:
        output = "product not found"
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
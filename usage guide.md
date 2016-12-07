## Usage Guide

This api has five main functions :

 - to display all the product from database
 - to display a single product of given pid
 - to add a product to the database
 - to update a product of given pid
 - to delete a product of given pid
 
###API Authentication

User has to authenticate once before using the API in each session.
Following are the username and password:

> - username: nitin, password: nitin
> - username: vipin, password: vipin
> - username: sunil, password: sunil
> - username: amit, password: amit 

###Display all the product from database

 - **URL** : http://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/
 - **Method** :  GET
 - **Body** : not needed
 - **Response** : 

> {
  "result": [
    {
      "description": "HP 8 GB RAM", 
      "name": "Laptop", 
      "pid": "P1001", 
      "price": "Rs 40000", 
      "status": "active", 
      "supplier_name": "Vipin"
    }, 
    {
      "description": "LG LCD", 
      "name": "Monitor", 
      "pid": "P1002", 
      "price": "Rs 4000", 
      "status": "inactive", 
      "supplier_name": "Amit"
    }, 
    {
      "description": "LG Wireless", 
      "name": "Mouse", 
      "pid": "P1003", 
      "price": "Rs 200", 
      "status": "active", 
      "supplier_name": "Aman"
    }, 
    {
      "description": "32 GB", 
      "name": "Pendrive", 
      "pid": "P1000", 
      "price": "Rs 200", 
      "status": "active", 
      "supplier_name": "Nitin"
    }
  ]
}

 


###Display a single product of given pid

 - **URL** : https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/P1000
 - **Method** :  GET
 - **Body** : not needed
 - **Response** : 

> {
  "result": [
    {
      "description": "32 GB", 
      "name": "Pendrive", 
      "pid": "P1000", 
      "price": "Rs 200", 
      "status": "active", 
      "supplier_name": "Nitin"
    }
  ]
}


### Add a product to the database

 - **URL** : https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/
 - **Method** :  POST
 - **Content-type** : application/json
 - **Body** : `{"pid":"P1008","name":"PD","description":"8 GB","supplier_name":"Ronak","status":"active","price":"Rs 100"}`
 - **Response** : 

> {
  "result": [
    {
      "description": "8 GB",
      "name": "PD",
      "pid": "P1008",
      "price": "Rs 100",
      "status": "active",
      "supplier_name": "Ronak"
    }
  ],
  "status": "Successfully added the product"
}

### Update a product of given pid

 - **URL** : https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/P1008
 - **Method** :  POST
 - **Content-type** : application/json
 - **Body** : `{"pid":"P1008","name":"upPD","description":"8 GB","supplier_name":"Ravi","status":"active","price":"Rs 100"}`
 - **Response** : 

> {
  "result": [
    {
      "description": "8 GB",
      "name": "upPD",
      "pid": "P1008",
      "price": "Rs 100",
      "status": "active",
      "supplier_name": "Ravi"
    }
  ],
  "status": "Successfully updated product"
}

### Delete a product of given pid

 - **URL** : https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/P1008
 - **Method** :  DELETE
 - **Body** : not needed
 - **Response** : 

> {
  "result": "successfully deleted product with pid P1008"
}

 
 

## Testing the API


To test the live API

- Run the Python file `test_live_api.py` using command `python test_live_api.py`

To test the API on local server (set to localhost:5000)

 - Run the Python file `test_local_api.py` using command `python test_local_api.py`



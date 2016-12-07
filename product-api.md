PRODUCT API
===================


### Objective

To design a RESTful API for an online store which can be used to manage different products

##Overview

This API is built using Flask a python framework.It is used for searching , adding, deleting and updating product. It has only one endpoint `/product` 



## Schema

Product Table

 - **pid** : unique id of produxt
 - **name** : name of product
 - **description** : description of product
 - **supplier_name** : name of supplier
 - **status** : product is active or inactive
 - **price** : price of product

##API Authentication

User has to authenticate once before using the API in each session.
Following are the username and password:

> - username: nitin, password: nitin
> - username: vipin, password: vipin
> - username: sunil, password: sunil
> - username: amit, password: amit


##Routes Configuration

 

 1. 
> **URL**: /wingify/api/v1.0/product/
> **Method**: GET
> **Description**: return all the products
 
 2. 
> **URL**: /wingify/api/v1.0/product/<pid>
>  **Method**: GET
> **Description**: return product of given pid

 3. 
> **URL**: /wingify/api/v1.0/product/
> **Method**: POST
> **Description**: add a product to database

 4. 
> **URL**: /wingify/api/v1.0/product/<pid>
> **Method**: POST
> **Description**: update a product of given pid

 5. 
> **URL**: /wingify/api/v1.0/product/<pid>
> **Method**: DELETE
> **Description**: delete product of given pid



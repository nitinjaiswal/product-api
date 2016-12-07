# Code Setup Guide

This api is already on heroku at [https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/](https://vast-everglades-95203.herokuapp.com/wingify/api/v1.0/product/).
But still this is code setup guide.

## System Dependencies
- Pyhton 3.4

## Clone repo

Clone the repo `product-api` from [https://github.com/nitinjaiswal/product-api](https://github.com/nitinjaiswal/product-api)

The directory `product-api` have three main files.

- **app.py**: This is the main file for the api.
- **test_live_api.py**: This file is used to test the live api.
- **test_local_api.py**: This file is for testing api on localhost (5000).
- **requirements.txt**: This file contains requirements required by the app.py and test.py


### Directory Structure
```
    -|/product-api/
           -|/app.py
           -|/test_live_api.py
           -|/test_local_api.py
           -|/requirements.txt
   
```
## Create virtual enviroment

 - Install `virtualenv` using command `pip install virtualenv`
 - Open terminal in `product-api` directory
 - Create virtualenv using command `virtualenv flask`
 - Activate virtualenv using command `.\flask\Scripts\activate`
 

## Installation of 3rd Party Libraries
- Open terminal in `product-api`
- Activate virtualenv using command `.\flask\Scripts\activate`
- Change directory to `flask` using command `cd flask`
- Install requirements using command `pip install -r requirements.txt`

## Running API
- Open terminal in `product-api`
- Activate virtualenv using command `.\flask\Scripts\activate`
- To run the API, run command `python app.py`
- Now the API is live on `localhost:<port>`
- Now go to `https://localhost:<port>/wingify/api/v1.0/product/` to use API

## Testing API
 
 To test the live api
 - Run python file `test_live_api.py` using command `python test_live_api.py`

To test the api on loaclhost (llocalhost:5000)
 - Run python file `test_local_api.py` using command `python test_local_api.py`


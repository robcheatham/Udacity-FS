from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Product

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///productcatalogue.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


navitems = session.query(Category).order_by(asc(Category.name))

# Show all the categories
@app.route('/')
@app.route('/category/')
def showCategories():
    products = session.query(Product).all()
    return render_template('categories.html', navitems=navitems, products=products)


@app.route('/category/<string:url_name>/')
@app.route('/category/<string:url_name>/products/')
def showCategoryProducts(url_name):
	category = session.query(Category).filter_by(url_name=url_name).one()
	products = session.query(Product).filter_by(category_url=url_name).all()
	return render_template('public-categoryproducts.html', navitems=navitems, category=category, products=products)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

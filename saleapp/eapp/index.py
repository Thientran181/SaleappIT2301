import math

from flask import Flask, render_template, request
from unicodedata import category
from eapp import dao, app

@app.route("/")
def index():
    kw = request.args.get('kw')
    page = request.args.get('page', 1, type=int)

    pase_size = app.config["PAGE_SIZE"]
    return render_template('index.html', products=dao.load_products(kw=kw, page=page),
                           pages= math.ceil(dao.count_products()/pase_size))


@app.route("/register")
def register():

    return render_template('register.html')

@app.route("/login")
def login():

    return render_template('login.html')

@app.context_processor
def common_responses():
    categories = dao.load_categories()

    return {
        'categories': categories
    }

if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)

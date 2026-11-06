from flask_admin.contrib.sqla import ModelView

from eapp.models import *
from flask_admin import Admin
from eapp import app

admin = Admin(app=app, name="E-commerce's Admin")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))

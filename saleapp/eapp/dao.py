from eapp.models import Category

def load_categories():
    return Category.query.order_by('id').all()
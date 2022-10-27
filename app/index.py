from flask import render_template, request
from app import app, dao


@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products(category_id=request.args.get('category_id'),
                                 kw=request.args.get('keyword'))
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, request, redirect, session, jsonify
from app import app, dao, utils
from flask_login import login_user, logout_user
from app.decorator import annonynous_user
import cloudinary.uploader


def index():
    products = dao.load_products(category_id=request.args.get('category_id'),
                                 kw=request.args.get('keyword'))
    return render_template('index.html', products=products)


def details(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)


def login_admin():
    username = request.form['username']
    password = request.form['password']
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')


@annonynous_user
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            n = request.args.get('next')
            return redirect(n if n else '/')
    return render_template('login.html')


def user_logout():
    logout_user()
    return redirect('/login')


def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            avatar = ''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                print(res)
                avatar = res['secure_url']
            try:
                dao.register(name=request.form['name'],
                             password=password,
                             username=request.form['username'], avatar=avatar)
                return redirect('/login')
            except:
                err_msg = 'Lỗi! Hãy quay lại sau.'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'
    return render_template('register.html', err_msg=err_msg)


def cart():
    return render_template('cart.html')


def add_2_cart():
    data = request.json
    key = app.config['CART_KEY']
    cart = session[key] if key in session else {}
    id = str(data['id'])
    name = data('name')
    price = data['price']
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] =  {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }
        session[key] = cart
    return jsonify(utils.cart_stats(cart))


def update_cart(product_id):
    key = app.config['CART_KEY']
    cart = session.get(key)
    if cart and product_id in cart:
        cart[product_id]['quantity'] = int(request.json['quantity'])
    session[key] = cart
    return jsonify(utils.cart_stats(cart))


def del_cart(product_id):
    key = app.config['CART_KEY']
    cart = session.get(key)
    if cart and product_id in cart:
        del cart[product_id]
    session[key] = cart
    return jsonify(utils.cart_stats(cart))


def pay():
    key = app.config['CART_KEY']
    cart = session.get(key)
    if dao.add_receipt(cart=cart):
        del session[key]
    else:
        return jsonify({'status': 500})
    return jsonify({'status': 200})


def load_user(user_id):
    return dao.get_user_by_id(user_id)


def common_attr():
    categories = dao.load_categories()
    return {
        'categories': categories,
        'cart': utils.cart_stats(session.get(app.config['CART_KEY']))
    }


if __name__ == '__main__':
    app.run(debug=True)

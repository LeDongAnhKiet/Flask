from flask import session
from app import app, dao, admin, login, utils, ctrler

app.add_url_rule('/', 'index', ctrler.index)
app.add_url_rule('/products/<int:product_id>', 'product-detail', ctrler.details)
app.add_url_rule('/login-admin', 'login-admin', ctrler.login_admin, methods=['post'])
app.add_url_rule('/login', 'login-user', ctrler.user_login, methods=['get', 'post'])
app.add_url_rule('/logout', 'logout', ctrler.user_logout)
app.add_url_rule('/register', 'register', ctrler.register, methods=['get', 'post'])
app.add_url_rule('/cart', 'cart', ctrler.cart)
app.add_url_rule('/api/cart', 'add-cart', ctrler.add_2_cart, methods=['post'])
app.add_url_rule('/api/cart/<product_id>', 'update-cart', ctrler.update_cart, methods=['put'])
app.add_url_rule('/api/cart/<product_id>', 'delete-cart', ctrler.del_cart, methods=['delete'])
app.add_url_rule('/api/pay', 'pay', ctrler.pay)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.context_processor
def common_attr():
    categories = dao.load_categories()
    return {
        'categories': categories,
        'cart': utils.cart_stats(session.get(app.config['CART_KEY']))
    }


if __name__ == '__main__':
    app.run(debug=True)

from app import db


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(200))
    product = db.relationship('Product', backref='category')


class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(200))
    user = db.relationship('User', backref='Role', uselist=False)


class CartProduct(db.Model):
    cp_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    user_role = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    cart = db.relationship('Cart', backref='user', uselist=False)
    product = db.relationship('Product', backref='user')


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    cartproduct = db.relationship('CartProduct', backref='cart')


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    cartproduct = db.relationship('CartProduct', backref='Product')


db.create_all()

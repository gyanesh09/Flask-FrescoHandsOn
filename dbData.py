from unicodedata import category
from app import db
import models

cat1 = models.Category(category_name="Fashion")
cat2 = models.Category(category_name="Electronics")
cat3 = models.Category(category_name="Books")
cat4 = models.Category(category_name="Groceries")
cat5 = models.Category(category_name="Medicines")

db.session.add_all([cat1, cat2, cat3, cat4, cat5])
db.session.commit()


role1 = models.Role(role_name="CONSUMER")
role2 = models.Role(role_name="SELLER")

db.session.add_all([role1, role2])
db.session.commit()

cons_role = models.Role.query.filter_by(role_id=1).first()
sell_role = models.Role.query.filter_by(role_id=2).first()

user1 = models.User(user_name="jack", password="pass_word",
                    user_role=cons_role.role_id)
user2 = models.User(user_name="bob", password="pass_word",
                    user_role=cons_role.role_id)
user3 = models.User(user_name="apple",
                    password="pass_word", user_role=sell_role.role_id)
user4 = models.User(user_name="glaxo",
                    password="pass_word", user_role=sell_role.role_id)

db.session.add_all([user1, user2, user3, user4])
db.session.commit()

user1 = models.User.query.filter_by(user_id=1).first()
user2 = models.User.query.filter_by(user_id=2).first()
cart1 = models.Cart(total_amount=20, user_id=user1.user_id)
cart2 = models.Cart(total_amount=0, user_id=user2.user_id)

db.session.add_all([cart1, cart2])
db.session.commit()

prod1 = models.Product(price=29190, product_name="ipad",
                       category_id=2, seller_id=3)
prod2 = models.Product(price=10, product_name="crocin",
                       category_id=5, seller_id=4)
db.session.add_all([prod1, prod2])
db.session.commit()

cartprod1 = models.CartProduct(cart_id=1, product_id=2, quantity=2)
db.session.add_all([cartprod1])
db.session.commit()

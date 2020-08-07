from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

#START:declaring class models#
class User(db.Model):
    id = Column(Integer, primary_key = True)
    user_name = Column(String(15), nullable = False)
    email = Column(String(15), nullable = False)
    password_hash = Column(db.String(10), nullable = False)

    @property
    def password(self):
        raise Exception("password can't be read by anybody")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

User_Roles = db.Table("User_Roles",
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("rol_id", Integer, ForeignKey("rol.id"))
)

class Rol(db.Model):
    id = Column(Integer, primary_key = True)
    rol = Column(String(20), nullable = False)

class Order(db.Model):
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    user = db.relationship("user", backref = "order")
    product = db.relationship("product", backref = "order")
    description = Column(db.String(20))
    requested_items = Column(Integer, nullable = False)

class product(db.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    items = Column(Integer, nullable = False)


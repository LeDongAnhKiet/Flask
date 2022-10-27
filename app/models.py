from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(Base):
    __tablename__ = "category"
    name = Column(String(50), nullable = False)
    products = relationship('Product', backref = 'category', lazy=True)

    def __str__(self):
        return self.name

class Product(Base):
    __tablename__ = "product"
    name = Column(String(50), nullable=False)
    description = Column(Text)
    image = Column(String(100))
    active = Column(Boolean, default = True)
    price = Column(Float, default = 0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Điện Thoại')
        # c2 = Category(name='Laptop')
        # c3 = Category(name='Tai nghe')
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        p1 = Product(name='iPhone 13', description='Apple, 128GB', price = 22000000,
                     image='', category_id=1)
        p2 = Product(name='iPhone 13 Pro', description='Apple, 128GB', price=28000000,
                     image='', category_id=1)
        p3 = Product(name='Galaxy J7', description='Samsung, 128GB', price=22000000,
                     image='', category_id=1)
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        # db.create_all()

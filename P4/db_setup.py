from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Create the User Class for the db
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    avatar = Column(String(250))


# Create the Category Class for the db
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    # Establish relationship to User
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


# Create the Product Class for the db
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    short_desc = Column(String(250), nullable = False)
    price = Column(String(8), nullable = False)
    # Establish relationship to User
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    # Establish relationship to Category
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


engine = create_engine('sqlite:///productcatalogue.db')

Base.metadata.create_all(engine)
print "Product Catalogue db schema established!"

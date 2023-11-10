from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship("Product", back_populates="seller")
    shop_address = relationship("ShopAddress", back_populates="seller")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    # price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    image = Column(String, nullable=False) #File Path or URL
    seller_id = Column(Integer, ForeignKey('sellers.id'), nullable=False)
    seller = relationship("Seller", back_populates="products")
    
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    customer_address = relationship("CustomerAddress", back_populates="customers")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    region = Column(String, nullable=False)
    customer_address = relationship("CustomerAddress")
    shop_address = relationship("ShopAddress")

class CustomerAddress(Base):
    __tablename__ = 'customer_address'
    customer_id = Column(Integer, ForeignKey('customers.id'), primary_key=True)
    address_id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    customer = relationship("Customer", back_populates="customer_address")
    address = relationship("Address", back_populates="customer_address")
class ShopAddress(Base):
    __tablename__ = 'shop_address'
    seller_id = Column(Integer, ForeignKey('sellers.id'), primary_key=True)
    address_id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    seller = relationship("Seller", back_populates="shop_address")
    address = relationship("Address", back_populates="shop_address")



    

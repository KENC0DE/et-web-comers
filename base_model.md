# Overview

This project utilizes SQLAlchemy database model for managing sellers, products, customers, and addresses. The model is designed to represent the relationships between these entities, allowing for efficient data retrieval and updates.

# Setup

## Python 3

## SQLAlchemy

# Installation

1. Clone Repo
2. Install: pip install SQLAlchemy

# Code Description

1. from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey


    ## Importing specific classes necessary or defining the structure of the database tables and estableshing relationship between them.

2. from sqlalchemy.orm import sessionmaker, relationship


    ## Imports the sessionmaker(try searching on gpt) and relationship classes. The sessionmaker is used for creating database sessions, and the relationship class is for connecting the relations between the model classes defined in the code.

3. from sqlalchemy.ext.declarative import declarative_base


    ## imports declarative_base function. It is used to create a base class that serves as the foundation for all the model classes.

4. Base = declarative_base()


    ## creates base class called Base; it should be inherited by all the model classes we define later.

5. class Seller(Base):


    ## define new class called Seller, to represent the seller. The Base class is specified as the parent class.

6. **tablename** = 'sellers'


    ## sets the table name for the seller class to 'sellers'. the table name is used when creating the corresponding table in the db.

7. id = Column(Integer, primary_key=True)


    ## defines a column called id in the Seller table, it serves as primary key for the table

8. name = Column(String, nullable=False)


    ## This line defines a column called name in the Seller table. It is of type String and is not allowed to be NULL.

9. products = relationship("Product", back_populates="seller")


    ## This line establishes a relationship between the Seller and Product tables. It creates a bidirectional relationship where each Seller can have multiple Product instances, and each Product instance belongs to a single Seller. The back_populates argument specifies the corresponding attribute in the Product class.

10. shop_address = relationship("ShopAddress back_populates="seller")


    ## This line establishes a relationship between the Seller and ShopAddress tables. It creates a bidirectional relationship where each Seller can have multiple ShopAddress instances, and each ShopAddress instance belongs to a single Seller. The back_populates argument specifies the corresponding attribute in the ShopAddress class.

    ##### The following line of code follow a similar pattern, so try to understand it using the above explanation.

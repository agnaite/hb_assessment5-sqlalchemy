from collections import defaultdict
from pprint import pprint

"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter_by(founded=1903, discontinued=None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').first()


# Fill in the following functions. (See directions for more info.)
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # get all models with the year that was passed in as argument
    all_models = Model.query.filter_by(year=year).all()

    # for each model object print the name, brand, and headquarters
    for model in all_models:
        print 'model: {}, brand: {}, headquarters: {}'.format(model.name, 
                                                             model.brand_name, 
                                                             model.brands.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # get all brands from database in a list object
    all_brands = Brand.query.all()
    # initialize empty dictionary with an empty list as default value
    brands_models = defaultdict(list)

    # for each brand object in list, add the brand name as key and
    # the list of model names as the value to the brand_models dictionary
    for brand in all_brands:
        brands_models[brand.name]
        for model in brand.models:
            brands_models[brand.name].append(model.name)

    # use pretty print to print the final dictionary as dict, as
    # pprint does not support defaultdicts
    pprint(dict(brands_models))

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The returned value is a list with one brand object and the type is 'flask_sqlalchemy.BaseQuery'.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that is used for many-to-many relationships, when the
# table holding the foreign key does not have any meaningful columns of its own. Its sole pupose
# is to bind two other tables together.

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    return Brand.query.filter((Brand.name.like('%' + mystr + '%')) | (Brand.name == mystr)).all()


def get_models_between(start_year, end_year):
    return Model.query.filter(Model.year > start_year, Model.year < end_year).all()

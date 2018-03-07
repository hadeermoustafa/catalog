from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
Root = User(name="Hadeer Moustafa", email="hadeer.moustafa@outlook.com")
session.add(Root)
session.commit()

# Create first category
category1 = Category(user_id=1, name="Cloths")

session.add(category1)
session.commit()

categoryItem = CategoryItem(user_id=1, name="T-shirts",
                            description="A comfy piece of cloth",
                            category=category1)

session.add(categoryItem)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Scarfs",
                             description="Something to be traped"
                             "around the neck",
                             category=category1)

session.add(categoryItem1)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Skirt",
                             description="Comes in diffrent length,"
                             "could be mini or maxi",
                             category=category1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Dresses",
                             description="Gorgous outfit for ladies,"
                             "great for evening and summer time",
                             category=category1)

session.add(categoryItem4)
session.commit()

 #Create second category
category2 = Category(user_id=1, name="foot wear")

session.add(category2)
session.commit()

categoryItem = CategoryItem(user_id=1, name="Boots",
                            description="a unisex piece, good for winter",
                            category=category2)

session.add(categoryItem)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="sandals",
                             description="a very stilish piece for summer",
                             category=category2)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="flip flops",
                             description="The most comfi one",
                             category=category2)

session.add(categoryItem2)
session.commit()

print "Categories Have been added in the catalog"

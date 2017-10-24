from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

# Import the necessary db Classes
from db_setup import Base, User, Category, Product

# Create the engine and bind it to the Base class metadata
# so that declaratives can be accessed through the session instance
engine = create_engine('sqlite:///productcatalogue.db')
Base.metadata.bind(engine)

# Create a session as a STG area for db objects
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create Users in the db
# User 1
user1 = User(name="Robert Cheatham", email="robcheatham99@gmail.com",
             avatar="https://goo.gl/PSniGn")
session.add(user1)
session.commit()

# User 2
user2 = User(name="Rob Cheatham", email="rob.cheatham.uk@gmail.com",
             avatar="https://goo.gl/5agCyJ")
session.add(user2)
session.commit()

# User 3
user3 = User(name="Decipher Bot", email="rob@wearedecipher.com",
             avatar="https://goo.gl/tgzsKL")
session.add(user3)
session.commit()

print("Users added successfully to the database!")


# Create Outerwear Category with Products
# Outerwear Category Creation
category1 = Category(user_id=1, name="Outerwear")

session.add(category1)
session.commit()

# Outerwear Product Creation
product1 = Product(user_id=1, name="Long Sleeve ZipUp",
                   short_desc="Lightweight layer for chilly trail runs",
                   price="$60.00", category=category1)

session.add(product1)
session.commit()

product2 = Product(user_id=2, name="TriClimate Jacket",
                   short_desc="All-weather protection all year round",
                   price="$199.99", category=category1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Active Hoodie",
                   short_desc="Style and warmth without the weight",
                   price="$89.00", category=category1)

session.add(product3)
session.commit()

product4 = Product(user_id=3, name="Breathable Pullover",
                   short_desc="Improved style, same technical protection",
                   price="$55.00", category=category1)

session.add(product4)
session.commit()

product5 = Product(user_id=1, name="Dock Worker Beanie",
                   short_desc="Warmth and style all in one",
                   price="$19.99", category=category1)

session.add(product5)
session.commit()

print("Outerwear Category & Products added succesfully to the database!")


# Create T-Shirts Category with Products
# T-Shirts Category Creation
category2 = Category(user_id=2, name="T-Shirts")

session.add(category2)
session.commit()

# T-Shirt Product Creation
product6 = Product(user_id=2, name="Explore Tee",
                   short_desc="Go out and see the world in style",
                   price="$24.99", category=category2)

session.add(product6)
session.commit()

product7 = Product(user_id=3, name="Flex Tee",
                   short_desc="Essential support for outdoor training",
                   price="$19.99", category=category2)

session.add(product7)
session.commit()

product8 = Product(user_id=1, name="Long Sleeve Shirt",
                   short_desc="Easy on the eye and the skin",
                   price="$30.00", category=category2)

session.add(product8)
session.commit()

product9 = Product(user_id=2, name="Raglan Tee",
                   short_desc="A warm layer for cold adventures",
                   price="$29.99", category=category2)

session.add(product9)
session.commit()

product10 = Product(user_id=3, name="Kilowatt T-Shirt",
                    short_desc="Maximum mobility and breathability",
                    price="$24.99", category=category2)

session.add(product10)
session.commit()

print("T-Shirt Category & Products added succesfully to the database!")


# Create Active Wear Category with Products
# Active Wear Category Creation
category3 = Category(user_id=3, name="Active Wear")

session.add(category3)
session.commit()

# Active Wear Product Creation
product11 = Product(user_id=1, name="Reversible Yoga Leggings",
                    short_desc="Get down in these edgy print leggings",
                    price="$70.00", category=category3)

session.add(product11)
session.commit()

product12 = Product(user_id=3, name="Cross Train Hoody",
                    short_desc="Level up your winter workouts",
                    price="$49.99", category=category3)

session.add(product12)
session.commit()

product13 = Product(user_id=2, name="Reflect Seamless Top",
                    short_desc="Sweat Wicking and Quick Drying Fabric",
                    price="$35.00", category=category3)

session.add(product13)
session.commit()

product14 = Product(user_id=2, name="Luxe Arctic Pants",
                    short_desc="Relaxed fit with quilted panels",
                    price="$39.99", category=category3)

session.add(product14)
session.commit()

product15 = Product(user_id=3, name="Luxe Gym Bag",
                    short_desc="The ultimate Gym Bad that you need",
                    price="$50.00", category=category3)

session.add(product15)
session.commit()

print("Active Wear Category & Products added succesfully to the database!")


# Create Hiking Gear Category with Products
# Hiking Gear Category Creation
category4 = Category(user_id=1, name="Hiking Gear")

session.add(category4)
session.commit()

# Hiking Gear Product Creation
product16 = Product(user_id=1, name="Hedgehog Gore-Tex Boots",
                    short_desc="Reassuring support for every terrain",
                    price="$99.99", category=category4)

session.add(product16)
session.commit()

product17 = Product(user_id=3, name="Banchee 50 Backpack",
                    short_desc="Versatile storage for a range of adventures",
                    price="$89.00", category=category4)

session.add(product17)
session.commit()

product18 = Product(user_id=2, name="Mountain Light Jacket",
                    short_desc="Three levels of hiking protection in one",
                    price="$119.99", category=category4)

session.add(product18)
session.commit()

product19 = Product(user_id=1, name="Apex Flex Shell Jacket",
                    short_desc="Lock out the wet and the wind",
                    price="$139.99", category=category4)

session.add(product19)
session.commit()

product20 = Product(user_id=2, name="Thermoball Gilet",
                    short_desc="Core warmth even in the wet",
                    price="$50.00", category=category4)

session.add(product20)
session.commit()

print("Hiking Gear Category & Products added succesfully to the database!")


# Create Snow Range Category with Products
# Snow Range Category Creation
category5 = Category(user_id=2, name="Snow Range")

session.add(category5)
session.commit()

# Snow Range Product Creation
product21 = Product(user_id=3, name="Lostrail Jacket",
                    short_desc="Sleek style, big alpine protection",
                    price="$279.00", category=category5)

session.add(product21)
session.commit()

product22 = Product(user_id=2, name="Repko Jacket",
                    short_desc="Go freestyle on the slopes",
                    price="$189.00", category=category5)

session.add(product22)
session.commit()

product23 = Product(user_id=1, name="Anonym Jacket",
                    short_desc="Slim fit, lofty insulation",
                    price="$299.99", category=category5)

session.add(product23)
session.commit()

product24 = Product(user_id=3, name="Leather Solo Glove",
                    short_desc="Maximum Warmth, Maximum Style",
                    price="$39.99", category=category5)

session.add(product24)
session.commit()

product25 = Product(user_id=2, name="Underhelmet Balaclava",
                    short_desc="Supreme warmth and moisture management",
                    price="$30.00", category=category5)

session.add(product25)
session.commit()

print("Snow Range Category & Products added succesfully to the database!")


# Create Running Category with Products
# Running Category Creation
category6 = Category(user_id=3, name="Running")

session.add(category6)
session.commit()

# Running Product Creation
product26 = Product(user_id=1, name="Rapido Jacket",
                    short_desc="Perfect for unpredicatble weather",
                    price="$69.99", category=category6)

session.add(product26)
session.commit()

product27 = Product(user_id=2, name="Dual Shorts",
                    short_desc="Versatile support for your run",
                    price="$45.00", category=category6)

session.add(product27)
session.commit()

product28 = Product(user_id=3, name="Better than Naked Shorts",
                    short_desc="Lightweight breathability for long sessions",
                    price="$54.99", category=category6)

session.add(product28)
session.commit()

product29 = Product(user_id=1, name="Runners eTip Gloves",
                    short_desc="Stay warm, dry and connected",
                    price="$19.99", category=category6)

session.add(product29)
session.commit()

product30 = Product(user_id=2, name="Winter Warm Tights",
                    short_desc="Stay warm and agile in Winter conditions",
                    price="$79.00", category=category6)

session.add(product30)
session.commit()

print("Running Category & Products added succesfully to the database!")

print("Database populated Successfully!")

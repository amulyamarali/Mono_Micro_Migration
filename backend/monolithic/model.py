from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import faker
import itertools
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv('URL')

uri = URL

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["monolithic_db"]

# # Initialize faker generator
# fake = faker.Faker()

# def unique_id_generator():
#     counter = itertools.count()
#     while True:
#         yield next(counter)

# # Initialize the generator
# id_generator = unique_id_generator()

# def generate_user_details():
#     return {
#         '_id' : next(id_generator),
#         'name': fake.name(),
#         'age': fake.random_int(min=18, max=75),
#         'email': fake.email(),
#         'password': fake.password(length=10),
#         'ph.no': fake.phone_number(),
#         'address': fake.address()
#     }

# collection = db["user"]

# # Initialize an empty list as our collection
# user_collection = []

# # Generate and add user details to the collection
# for _ in range(10):  # Change the range as needed
#     user_collection.append(generate_user_details())

# # insert usercollection into user collection
# collection.insert_many(user_collection)


# adding products to the database
product_collection = db["products"]
# product_collection.delete_many({})

computer_docs = [{
    "id": "1",
    "product": "Computer",
    "company": "Dell",
    "model": "Inspiron 15",
    "price": "899.99",
    "category": "Electronics",
    "description": "A versatile laptop with powerful performance and a sleek design."
},
    {
        "id": "2",
        "product": "Computer",
        "company": "HP",
        "model": "Pavilion 27",
        "price": "1299.00",
        "category": "Electronics",
        "description": "An all-in-one desktop PC with a large display and high-speed processing."
},
    {
        "id": "3",
        "product": "Computer",
        "company": "Apple",
        "model": "MacBook Air",
        "price": "1199.00",
        "category": "Electronics",
        "description": "An ultrathin and lightweight laptop known for its portability and smooth performance."
},
    {
        "id": "4",
        "product": "Computer",
        "company": "Lenovo",
        "model": "IdeaPad Flex",
        "price": "799.50",
        "category": "Electronics",
        "description": "A flexible 2-in-1 laptop with touchscreen capabilities and powerful processing."
},
    {
        "id": "5",
        "product": "Computer",
        "company": "Acer",
        "model": "Predator Helios 300",
        "price": "1299.00",
        "category": "Electronics",
        "description": "A gaming laptop with high-performance graphics and advanced cooling technology."
},
    {
        "id": "6",
        "product": "Computer",
        "company": "Microsoft",
        "model": "Surface Pro 7",
        "price": "999.99",
        "category": "Electronics",
        "description": "A versatile 2-in-1 tablet and laptop with a detachable keyboard and stylus support."
},
    {
        "id": "7",
        "product": "Computer",
        "company": "Asus",
        "model": "ZenBook 14",
        "price": "899.00",
        "category": "Electronics",
        "description": "A compact laptop with a premium build, strong performance, and long battery life."
},
    {
        "id": "8",
        "product": "Computer",
        "company": "Alienware",
        "model": "Aurora R10",
        "price": "1999.00",
        "category": "Electronics",
        "description": "A high-end gaming desktop with customizable components and advanced graphics capabilities."
},
    {
        "id": "9",
        "product": "Computer",
        "company": "HP",
        "model": "EliteBook 840",
        "price": "1299.00",
        "category": "Electronics",
        "description": "A business laptop with robust security features, reliable performance, and sleek design."
},
    {
        "id": "10",
        "product": "Computer",
        "company": "Lenovo",
        "model": "ThinkCentre M720",
        "price": "799.00",
        "category": "Electronics",
        "description": "A compact and powerful desktop computer suitable for business and productivity tasks."
},
    {
        "id": "11",
        "product": "Computer",
        "company": "Dell",
        "model": "XPS 13",
        "price": "1499.00",
        "category": "Electronics",
        "description": "A premium ultrabook with a stunning display, strong performance, and sleek design."
},
    {
        "id": "12",
        "product": "Computer",
        "company": "Acer",
        "model": "Chromebook 14",
        "price": "349.99",
        "category": "Electronics",
        "description": "A lightweight and affordable laptop running on Chrome OS, ideal for web-based tasks."
}
]

mobile_docs = [{

    "id": "1",
    "product": "Mobile",
    "company": "Apple",
    "model": "iPhone 13 Pro",
    "price": "1099.00",
    "category": "Electronics",
    "description": "The latest iPhone model with advanced camera capabilities and powerful performance."
},
    {
        "id": "2",
        "product": "Mobile",
        "company": "Samsung",
        "model": "Galaxy Z Fold 3",
        "price": "1799.00",
        "category": "Electronics",
        "description": "A foldable smartphone with a large display and multitasking features."
},
    {
        "id": "3",
        "product": "Mobile",
        "company": "Google",
        "model": "Pixel 6",
        "price": "799.99",
        "category": "Electronics",
        "description": "A Google Pixel phone with exceptional camera quality and the latest Android features."
},
    {
        "id": "4",
        "product": "Mobile",
        "company": "OnePlus",
        "model": "9 Pro",
        "price": "899.00",
        "category": "Electronics",
        "description": "A flagship OnePlus phone known for its smooth performance and fast charging."
},
    {
        "id": "5",
        "product": "Mobile",
        "company": "Xiaomi",
        "model": "Mi 11 Ultra",
        "price": "999.50",
        "category": "Electronics",
        "description": "A high-spec Xiaomi phone with a versatile camera system and powerful hardware."
},
    {
        "id": "6",
        "product": "Mobile",
        "company": "Sony",
        "model": "Xperia 1 III",
        "price": "1199.00",
        "category": "Electronics",
        "description": "A Sony Xperia phone with a 4K display and pro-level camera features."
},
    {
        "id": "7",
        "product": "Mobile",
        "company": "LG",
        "model": "G9 ThinQ",
        "price": "749.00",
        "category": "Electronics",
        "description": "An LG smartphone with AI-enhanced features and a sleek design."
},
    {
        "id": "8",
        "product": "Mobile",
        "company": "Motorola",
        "model": "Edge 20",
        "price": "599.99",
        "category": "Electronics",
        "description": "A Motorola Edge phone with 5G capabilities and a high-refresh-rate display."
},
    {
        "id": "9",
        "product": "Mobile",
        "company": "Huawei",
        "model": "P50 Pro",
        "price": "1299.00",
        "category": "Electronics",
        "description": "A Huawei flagship phone with advanced camera technology and sleek aesthetics."
},
    {
        "id": "10",
        "product": "Mobile",
        "company": "Oppo",
        "model": "Find X5 Pro",
        "price": "899.50",
        "category": "Electronics",
        "description": "An Oppo Find X phone with innovative design and impressive camera features."
},
    {
        "id": "11",
        "product": "Mobile",
        "company": "Nokia",
        "model": "8.4 5G",
        "price": "549.00",
        "category": "Electronics",
        "description": "A Nokia smartphone with 5G connectivity and a focus on reliability."
},
    {
        "id": "12",
        "product": "Mobile",
        "company": "Realme",
        "model": "GT Master Edition",
        "price": "379.99",
        "category": "Electronics",
        "description": "A Realme phone designed in collaboration with a renowned designer, featuring a unique aesthetic."
}
]

product_collection.insert_many(computer_docs)
product_collection.insert_many(mobile_docs)

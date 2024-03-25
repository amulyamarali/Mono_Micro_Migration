from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import faker
import itertools
# Initialize faker generator
fake = faker.Faker()

def unique_id_generator():
    counter = itertools.count()
    while True:
        yield next(counter)

# Initialize the generator
id_generator = unique_id_generator()

def generate_user_details():
    return {
        '_id' : next(id_generator),
        'name': fake.name(),
        'age': fake.random_int(min=18, max=75),
        'email': fake.email(),
        'password': fake.password(length=10),
        'ph.no': fake.phone_number(),
        'address': fake.address()
    }


uri = "mongodb+srv://2003codehelp:priyacloud@ecommerce.vw8rjsx.mongodb.net/?retryWrites=true&w=majority&appName=ECommerce"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["monolithic_db"]
collection = db["user"]

# add values into user collection

# document = {"_id": "1", "name": "John Doe", "age": 30, "email": "john@gmail.com", "password" : "1idk@", "ph.no": "9000090000", "address": "123, Baker Street, London, UK"}
# collection.insert_one(document)


# Initialize an empty list as our collection
user_collection = []

# Generate and add user details to the collection
for _ in range(10):  # Change the range as needed
    user_collection.append(generate_user_details())

# insert usercollection into user collection
collection.insert_many(user_collection)

# delete all the documents from the collection
# collection.delete_many({})



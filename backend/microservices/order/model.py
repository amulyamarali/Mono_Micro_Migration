from pymongo import MongoClient


URL = "mongodb+srv://2003codehelp:priyacloud@ecommerce.vw8rjsx.mongodb.net/?retryWrites=true&w=majority&appName=ECommerce"

client = MongoClient(URL)
db = client['microservice_order_db']  # Change 'your_database_name' to your actual database name
order_collection = db['order']
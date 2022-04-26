from ast import Str
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
NUM_RECORDS_TO_GENERATE = 1000
MONGODB_ATLAS_URL = 'mongodb+srv://XXX:XXXXXXX@cayman.ya2tg.azure.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
DATABASE = 'retail'
COLLECTION = 'superstore'

# Using variables.
print('Num Records to generate: ' + str(NUM_RECORDS_TO_GENERATE))
print('MongoDB Atlas DB URL: ' + MONGODB_ATLAS_URL)
print('Database: ' + DATABASE)
print('Collection: ' + COLLECTION)
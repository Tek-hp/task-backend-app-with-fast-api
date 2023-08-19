from dotenv import load_dotenv
import os

load_dotenv()

# Mongo Attributes.

USERNAME =  os.getenv('USER_NAME')
PASS = os.getenv('PASSWWORD_KEY')

mongodb_uri = f"mongodb+srv://{USERNAME}:{PASS}@cluster0.ezwy79d.mongodb.net/"


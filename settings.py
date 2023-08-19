from dotenv import load_dotenv
import os

load_dotenv()

# Mongo Attributes.

__USERNAME__ =  os.getenv('USER_NAME')
__PASS__ = os.getenv('PASSWWORD_KEY')
__CLUSTERNAME__ = os.getenv('CLUSTERNAME')

mongodb_uri = f"mongodb+srv://{__USERNAME__}:{__PASS__}@{__CLUSTERNAME__}.ezwy79d.mongodb.net/"


import os

MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://localhost:27017/')
MONGODB_USR = os.getenv('MONGODB_USR', 'admin')
MONGODB_PWD = os.getenv('MONGODB_PWD', 'password')
REACT_APP_URL = os.getenv('REACT_APP_URL', 'http://localhost:3000')
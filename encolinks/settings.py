# encoding: utf-8
import os


DEBUG = True
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'a7b05c4e06fe0502af4a3d42dd41327b'
)
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHENY_DATABASE_URI',
    'sqlite:///tmp.db'
)

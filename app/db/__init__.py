from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# Connect to the db using dotenv variable and sqlalchemy

engine = create_engine(getenv('DB_URL'),echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    # also needed for close_db to work

    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        # Store db connection in flask context
        g.db = Session()
    return g.db

#close db connection when finished

# when pop() tries to find and remove db from g object, if db exists, db close ends the connection

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
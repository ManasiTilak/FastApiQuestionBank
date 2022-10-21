from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
from .config import settings

password = urllib.parse.quote_plus(settings.database_password)
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'



# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='Tut_FastApi', user='postgres', password='Sana@2020', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break

#     except Exception as error:
#         print("Connectino to database failed")
#         print("Error: ", error)
#         time.sleep(2)
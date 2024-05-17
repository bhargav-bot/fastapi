from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Bhargav%401908@localhost/bhargav'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_link = "sqlite:///C:/Users/Wojtek/DataGripProjects/identifier.sqlite"
engine = create_engine(db_link)

Session = sessionmaker(bind=engine)
session = Session()



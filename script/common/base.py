from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:pharezpic123@localhost:5432/spotify_genre")
session = Session(engine)

Base = declarative_base()

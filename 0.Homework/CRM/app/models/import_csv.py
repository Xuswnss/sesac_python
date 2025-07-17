from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base = declarative_base()



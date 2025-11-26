from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///notes.db"

ENGINE = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

BASE = declarative_base()

SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_f8RB4vHSzQOc@ep-wispy-unit-a4vj7tu2-pooler.us-east-1.aws.neon.tech/movie_db?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Integer:
    pass


class String:
    pass


class ForeignKey:
    pass


def relationship():
    return None


def func():
    return None


def joinedload():
    return None
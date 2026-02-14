# db.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:barathkumar@localhost:5433/OtpApp"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class User(Base):
    __tablename__ = "totp"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    totp_secret = Column(String, nullable=False)

### pydantic field

class UserCreate(BaseModel):
    username: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

# Dependency: get DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def createTable():
    # This will create all tables defined in Base subclasses
     Base.metadata.create_all(bind=engine)
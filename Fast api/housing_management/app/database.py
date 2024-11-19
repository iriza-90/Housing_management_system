from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print(f"DATABASE_URL from .env: {os.getenv('DATABASE_URL')}")

# Get Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate that DATABASE_URL is not None
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please check your .env file or environment variables.")

# Print the DATABASE_URL for debugging (remove in production)
print(f"Using DATABASE_URL: {DATABASE_URL}")

# For asynchronous database operations (databases library)
database = Database(DATABASE_URL)

# For SQLAlchemy ORM
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

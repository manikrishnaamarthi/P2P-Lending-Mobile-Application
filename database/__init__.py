from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define your database connection string
DATABASE_URI = "sqlite:///example.db"  # Example SQLite database

# Create the database engine
engine = create_engine(DATABASE_URI)

# Create a session factory
Session = sessionmaker(bind=engine)

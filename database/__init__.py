from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = "postgresql://postgres:gdADC4gaG4AabFAaGgAG215eDAEAe*ec@viaduct.proxy.rlwy.net:34504/railway" 

# Create the database engine
engine = create_engine(DATABASE_URI)

# Create a session factory
Session = sessionmaker(bind=engine)

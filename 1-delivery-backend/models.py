from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base

# create database connection
db = create_engine("sqlite:///database/database.db")
# create db base
Base = declarative_base()

# create class/table mapping
## Users
class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String)
    email = Column("mail", String, nullable=False)
    password = Column("password", String)
    is_active = Column("is_active", Boolean)
    is_admin = Column("is_admin", Boolean, default=False)
    # add created_at and updated_at later
    created_at = Column("created_at", DateTime, server_default=func.now())    
    updated_at = Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now())
    
    def __init__(self, username: str, email: str, password: str, is_active: bool = True, is_admin: bool = False):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_admin = is_admin
## Orders
## OrderItems

# Run metadata to create tables
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, func

Base = declarative_base()

class Game(Base):
    
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    vendor = Column(String, nullable=False)
    platform = Column(ARRAY(String))
    rating = Column(String)  
    link = Column(String, unique=True)
    original_price = Column(Float)
    selling_price = Column(Float) 
    discount = Column(Float, default=0)    
    release_date = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
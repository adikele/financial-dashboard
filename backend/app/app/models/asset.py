from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.setup import Base

class Asset(Base):
    __tablename__ = "assets"
    
    #id = Column(Integer, primary_key=True, index=True)
    name_of_asset = Column(String, primary_key=True, index=True)
    original_value = Column(Integer) 
    owner_id = Column(Integer, ForeignKey("users.id")) 

    owner = relationship("User", back_populates="assets") 
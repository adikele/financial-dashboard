from pydantic import BaseModel
from typing import List


class AssetBase(BaseModel):
    name_of_asset: str
    original_value: int
    
class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    #id: int
    owner_id: int 

    class Config:
        orm_mode = True
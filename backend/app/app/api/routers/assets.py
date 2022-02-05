from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.api.schemas.asset import Asset, AssetCreate
#from app.api.schemas.user import UserSchema
from app.api.deps import get_db, get_current_user
from app.crud import crud_asset


router = APIRouter()

@router.get("/assetsOfSameValue/{original_value}", response_model=Asset, tags=['assets'])
def read_asset_by_original_value(original_value: int, db: Session = Depends(get_db)):
    db_asset = crud_asset.get_asset_by_original_value(db, original_value=original_value)
    return db_asset

@router.get("/manyAssetsOfSameValue/{original_value}", response_model=List[Asset], tags=['assets'])
def read_many_by_original_value(original_value: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_asset = crud_asset.get_many_assets_by_original_value(db, original_value=original_value, skip=skip, limit=limit)
    return db_asset

@router.post("/users/{user_id}/assets/", response_model=Asset, tags=['assets'])
def create_asset_for_user(
    user_id: int, asset: AssetCreate, db: Session = Depends(get_db)
):
    return crud_asset.create_user_asset(db=db, asset=asset, user_id=user_id)


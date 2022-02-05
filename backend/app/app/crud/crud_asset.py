from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.api.schemas.asset import AssetCreate

def get_asset_by_original_value(db: Session, original_value: str):
    #the one below worked, returned one matching original_value
    return db.query(Asset).filter(Asset.original_value == original_value).first()
    
def get_many_assets_by_original_value(db: Session, original_value: str, skip: int = 0, limit: int = 100):
    return db.query(Asset).filter(Asset.original_value == original_value).offset(skip).limit(limit).all()

def create_user_asset(db: Session, asset: AssetCreate, user_id: int):
    db_asset = Asset(**asset.dict(), owner_id=user_id)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset
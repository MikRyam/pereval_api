from fastapi import APIRouter, Depends
from typing import List
# from auth.oauth2 import get_current_user

from routers.schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Creat user
@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)): 
    return db_user.create_user(db, request)
 

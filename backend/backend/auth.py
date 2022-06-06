import bson.errors

from backend.errors import AuthenticationError
from backend.storage.database import DbInterface


def authenticate(user_ref: str, db: DbInterface) -> bool:
    try:
        res = db.get_user_ref(user_ref)
    except bson.errors.InvalidId as e:
        return False
    if res is None:
        return False
    return True

from backend.storage.database import DbInterface


def register_user(db: DbInterface) -> str:
    return db.create_user()
    

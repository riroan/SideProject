from app.database import Database
from fastapi import Depends, Request
from sqlalchemy.orm import Session


def app_db(request: Request) -> Database:
    return request.app.db


# TODO: 세션 관리 방식 uow로 변경
async def get_session(db: Database = Depends(app_db)) -> Session:
    session = db.get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

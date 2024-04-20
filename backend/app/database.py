from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, sessionmaker


class Database:
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        port: int,
        db_name: str,
        db_type: str = "mysql+pymysql",
        echo: bool = False,
    ):
        url = URL.create(
            drivername=db_type,
            username=user,
            password=password,
            host=host,
            port=port,
            database=db_name,
        )
        self.engine = create_engine(url, pool_size=15, echo=echo)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self) -> Session:
        return self.SessionLocal()

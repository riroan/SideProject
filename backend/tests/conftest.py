import pytest
import pytest_asyncio
from app import create_app
from app.depends.common import get_session
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from model.base import Base
from settings import TSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=False,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


async def get_test_session():
    try:
        db = TestingSessionLocal()
        yield db
        db.commit()
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def settings():
    return TSettings()


@pytest.fixture
def app(test_db, settings) -> FastAPI:
    app = create_app(settings)
    app.dependency_overrides[get_session] = get_test_session

    return app


@pytest_asyncio.fixture
async def client(app: FastAPI):
    async with AsyncClient(
        base_url="http://localhost:8000", transport=ASGITransport(app=app)
    ) as ac:
        yield ac

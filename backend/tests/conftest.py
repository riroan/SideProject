from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
import pytest
import pytest_asyncio

from app import create_app
from settings import TestSettings


@pytest.fixture
def app() -> FastAPI:
    settings = TestSettings()

    return create_app(settings)


@pytest_asyncio.fixture
async def client(app: FastAPI):
    async with AsyncClient(
        base_url="http://localhost:8000",
        transport=ASGITransport(app=app)
    ) as ac:
        yield ac


@pytest.fixture
def tc(app: FastAPI) -> TestClient:
    return TestClient(app)

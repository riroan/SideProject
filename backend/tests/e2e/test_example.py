from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    response = await client.get("/example/root")
    assert response.status_code == 200

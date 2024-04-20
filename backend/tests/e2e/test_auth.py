import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    response = await client.post(
        "/api/auth/register",
        json={
            "nickname": "abc",
            "email": "email",
            "password": "pw",
            "gender": 1,
            "birthday": "2024-04-14 16:00:00",
        },
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_register_failed_when_duplicated_nickname(client: AsyncClient):
    response = await client.post(
        "/api/auth/register",
        json={
            "nickname": "abc",
            "email": "email",
            "password": "pw",
            "gender": 1,
            "birthday": "2024-04-14 16:00:00",
        },
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post(
        "/api/auth/register",
        json={
            "nickname": "abc",
            "email": "email",
            "password": "pw",
            "gender": 1,
            "birthday": "2024-04-14 16:00:00",
        },
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

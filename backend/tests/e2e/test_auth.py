import jwt
import pytest
from fastapi import status
from httpx import AsyncClient
from settings import TSettings

# TODO: 더미 유저 생성하는 fixture 생성


def create_dummy_user_data(
    nickname: str = "abc",
    email: str = "email",
    password: str = "pw",
    gender: int = 1,
    birthday: str = "2024-04-14 16:00:00",
):
    return {
        "nickname": nickname,
        "email": email,
        "password": password,
        "gender": gender,
        "birthday": birthday,
    }


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    response = await client.post(
        "/api/auth/register",
        json=create_dummy_user_data(),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_register_failed_when_duplicated_nickname(client: AsyncClient):
    response = await client.post(
        "/api/auth/register",
        json=create_dummy_user_data(),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post(
        "/api/auth/register",
        json=create_dummy_user_data(),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_register_and_login_success(client: AsyncClient, settings: TSettings):
    nickname = "nickname"
    email = "email@email.email"
    response = await client.post(
        "/api/auth/register",
        json=create_dummy_user_data(nickname=nickname, email=email),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post(
        "/api/auth/login",
        json={"email": email, "password": "pw"},
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == status.HTTP_200_OK
    token = response.json()["result"]
    user_data = jwt.decode(
        token, settings.jwt_secret, algorithms=settings.jwt_algorithm
    )

    assert user_data["nickname"] == nickname
    assert user_data["email"] == email


@pytest.mark.asyncio
async def test_register_and_login_fail_when_invalid_password(client: AsyncClient):
    nickname = "nickname"
    email = "email@email.email"
    response = await client.post(
        "/api/auth/register",
        json=create_dummy_user_data(nickname=nickname, email=email),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post(
        "/api/auth/login",
        json={"email": email, "password": "invalid_pw"},
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_register_and_login_fail_when_not_found(client: AsyncClient):
    response = await client.post(
        "/api/auth/login",
        json={"email": "not_found_email", "password": "invalid_pw"},
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

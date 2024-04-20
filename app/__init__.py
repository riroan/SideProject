from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api.auth import api as auth


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"]
    )
    app.add_middleware(
        GZipMiddleware,
        minimum_size=1024
    )

    app.include_router(auth, prefix="/api/auth")

    return app

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.example import api as example
from settings import Settings


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.app_name
    )

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

    app.include_router(example, prefix="/example")

    return app

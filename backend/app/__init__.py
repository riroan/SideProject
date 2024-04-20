from app.api.auth import api as auth
from app.api.example import api as example
from app.database import Database
from app.error_handler import handle_error
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from settings import Settings


def create_app(settings: Settings):
    app = FastAPI(title=settings.app_name)

    db = Database(
        host=settings.db_host,
        user=settings.db_user,
        password=settings.db_password,
        port=settings.db_port,
        db_name=settings.db_name,
        echo=True,
    )

    handle_error(app)

    app.db = db

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    app.add_middleware(GZipMiddleware, minimum_size=1024)

    app.include_router(example, prefix="/example")
    app.include_router(auth, prefix="/api/auth")

    return app

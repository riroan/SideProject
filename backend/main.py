import uvicorn
from app import create_app
from settings import Settings

app = create_app(Settings())

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

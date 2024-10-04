from fastapi import FastAPI
from bundle.database import Base, engine
from bundle.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router)

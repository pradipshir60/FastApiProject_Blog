import os
from fastapi import FastAPI
import uvicorn
from config.database import Base, engine
import user.authentication as authentication
from user.routes import router as userrouter
from blog.routes import router as blogrouter
from role.routes import router as rolerouter
from userrole.routes import router as userrolerouter
from endpoint.routes import router as endpointrouter
from roleendpoint.routes import router as roleendpointrouter
from menu.routes import router as menurouter
from menurole.routes import router as menurolerouter
from convertdoc.routes import router as convertdocrouter
from emailmanage.routes import router as emailrouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    tags=["authentication"]
)

Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    # Add more allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(userrouter)
app.include_router(blogrouter)
app.include_router(rolerouter)
app.include_router(userrolerouter)
app.include_router(endpointrouter)
app.include_router(roleendpointrouter)
app.include_router(menurouter)
app.include_router(menurolerouter)
app.include_router(convertdocrouter)
app.include_router(emailrouter)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/blog/assets", StaticFiles(directory="blog/assets"), name="blog")
app.mount("/emailmanage/assets", StaticFiles(directory="emailmanage/assets"), name="emailmanage")
"""Wukong Math Quest - FastAPI Backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.levels import router as levels_router
from .api.progress import router as progress_router

app = FastAPI(
    title="Wukong Math Quest API",
    description="Backend for AI-powered children's educational game",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(levels_router)
app.include_router(progress_router)


@app.get("/")
def root():
    return {
        "name": "Wukong Math Quest API",
        "version": "0.1.0",
        "docs": "/docs",
    }

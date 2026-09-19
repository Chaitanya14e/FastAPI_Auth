import os

from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase environment variables are missing")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

app = FastAPI(title="Auth API")


from app.routes.auth_routes import router as auth_router
from app.routes.protected_routes import router as protected_router

app.include_router(auth_router)
app.include_router(protected_router)

@app.get("/")
def root():
    return {
        "message": "Auth API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "supabase": "connected"
    }
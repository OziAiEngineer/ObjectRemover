from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.database_config import connect_to_mongo, close_mongo_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events for database and optional services.
    """
    # ── Startup ───────────────────────────────────────────────────────────────
    print("[Lifespan] Starting up...")
    
    # Connect to MongoDB
    await connect_to_mongo()
    
    print("[Lifespan] Startup complete")
    
    yield
    
    # ── Shutdown ──────────────────────────────────────────────────────────────
    print("[Lifespan] Shutting down...")
    
    # Close MongoDB connection
    await close_mongo_connection()
    
    print("[Lifespan] Shutdown complete")


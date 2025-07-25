from fastapi import FastAPI
from app.api import test
from app.routes import dashboard

app = FastAPI()

# Register routes
app.include_router(test.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")

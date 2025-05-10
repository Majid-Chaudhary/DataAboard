from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers (to be defined in api/ directory)
from api.routes_users import router as user_router
from api.routes_workspace import router as workspace_router
from api.routes_access import router as access_router

app = FastAPI(
    title="DataDemocrat API",
    description="Self-service on-prem data platform for secure SQL and ML workspaces",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Allow local frontend/dev environment to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route groups
app.include_router(user_router, prefix="/auth", tags=["Auth"])
app.include_router(workspace_router, prefix="/workspace", tags=["Workspace"])
app.include_router(access_router, prefix="/access", tags=["Access"])

@app.get("/")
def read_root():
    return {"msg": "Welcome to DataDemocrate backend API!"}
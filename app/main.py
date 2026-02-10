from fastapi import FastAPI
from app.db.db_connection import Base, engine
from app.routes import Login_router, Register_router, Query_router, HealthCheck_router, History_router
import warnings

warnings.filterwarnings("ignore")

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(HealthCheck_router.router)
app.include_router(Login_router.router)
app.include_router(Register_router.router)
app.include_router(Query_router.router)
app.include_router(History_router.router)
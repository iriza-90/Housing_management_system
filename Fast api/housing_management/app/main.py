from fastapi import FastAPI
from app.database import Base, engine, database
from app.routers import users, properties, payments, applications, tenants, maintenance

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(applications.router, prefix="/applications", tags=["Applications"])
app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["Maintenance"])

# Startup and Shutdown Events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

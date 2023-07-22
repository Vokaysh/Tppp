```python
from fastapi import FastAPI
from .routes import router as MainRouter
from .database import initialize_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await initialize_db(app)

app.include_router(MainRouter)
```
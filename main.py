```python
from fastapi import FastAPI
from app.main import app as application

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(application)
```
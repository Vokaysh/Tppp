```python
from pydantic import BaseModel

# Define your models here

class User(BaseModel):
    id: str
    name: str
    email: str
    password: str

class Post(BaseModel):
    id: str
    user_id: str
    title: str
    content: str
```
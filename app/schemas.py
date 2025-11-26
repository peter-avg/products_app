from pydantic import BaseModel
from typing import List


class ProductSchema(BaseModel):
    name: str
    description: str

class TagResponse(BaseModel):
    tags: List[str]

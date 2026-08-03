from pydantic import BaseModel
from typing import List


class ValidationSchema(BaseModel):
    is_valid: bool
    warnings: List[str]
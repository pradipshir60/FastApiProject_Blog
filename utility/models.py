from pydantic import BaseModel
from typing import List, Optional

class TokenData(BaseModel):
    email: Optional[str]   
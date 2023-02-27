from typing import Optional

from pydantic import BaseModel


class Version(BaseModel):
    major: Optional[int] = None
    minor: Optional[int] = None
    patch: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

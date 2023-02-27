from typing import Optional

from pydantic import BaseModel


class RecentChanges(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

from typing import List, Optional

from pydantic import BaseModel, Field

from src.methods.argument import Argument
from src.methods.return_type import ReturnType


class Method(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    arguments: Optional[List[Argument]] = Field(default_factory=list)
    multipart_only: Optional[bool] = Field(None)
    return_type: Optional[ReturnType] = Field(None)
    documentation_link: Optional[str] = Field(None)

    def sorted_args(self) -> List[Argument]:
        return sorted(self.arguments, key=lambda x: (x.required, x.name), reverse=True)

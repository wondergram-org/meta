from typing import List, Optional

from pydantic import BaseModel, Field

from src.base_types.any_of import AnyOf
from src.enums import TypeEnum
from src.objects.property import Property


class Object(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    type: Optional[TypeEnum] = Field(None)
    any_of: Optional[List[AnyOf]] = Field(None)
    properties: Optional[List[Property]] = Field(default_factory=list)
    documentation_link: Optional[str] = Field(None)

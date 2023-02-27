from typing import Any, List, Optional

from pydantic import BaseModel

from src.base_types.any_of import AnyOf
from src.base_types.array import Array
from src.enums import PROPERTY_CONVERSION, TypeEnum


class Argument(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[TypeEnum] = None
    default: Optional[Any] = None
    array: Optional[Array] = None
    any_of: Optional[List[AnyOf]] = None
    reference: Optional[str] = None
    required: Optional[bool] = None
    min: Optional[int] = None
    max: Optional[int] = None

    def render(self) -> str:
        """
        Renders argument as it should appear in the head of the method.
        :return: str
        """
        if self.required:
            return f"{self.name}: {self.to_pythonic_value(enable_quotation=False)}"
        return f"{self.name}: Optional[{self.to_pythonic_value(enable_quotation=False)}] = None"

    def to_pythonic_value(self, enable_quotation: bool, **kwargs) -> str:
        """
        Converts type of this argument to its Python equivalent.
        :return: str
        """
        conversion_callable = PROPERTY_CONVERSION.get(self.type)

        if self.type == TypeEnum.ARRAY:
            return conversion_callable(self.array, enable_quotation, **kwargs)
        elif self.type == TypeEnum.ANY_OF:
            return conversion_callable(self.any_of, enable_quotation, **kwargs)
        elif self.type == TypeEnum.REFERENCE:
            return conversion_callable(self.reference, enable_quotation, **kwargs)

        return conversion_callable()

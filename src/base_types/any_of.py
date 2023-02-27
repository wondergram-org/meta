from typing import TYPE_CHECKING, Any, List, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from src.base_types.array import Array

from src.enums import PROPERTY_CONVERSION, TypeEnum


class AnyOf(BaseModel):
    type: Optional[TypeEnum] = None
    array: Optional["Array"] = None
    any_of: Optional[List["AnyOf"]] = None
    reference: Optional[str] = None
    default: Optional[Any] = None

    def to_pythonic_value(self, enable_quotation: bool, **kwargs) -> str:
        """
        Converts custom API type to pythonic equivalent.
        :return: str
        """
        conversion_callable = PROPERTY_CONVERSION.get(self.type)

        if self.type == TypeEnum.ANY_OF:
            return conversion_callable(self.any_of, enable_quotation, **kwargs)
        elif self.type == TypeEnum.REFERENCE:
            return conversion_callable(self.reference, enable_quotation, **kwargs)

        return conversion_callable()

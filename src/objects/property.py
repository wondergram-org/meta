from keyword import kwlist as prohibited_words
from typing import Any, List, Optional

from humps import pascalize
from pydantic import BaseModel

from src.base_types.any_of import AnyOf
from src.base_types.array import Array
from src.enums import PROPERTY_CONVERSION, TypeEnum


class Property(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enumeration: Optional[List[str]] = None
    default: Optional[Any] = None
    required: Optional[bool] = None
    type: Optional[TypeEnum] = None
    array: Optional[Array] = None
    any_of: Optional[List[AnyOf]] = None
    reference: Optional[str] = None

    def render(self, obj_name: str) -> str:
        """
        Make property a valid pythonic string.
        """

        name = f"{self.name}{'_' if self.name in prohibited_words else ''}"
        type_hint = (
            f"{pascalize(obj_name + self.name.title())}"
            if self.enumeration
            else (
                f"Literal[{self.default!r}]"
                if self.required and self.default
                else (
                    f"Optional[{self.to_pythonic_value(True)}]"
                    if not self.required
                    else self.to_pythonic_value(True)
                )
            )
        )
        value = (
            f"Field({self.get_default()}, alias={self.name!r})"
            if self.name in prohibited_words
            else f"Field({self.get_default()})"
        )

        result = (
            f"{name}: {type_hint} = "
            f"{value if self.get_default() else value.replace(', ', '')}"
        )
        return result

    def get_default(self) -> str:
        """
        Returns default value of this property.
        :return: str
        """
        if self.required and not self.default:
            return ""

        if self.default:
            return f"default={self.default!r}"

        if self.array:
            return f"default_factory=list"

        return "default=None"

    def to_pythonic_value(self, enable_quotation: bool, **kwargs) -> str:
        """
        Converts custom API type to pythonic equivalent.
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

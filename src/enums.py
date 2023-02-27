from enum import Enum
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.base_types.any_of import AnyOf
    from src.base_types.array import Array


class TypeEnum(Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    ARRAY = "array"
    REFERENCE = "reference"
    ANY_OF = "any_of"
    PROPERTIES = "properties"


def to_int(**kwargs) -> str:
    return "int"


def to_string(**kwargs) -> str:
    return "str"


def to_float(**kwargs) -> str:
    return "float"


def to_bool(**kwargs) -> str:
    return "bool"


def to_object(reference: str, enable_quotation: bool = True, **kwargs) -> str:
    if enable_quotation:
        return f'"{reference}"'
    return reference


def to_list(array: "Array", enable_quotation: bool, **kwargs) -> str:
    return f"List[{array.to_pythonic_value(enable_quotation)}]"


def to_union(any_of: List["AnyOf"], enable_quotation: bool, **kwargs) -> str:
    return f"Union[{', '.join(m.to_pythonic_value(enable_quotation) for m in any_of)}]"


PROPERTY_CONVERSION = {
    TypeEnum.INTEGER: to_int,
    TypeEnum.STRING: to_string,
    TypeEnum.FLOAT: to_float,
    TypeEnum.BOOL: to_bool,
    TypeEnum.REFERENCE: to_object,
    TypeEnum.ARRAY: to_list,
    TypeEnum.ANY_OF: to_union,
}

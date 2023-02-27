from json import JSONDecodeError
from typing import Dict, List, Union

from pydantic import ValidationError
from requests import get

from src.body import Body
from src.objects.object import Object
from src.objects.property import Property


class Schema:
    def __init__(
        self, schema_url: str = "https://ark0f.github.io/tg-bot-api/custom.min.json"
    ) -> None:
        self.content = self.fetch(schema_url)

    @staticmethod
    def fetch(url: str) -> Body:
        """
        Fetches and validates schema from URL.
        """
        try:
            schema = Body(**get(url).json())
        except (ValidationError, JSONDecodeError):
            raise TypeError("Bad response")
        return schema

    def get_ref(self, name: str) -> Object:
        """
        Returns object by its name.
        """
        return [obj for obj in self.content.objects if obj.name == name][0]

    def get_discriminator(self, model: str) -> Union[str, None]:
        """
        Return the name of a field that appear in all models of a union type.
        If a field appears in all models more than once, it's a discriminator.
        """
        obj = self.get_ref(model)

        if not obj.any_of:
            raise ValueError(f"Object {model!r} is not a union type")

        prop_frequency: Dict[str, int] = {}
        variations: List[Object] = [self.get_ref(a.reference) for a in obj.any_of]

        for v in variations:
            for p in v.properties:
                prop_frequency.update({p.name: prop_frequency.get(p.name, 0) + 1})

        return repr(max(prop_frequency, key=prop_frequency.get))

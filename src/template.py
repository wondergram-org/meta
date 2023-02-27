from pathlib import Path
from typing import Any, Dict

from humps import decamelize, pascalize
from jinja2 import Environment, FileSystemLoader

from src.utils.format import unmarkdown
from src.utils.wrap import wrapped

templates_dir: Path = Path(__file__).parent / "templates"


class Renderer:
    def __init__(self):
        self.environment = Environment(
            loader=FileSystemLoader(searchpath=[templates_dir])
        )
        self.environment.filters.update(
            {
                "pascalize": pascalize,
                "decamelize": decamelize,
                "unmarkdown": unmarkdown,
                "wrapped": wrapped,
            }
        )

    def render_template(
        self,
        template_name: str,
        context: Dict[str, Any],
    ):
        return self.environment.get_template(template_name).render(context)

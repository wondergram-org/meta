from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from black import FileMode, format_str

from src.schema import Schema
from src.template import Renderer

current_dir = Path.cwd()


class Dispatcher:
    def __init__(
        self, dir: Optional[Union[str, Path]] = Path(current_dir / "generated")
    ) -> None:
        self.schema = Schema()
        self.renderer = Renderer()

        self.dir = Path(dir) if isinstance(dir, str) else dir
        self.dir.mkdir(exist_ok=True)

        print(
            f"Dispatcher started with API v{self.schema.content.version} "
            f"from {self.schema.content.recent_changes}"
        )

    def start(self) -> None:
        before = datetime.now()

        for tmp in Path(current_dir / "src" / "templates").iterdir():
            with Path(self.dir / tmp.name.strip(".jinja2")).open("w") as f:
                f.write(
                    format_str(
                        self.renderer.render_template(
                            tmp.name, {"schema": self.schema}
                        ),
                        mode=FileMode(),
                    )
                )

        after = datetime.now()
        print(f"Finished in {(after - before).microseconds} μs")

from textwrap import wrap
from typing import Optional

from src.const import LINE_BREAK_LENGTH, LINE_BREAK_STYLE


def wrapped(
    text: str,
    line_break: Optional[str] = LINE_BREAK_STYLE,
    break_every: Optional[int] = LINE_BREAK_LENGTH,
) -> str:
    return line_break.join(wrap(text, break_every))

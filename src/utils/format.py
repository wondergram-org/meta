from re import sub

from markdown import markdown as to_html

equivalents = {
    "&nbsp;": " ",
    "&gt;": ">",
    "&lt;": "<",
    "&amp;": "&",
    "&quot;": '"',
}


def unmarkdown(string: str) -> str:
    """
    Converts Markdown text to HTML, then removes all HTML tags
    and replaces characters starting with & to their equivalent.
    E.g. &nbsp; to space, &gt; to >, &lt; to <, etc.
    """
    html = to_html(string)

    result = sub("<[^<]+?>", "", html)
    for char, equivalent in equivalents.items():
        result = result.replace(char, equivalent)
    return result

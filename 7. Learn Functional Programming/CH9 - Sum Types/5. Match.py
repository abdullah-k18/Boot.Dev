from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    if from_format == DocFormat(3) and to_format == DocFormat(4):
        content = content.replace("# ", "")
        content = f"<h1>{content}</h1>"
        return content
    elif from_format == DocFormat(2) and to_format == DocFormat(1):
        content = f"[PDF] {content} [PDF]"
        return content
    elif from_format == DocFormat(4) and to_format == DocFormat(3):
        content = content.replace("<h1>", "# ")
        content = content.replace("</h1>", "")
        return content
    else:
        raise Exception ("invalid type")

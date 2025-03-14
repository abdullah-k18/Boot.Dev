default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    cmd = commands.copy()
    cmd[new_command] = function
    return cmd


def add_format(formats, format):
    fmt = list(formats)
    fmt.append(format)
    return fmt


def save_document(docs, file_name, doc):
    dc = docs.copy()
    dc[file_name] = doc
    return dc


def add_line_break(line):
    return(line + "\n\n")


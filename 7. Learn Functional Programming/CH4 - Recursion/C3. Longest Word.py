def list_files(parent_directory, current_filepath=""):
    paths = []
    for name, value in parent_directory.items():
        if current_filepath:
            new_path = f"{current_filepath}/{name}"
        else:
            new_path = f"/{name}"

        if value is None:
            paths.append(new_path)
        else:
            paths.extend(list_files(value, new_path))

    return paths

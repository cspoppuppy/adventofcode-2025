def read_input(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, "r") as file:
        content = file.read()
    return content

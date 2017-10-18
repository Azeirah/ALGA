def fileprint(filename, *args, **kwargs):
    """Prints both to file as well as to console"""
    with open(filename, "w") as f:
        print(file=f, *args, **kwargs)
        print(*args, **kwargs)

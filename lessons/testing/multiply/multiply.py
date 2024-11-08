def multiply(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return False
    return a * b
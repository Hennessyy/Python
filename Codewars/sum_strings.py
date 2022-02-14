def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif not a and b:
        return b
    elif a and not b:
        return a
    else:
        return '0'
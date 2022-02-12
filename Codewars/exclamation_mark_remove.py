def remove(s):

    if s and s.endswith('!'):
        return s[:-1]
    else:
        return s


print(remove("Hello!"))


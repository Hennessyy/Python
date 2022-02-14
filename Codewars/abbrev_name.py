def abbrev_name(name):
    ls = name.split(" ")

    return f"{ls[0][0]}.{ls[1][0]}".upper()


print(abbrev_name("leon hennessy"))
def remove(s):
    ls = []
    for i in range(len(s)):
        if i == ( len(s) - 1 ) and s[i] != '!':
            ls.append(s[i]+"!")
        elif i == ( len(s) - 1 ) and s[i] == '!':
            ls.append(s[i])
        elif  s[i] == '!':
            continue
        else:
            ls.append(s[i])

    return ''.join(ls)
    

print(remove("Hi!!!"))

# Improvement 
# def remove(s):
#     return s.replace("!", "") + "!"
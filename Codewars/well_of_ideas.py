def well(x):
    amt = x.count("good")

    if amt > 2:
        return "I smell a series!"
    elif amt <= 2 and amt > 0:
        return "Publish!"
    else:
        return "Fail!"

    
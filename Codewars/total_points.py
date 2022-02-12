def points(games):
    x = 0

    for game in games:
        if int(game[0]) > int(game[2]):
            x += 3
        elif int(game[0]) == int(game[2]):
            x += 1
        else:
            continue
        
    return x


    


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
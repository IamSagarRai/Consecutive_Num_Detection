arry = [1,1,1,54,54,34,65,23,52,52,52,13,63,43]
rng = len(arry)
for i in range(rng - 2):
    if arry[i] == arry[i + 1] and arry[i + 1] == arry[i + 2]:
        print(arry[i])
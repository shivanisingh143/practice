def hist( list ):
    print(list)
    for i in list:
        times = i
        out = ''
        while times > 0:
            out += '*'
            times = times - 1
        print(out)


list = [3, 5, 7, 9]
hist(list)
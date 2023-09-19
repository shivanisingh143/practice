time = int(input("seconds : "))
days = time / 86400
hour = time / 3600
min = time / 60
sec = time

print(days, hour, min, sec)
print("d:h:m:s-> %d:%d:%d:%d" % (days, hour, min, sec))

#
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# print(day)
# time = time % (24 * 3600)
# print(time)
# hour = time // 3600
# print(hour)
# time %= 3600
# print(time)
# minutes = time // 60
# print(minutes)
# time %= 60
# print(time)
# seconds = time
# print(seconds)
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
days = int(input("days : ")) * 3600 * 24
hour = int(input("hr : ")) * 3600
min = int(input("min : ")) * 60
sec = int(input("sec : "))

print(days, hour, min, sec)
time = days + hour + min + sec

print(time)
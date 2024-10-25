x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))

maxi = max(x,y,z)
mini = min(x,y,z)

sec = (x+y+z)-maxi-mini
print(maxi, sec, mini)
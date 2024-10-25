try:
    x = 1
except Exception as e:
    print("x var not def")
else:
    print("x var def")
try:
    y
except Exception as e:
    print("not def")
else:
    print("var def")
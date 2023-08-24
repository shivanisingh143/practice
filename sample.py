if 5 > 2:
    print('greater')

##casting
x = str(3)
print(x)

####Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)

x = memoryview(bytes(5))
print(type(x))

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(a.upper())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(','))

quantity = 3
itemno = 567
price = 49.95
myorder = "do {2} is {0} hwgja {1}"
print(myorder.format(quantity, itemno, price))

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

tuple = {'john', 'sweet'}
chk = '#'.join(tuple)
print(chk)

txt = "hello sam"
new = str.maketrans("h", "s")
print(txt.translate(new))

#######unpack a list

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

color_list = ["Red","Green","White" ,"Black"]
print("first_color: ", color_list[0] + ", " + "last_color: ", color_list[-2])
print("%s %s"%(color_list[0],color_list[-1]))

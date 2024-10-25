import sys
str1 = "one"
str2 = "four"
str3 = "three"
x = 0
y = 112
z = 122.56

print("size of ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("Size of ",str2,"=",str(sys.getsizeof(str2))+ " bytes")
print("Size of ",str3,"=",str(sys.getsizeof(str3))+ " bytes")
print("Size of ",x,"=",str(sys.getsizeof(x))+ " bytes")
print("Size of ",y,"=",str(sys.getsizeof(y))+ " bytes")
print("Size of ",z,"=",str(sys.getsizeof(z))+ " bytes")
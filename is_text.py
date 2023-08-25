def new_string(text):
    if (len(text) >= 2 and text[:2] == "is"):
        print(text)
        return text
    print("is"+text)
    return "is"+text
new_string("isnum")
new_string("new")

def larger_string(text, n):
   result = ""
   print(result)
   for i in range(n):
      result = result + text
      print(result)
   return result
print(larger_string('abc', 2))
print(larger_string('.py', 3))
# str = "shivanisingh"
str = "p"

st = str[:2]
print(st)

n = 3
result = ""
for i in range(n):
    result = result + st
print(result)

def substring_copy(text, n):
  # flen = 2
  # if flen > len(text):
  #   flen = len(text)
  substr = text[:n]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));


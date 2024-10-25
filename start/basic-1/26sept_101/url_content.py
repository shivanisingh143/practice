from http.client import HTTPConnection

conn = HTTPConnection("example.com")

conn.request("GET", "/")
res = conn.getresponse()
a = res.read()
print(a)
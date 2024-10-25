class person:
    def __init__(self, fname, lname):
         self.firstname = fname
         self.lastnast = lname

    def printname(self):
        print("first name is ", self.firstname)

x = person("John", "Doe")
x.printname()
class parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("welcome print", self.firstname)

x = parent("john", "doe")
x.printname()

class child(parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("child class", self.firstname)

y = child("john", "doe", 2018)
y.welcome()



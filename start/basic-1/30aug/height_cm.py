h_feet = int(input("feet is : "))
h_inch = int(input("inch is : "))

h_inch += h_feet * 12

h_cm = round(h_inch * 2.54, 1)
print(h_cm)
import os
os.system("cls")
a = input("A: ") ; b = input("B: ")
if a > b:
    print("A katta: ", a)
elif b > a:
    print("B katta : ",b)
else:
    print("{} va {} sonlar teng".format(a,b))
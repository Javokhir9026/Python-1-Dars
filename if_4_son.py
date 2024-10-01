import os
os.system("cls")
a = int( input("A: ")) ; b = int( input("B: "))
c = int (input("C: ")) ; d = int (input("D: "))
if (a >= b and a >= d and a >= c):
    print("A katta: ", a)
elif (b >= a and b >= c and b >= d):
    print("B katta : ",b)
elif (c >= a and c >= b and c >= d):
    print("C katta : ",c)
elif (d >= a and d >= c and d >= b):
    print("D katta : ",d)
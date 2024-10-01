
        # 1-USUL
import os       # system cls uchun
os.system("cls")

son = 234
print(son, type(son))

son = False
print(son, type(son))

son = "salom"
print(son, type(son))

son  = 123.456
print(son, type(son))

        #  2-USUL
a = 123; b = 1234.23
c = "salom" ; d = False
print()
print("Int ==>",a)
print("Float ==>",b)
print("String ==>",c)
print("Bool ==?",d)
        #  FORMAT KORINISH 1-USUL
print()     
print(f"int ==> {a}\t\tFloat ==> {b}")
print(f"String ==> {c}\tBool ==> {d}")
print()
        #  FORMAT 2-USUL
print("Int ==> {}\t\tFloat ==> {}".format(a,b))
print("Int ==> {}\t\tFloat ==> {}".format(c,d))
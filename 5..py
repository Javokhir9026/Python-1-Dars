import os
os.system("cls")

matn = input("Matn: ")
if matn.isupper() or matn.islower():
    print(True)
if matn[:1].isupper():
    print(True)
else:
    print(False)
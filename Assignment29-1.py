import os

filename=input("Enter file name:")

if os.path.exists(filename):
    print(filename,"exists.")
else:
    print(filename,"does not exists.")
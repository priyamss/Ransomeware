#!/usr/bin/env python
import os
from cryptography.fernet import Fernet
from time import sleep
files = []

for file in os.listdir():
    if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


print(files)
print("Recovering your file system")

sleep(5)


with open("thekey.key","rb") as key:
    secretkey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open (file,"wb") as thefile:
        thefile.write(contents_decrypted)
        sleep(3)
        print("Done")
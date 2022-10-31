#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "Ransomeware.py" or file == "Decrypt.py" or file == "thekey.key" :
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key","rb") as key :
    secretkey = key.read()

for file in files :
    with open(file,"rb") as thefile:
        contents = thefile.read()        
    contents_decrypt = Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_decrypt)

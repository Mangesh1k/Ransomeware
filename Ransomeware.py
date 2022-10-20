import os 
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "Ransomewere.py" or file =="Decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)




with open("thekey.key","rb") as thekey:
    secretkey = thekey.write(thekey.key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_decrypted)



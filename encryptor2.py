"""Encrpytes file. wokring on using pre made key I get to decide vs generated 
key"""
from cryptography.fernet import Fernet 

#key=pword.encode('utf-8')
#store key and read from it
#key=Fernet.generate_key()
"""
#
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

#Encrpyt file
with open('filekey.key', 'rb') as filekey:
    key=filekey.read()
fernet=Fernet(key)

with open('test.txt', 'rb') as file:
    original = file.read()
encrypted=fernet.encrypt(original)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
"""
def encrypt(fileName, key):    
    with open(fileName, 'rb') as rfile:
        original = rfile.read()
    rfile.close()    
    fernet=Fernet(key)
    encrypted_data=fernet.encrypt(original)    
    with open(fileName,'wb') as encrypted_file:   
        encrypted_file.write(encrypted_data)    
    encrypted_file.close()   
    print("encrypted")


if __name__=="__main__":
    print("encryptor ran as main")

"""Encrpytes file. wokring on using pre made key I get to decide vs generated 
key"""
from cryptography.fernet import Fernet 

#make key
pword="paasword="
 
#key=pword.decode('utf-8')
key=pword.encode('utf-8')
#key=bytes(pword, 'utf-8 ')
#store key and read from it
#key=Fernet.generate_key()
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

def encrypt():    
    print("encrypted")

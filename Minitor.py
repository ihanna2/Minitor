from cryptography.fernet import Fernet
import encryptor2
"""
Choose if they want to encrypt or decrypt their file. Or read without 
decrypting it
Have users choose file they want to encrypt. Have them input a password. 
Encrypt file using appended password with key. 
find files in different folders to encrypt
"""
#get file name from user

#choose mode
mode=input("Type 1 for Encryption and 2 for Decryption: ")
mode=int(mode)
#load key
with open("filekey.key",'r') as keyfile:
    key=keyfile.read().encode()

#encryption
if (mode==1):
    print("encryption activate")
    encryptor2.encrypt()
elif(mode==2):
    print("decryption acivated")

else:
    print("Only modes supported are encryption and decryption currently")

file = input("please give a file name: ")

#with open(file, 'w') as data:
#	data.write("test")

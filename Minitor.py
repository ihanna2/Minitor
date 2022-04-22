from cryptography.fernet import Fernet
import encryptor2
import decryptor2
import keyGen
import getpass
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
fileKey="filekey.key"
#should be filekey.key
#load key by checking if keyfile exists.
if keyGen.fileExists(fileKey):
    #if it does, does it have a key?
    if(keyGen.fileHasInfo(fileKey)):           
        with open(fileKey,'r') as keyfile:
            key=keyfile.read().encode()
        keyfile.close()
    else:
        print("\nWould you like to create one? \n 1: yes\n 2: no")
        answer=int(input())
        if answer == 1:
            with open(fileKey,'w') as keyfile:
                keyfile.write(keyGen.writeKey().decode())
            keyfile.close()
            print("key created")
            with open(fileKey,'r') as keyfile:
                key=keyfile.read().encode()
            keyfile.close()
            print("key loaded")
        elif answer ==2:
            print("Error key can not be used in current form. Please configure key to correct format")
            exit()
else:
    answer=int(input("No key file found, would you like to create it?\n 1:Yes \n 2:No "))
    if answer == 1:
        with open(fileKey,'w') as keyfile:
            keyfile.write(keyGen.writeKey().decode())
        keyfile.close()
        print("key created")
        with open(fileKey,'r') as keyfile:
            key=keyfile.read().encode()
        keyfile.close()
        print("key loaded")
    elif answer == 2: 
        print("Error no key file found but do not want one created. Think about what you want. Restart Required.")
        exit()
    else:
        print("Did not enter an accepted answer. Restart required.")
        exit()


#Password Implementation
answer=int(input("Would you like to use a password with your key?\n1:Yes\n2:No\n"))
if answer == 1:
    key=keyGen.passwordKey(key)
          
#encryption
if (mode==1):
    print("encryption mode activated")
    TargetFile = input("please give a file name: ")
    encryptor2.encrypt(TargetFile,key)

#decryption
elif(mode==2):
    print("decryption mode activated")
    TargetFile = input("please give a file name: ")
    decryptor2.decrypt(TargetFile,key)
else:
    print("Only modes supported are encryption and decryption currently")


#with open(file, 'w') as data:
#	data.write("test")

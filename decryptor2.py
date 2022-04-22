#placeholder
"""Description: decryptor file that will decrypt a files data"""

from cryptography.fernet import Fernet
"""
with open("filekey.key", 'rb') as file:
        data=file.readline()
        decData=data.decode('utf-8')    
        print(decData)
        key=decData

# using the key
#key="uUpGAxIwGGNtfSP06FrtNm6-I3sSlBRELUYpTrk2Eoc="
fernet = Fernet(key)

# opening the encrypted file
with open('test.txt', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('test.txt', 'wb') as dec_file:
	dec_file.write(decrypted)
"""
def decrypt(fileName,key):
    with open(fileName,'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    encrypted_file.close()
    
    fernet=Fernet(key)
    unencrypted_data=fernet.decrypt(encrypted_data)

    with open(fileName,'wb') as unencrypted_file:
        unencrypted_file.write(unencrypted_data)
    unencrypted_file.close()    
    print("decrypted")

if __name__=="__main__":
    print("decryptor ran as main")

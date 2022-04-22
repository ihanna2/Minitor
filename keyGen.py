from cryptography.fernet import Fernet 
from pathlib import Path
import os 

def fileExists(fileName):    
    path_to_file = fileName
    path = Path(path_to_file)
    return path.is_file()
#is a key loaded in the file
def fileHasInfo(fileName):
    file_path=fileName
    size=os.stat(file_path).st_size
    if (size==44 or size == 45):
        print("key loaded")
        return True
    else:
        print("Error with key. This could be a key that is too short or long.")
        return False
#if key exists, load it.
def writeKey():
    key = Fernet.generate_key()  
    return key
#if no key, create it.

#main
if __name__=="__main__":    
    #check if key file exists first
    print("keygen ran as main")

# This will essentially be a HashNode of the hashmap
# hashNode class can be things like room1, victors room, car, bathroom etc.. anything we consider a 

from SLLStorage import SLLStorage
from typing import List

""" 
Class variables:
    - string room    //name of the room
    - SLLStorage()    //corresponds to storages that are in the room like desk, vaneer, closet, bathroom, will be SLL (prob not a class variable)
    - int numStorages
    
Class methods:
    //constructors
    - hashNode()
    - hashNode(string k)   
    - hashNode(string k, string item)
    - hashNode(string k, string item, string storage)

    -addStorage() will add a storage to the SLLStorage 
    -removeStorage() will remove a storage from the SLLStorage
    -printStorage() will print all the strorages in the room
"""

# Dont forget to make it so that the user HAS to provide a key that isnt blank in the interface

class HashNode:
    
    def __init__(self, key:str, value:str = None):
        if value is None:
            # key is inputted but value is not
            self.room = key
            self.storages = SLLStorage()
            self.numStorages = 0
        else:
            # both key and value are inputted
            self.room = key
            self.storages = SLLStorage(value)
            self.numStorages = 1
      
    def addStorage(self, storageName:str):
        # add a storage
        if storageName == "":
            print("Error: Please enter a valid storage name that is not blank")
            print("")
            return
        
        found = self.storageExists(storageName)
        
        #check to see if the storage exists already and if so prompt the user that it exists
        if found == 1:
            print(f"Error: {storageName} already exists in the room")
            print("")
            return 
        
        self.storages.appendStorage(storageName)
        self.numStorages =  self.numStorages + 1
        print(f"Successfully added {storageName} to the room")
    
    def removeStorage(self, storageName:str):
        self.storages.remove(storageName)
        self.numStorages = self.numStorages - 1
    
    def printStorages(self):
        self.storages.printList()
    
    def addItemtoStorage(self, storageName:str, item:str):
        self.storages.addItem(storageName, item)
    
    def delRecentlyAddedStorage(self) -> List[str]:
        items = self.storages.pop()
        self.numStorages = self.numStorages - 1
        return items
    
    def storageExists(self, storageName: str) -> int:
        # if the storage does not exist return -1 otherwise return 1
        exists = self.storages.findStorage(storageName)
        return exists
    
    
    
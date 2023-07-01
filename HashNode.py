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
    
    def __init__(self, key:str, storage=None):
        self.room = key
        if storage is not None:
            # means we have a storage
            self.storages = storage
            counter = 0
            currentNode = self.storages.first
            while currentNode:
                # because we loaded in from json we must figure out how many storages we have since we bypassed using json
                counter += 1
                currentNode = currentNode.next
            self.numStorages = counter
        else:
            # means we are starting fresh
            self.storages = SLLStorage()
            self.numStorages = 0
      
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
    
    
    # New Shit
    def to_dict(self):
        return {
            'room': self.room,
            'storage': self.storages.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        storage = SLLStorage.from_dict(data['storage'])
        return cls(data['room'], storage)
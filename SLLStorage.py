from SLLNode import SLLNode
from typing import List

""" 
Class variables:
    - SLLNode *first
    - int numStorages   //number of storages in the 
    
Class methods:
    //constructors
    - SLLStorage()
    - SLLStorage(string n)  //constructor takes the name of the storage
    - void push(string n)   //push a storage to the end of the list 
    - *string *pop()        //pop the storage from the front of the list and return the items array of the storage
    - int remove(string k)  //remove a storage from the list
    - void printStorages()  //print the storages
"""


class SLLStorage:
    def __init__(self, storage=None):
        if storage is None:
            self.first = None
            self.numberStorages = 0
        else:
            self.first = storage
            self.numberStorages = 0
            currentNode = self.first
            while currentNode:
                #print(currentNode.storageName)
                self.numberStorages += 1
                currentNode = currentNode.next         

    def appendStorage(self, storage:str):
        # add a node to the beginning of the list
        newNode = SLLNode(storage)
        if self.numberStorages == 0:
            self.first = newNode
            self.numberStorages += 1
        else:
            newNode.next = self.first
            self.first = newNode
            self.numberStorages += 1

    def printList(self):
        currentNode = self.first
        if self.numberStorages == 0:
            print("There are no storages to print")
            return 
        
        print(f"Here are all of the storages: ")
        while currentNode:
            print(currentNode.storageName)
            currentNode = currentNode.next

    def pop(self) -> List[str]:
        if self.numberStorages == 0:
            print("Error: There are no storages to pop")
            return
        # remove storage from the beginning of the list and return the items stored in that storage
        items = self.first.storedItems
        print(f"Successfully removed the most recently added storage: {self.first.storageName}")
        self.first = self.first.next    # if no songs after self.first then it will be None
        self.numberStorages -= 1
        return items

    def remove(self, storageName:str):
        # will remove some strorage from the room that you dont want
        
        if self.numberStorages == 0:
            return 0
        
        if self.first.storageName == storageName:
            self.first = self.first.next
            self.numberStorages -= 1
            print(f"Successfully removed {storageName}")
            return 1
            
        currentNode = self.first
        
        while currentNode.next:
            if currentNode.next.storageName == storageName:
                currentNode.next = currentNode.next.next
                self.numberStorages -= 1
                print(f"Successfully removed {storageName}")
                return 1
            currentNode = currentNode.next
        
        print(f"{storageName} does not exist in this room")
        return -1

    def addItem(self, strgName:str, item: str):
        if self.numberStorages == 0:
            print("There are no storages to add items to.")
            return 0
        
        currentNode = self.first
        while currentNode:
            if currentNode.storageName == strgName:
                currentNode.appendItem(item)
                return 1
            currentNode = currentNode.next          
            
        print(f"{strgName} does not exist in this room")
        return -1

    def findStorage(self, storageName:str) -> int:
        currentNode = self.first
        found = -1
        while currentNode:
            if currentNode.storageName == storageName:
                found = 1
            currentNode = currentNode.next
        
        return found
    
    # seems like a flaw here, what if the item does not exist in the storage
    def removeItemfromStorage(self, strgName:str, item:str):
        if self.numberStorages == 0:
            print("There are no storages to remove from")
            return 0
        currentNode = self.first
        
        while currentNode:
            if currentNode.storageName == strgName:
                currentNode.removeItem(item)
                print(f"Successfully removed {item} from {strgName}")
                return 1
            
            currentNode = currentNode.next

        print(f"Error: The storage '{strgName}' does not exist in this room")
        return -1
    
    def printStorageItems(self, strgName):
        if self.numberStorages == 0:
            return print("There are no storages to print items from")
        currentNode = self.first
        while currentNode:
            if currentNode.storageName == strgName:
                currentNode.printStoredItems()
                return
            currentNode = currentNode.next
        
        print(f"Error: The storage '{strgName}' does not exist in this room")
    
    # New shit
    
    def to_dict(self):
        return self.first.to_dict() if self.first else None

    @classmethod
    def from_dict(cls, data):
        linked_list = SLLNode.from_dict(data)
        return cls(linked_list)

    
    
    
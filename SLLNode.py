
""" 
Class variables:
    - string storageName
    - string *storedItems
    - int storedItems
    - SLLNode *next
Class methods:
    - SLLNode()
    - SLLNode(string item)
"""
class SLLNode:
    def __init__(self, storageName):
        self.storageName = storageName
        self.storedItems = []
        self.numStoredItems = 0
        self.next = None

    def appendItem(self, item:str):
        self.storedItems.append(item)
        self.numStoredItems = self.numStoredItems + 1
    
    def printStoredItems(self):
        print("Here are all the stored items: ")
        for item in self.storedItems:
            print(item)
    
    def removeItem(self, item: str):
        if item in self.storedItems:
            self.storedItems.remove(item)
            self.numStoredItems = self.numStoredItems - 1
            return 
        























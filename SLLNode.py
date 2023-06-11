
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
        print(self.storedItems[0])
        self.numStoredItems += 1
    
    def printStoredItems(self):
        for item in self.storedItems:
            print(item)
    























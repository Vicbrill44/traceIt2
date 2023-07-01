
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
    def __init__(self, storageName, storedItems=None):
        self.storageName = storageName
        if storedItems is None:
            self.storedItems = []
            self.numStoredItems = 0
        else:
            self.storedItems = storedItems
            self.numStoredItems = len(storedItems)
                    
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
    
    # new shit 
           
    def to_dict(self):
        node_dict = {
            'Storage Name': self.storageName,
            'Items': self.storedItems,
            #'next_node': self.next
        }

        if self.next:
            # Call the next node's to_dict method.
            next_dict = self.next.to_dict()
            
            # Combine the current dictionary with the next node's dictionary into a list.
            return [node_dict] + next_dict
        else:
            # If this is the last node in the list, return a list with just this node's dictionary.
            return [node_dict]
            
        
    @classmethod
    def from_dict(cls, data):
        if data is None:
            return None
        storage = data[0]
        node = cls(storage['Storage Name'], storage['Items'])
        node.next = cls.from_dict(data[1:]) if len(data) > 1 else None
        return node





















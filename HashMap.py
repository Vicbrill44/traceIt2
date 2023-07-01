from HashNode import HashNode

""" 
This is the HashMap Data structure which will contain:

Class Variables:
    - hashNode **map //a pointer to an array of pointers
    - numKeys: the number of keys
    - mapSize: total size of the hashMap
    - numCollisions: number of collisions using the collision-handling method
    - numHashColl: number of initial collisions using just the hash function

Class methods:
    - hashMap();    //constructor
    // maybe we have more addKeyValue methods 
    - addKeyValue(string k);  //basic add key and value to the 
    - addKeyValue(string k, string v);  //basic add key and value to the hashMap; add key room and value storage //an item will be added seperately
    - int getIndex(string k)    //get the index of the key in the hashMap
    - void getClosestPrime();   //get the closest prime to use for rehashing the hashMap
    - int calcHash1(string k);  // hash function
    - void reHash()     //will rehash the hashmp when the size of the array is 70%, double array size, and rehash keys
    - int coll1(int h, int i, string k);  // a probing method for collisions (when index is already full)
    - void printMap();  //I wrote this solely to check if everything was working.
"""

class HashMap:
    
    def __init__(self):
        self.mapSize = 7
        self.numKeys = 0     #number of rooms in the hashMap
        self.collFunCollisions = 0   #number of collisions caused by the collision handling function
        self.hashCollisions = 0 #number of collisions caused by the hash function
        
        self.map = [None] * self.mapSize
        
        
    def addKeyValue(self, key: str):
        """ The key is the room and the value is a storage"""
        # I think I should remove the ability to add a room and a storage at the same time 
        idx = self.getIndex(key)
        print(idx)
        if self.map[idx] == None:
            self.map[idx] = HashNode(key)
            self.numKeys = self.numKeys + 1
            print(f"{key} was successfully added")
        else:
            print(f"{key} already exist")
            return 
                
        #rehash if over 70% 
        load = int(((self.mapSize * 70) / 100))
        if self.numKeys >= load:
            print("rehashing")
            self.reHash()
        
        
    def getIndex(self, key:str, isReHashing:bool = False, newHash:int = 0) -> int:
        if not isReHashing:
            idx = self.calcHash(key)
            if self.map[idx] == None or self.map[idx].room == key:
                return idx
            else:
                # We have a collision
                self.hashCollisions += 1
                idx = self.collisonFunction(idx, key)
                return idx
        else:
            idx = self.calcHash(key, newHash)
            return idx
            # we will figure out if we have a collision for the new hash in the reshashing method
            
            

    def calcHash(self, k: str, newHash:int = 0) -> int:
        if newHash == 0:
            stringSize = len(k)
            h = 0 
            prime = 11
            if stringSize == 1:
                h = ord(k[0]) % self.mapSize
            elif stringSize == 2:
                h = ((ord(k[0])) + (ord(k[1]) * prime)) % self.mapSize
            else:
                h = ((ord(k[0])) + (ord(k[1]) * prime) + (ord(k[2]) * (prime*prime))) % self.mapSize           
            
        else:
            stringSize = len(k)
            h = 0 
            prime = 11
            if stringSize == 1:
                h = ord(k[0]) % newHash
            elif stringSize == 2:
                h = ((ord(k[0])) + (ord(k[1]) * prime)) % newHash
            else:
                h = ((ord(k[0])) + (ord(k[1]) * prime) + (ord(k[2]) * (prime*prime))) % newHash
            
        return h
        
    def getClosePrime(self) -> int:
        primesList = [1, 61, 97, 131, 173, 211, 251, 293, 337, 379, 419, 457, 499, 541, 577,
			          619, 661, 701, 739, 773, 811, 853, 887, 929, 967, 1009, 1049, 1091, 1129,
			          1169, 1201, 1249, 1291, 1327, 1367, 1409, 1451, 1487, 1523, 1567, 1607,
			          1657, 1693, 1733, 1777, 1811, 1847, 1889, 1931, 1979, 2017, 2053, 2099,
			          2137, 2179, 2221, 2267, 2309, 2347, 2381, 2417, 2459, 2503, 2539, 2591,
			          2633, 2683, 2719, 2767, 2803, 2843, 2887, 2939, 2971, 3011, 3049, 3089,
			          3137, 3181, 3221, 3259, 3299, 3343, 3389, 3433, 3469, 3511, 3557, 3593,
			          3631, 3671, 3709, 3761, 3803, 3847, 3881, 3919, 3967, 4007, 4051, 4091,
			          4127, 4177, 4217, 4259, 4297, 4339, 4373, 4421, 4463, 4507, 4547, 4591,
			          4639, 4679, 4721, 4759, 4801, 4831, 4877, 4919, 4951]
        
        primeToFind = self.mapSize * 2
        primeListLength = len(primesList)
        low = 0
        high = primeListLength - 1
        mid = 0
        foundPrime = 0
        while low <= high:
            mid = int(low + (high - low) / 2)
            if primesList[mid] > primeToFind:
                foundPrime = mid
                high = mid - 1
            else:
                low = mid + 1
        foundPrime = primesList[foundPrime]
        return foundPrime
        
            
    def reHash(self):
         oldMapSize = self.mapSize
         newHashPrime = self.getClosePrime()
         newIdx = 0
         newMap = [None] * newHashPrime
         self.numKeys = 0   #set the numKeys back to zero
         i = 0
         while i < oldMapSize:
             currentHashNode = self.map[i]
             if currentHashNode is not None:
                 tempNode = currentHashNode
                 newIdx = self.getIndex(tempNode.room, True, newHashPrime)
                 #check for collisions
                 if newMap[newIdx] == None:
                    newMap[newIdx] = tempNode
                 else:
                    # We have a collision
                    newIdx = self.collisonFunction(newIdx, tempNode.room, True, newHashPrime, newMap)
                    newMap[newIdx] = tempNode
                 
                 self.numKeys = self.numKeys + 1
             
             i = i + 1
                 #we should also delete the node from the original 
        
         self.map = newMap
         self.mapSize = newHashPrime   
            
         

    def collisonFunction(self, idx: int, key:str, isReHashing:bool = False, newHash:int = 0, newMap = None) -> int:
        counter = 0
        probing = idx
        if not isReHashing:
            while self.map[probing] != None:
                if self.map[probing].room == key:
                    self.collFunCollisions += 1
                    break
                probing = (probing + int(pow(counter, counter))) % self.mapSize
                counter += 1
                if probing > self.mapSize:
                    probing = 0
                self.collFunCollisions += 1
        else:
            while newMap[probing] != None:
                if newMap[probing].room == key:
                    break
                probing = (probing + int(pow(counter, counter))) % newHash
                counter += 1
                if probing > newHash:
                    probing = 0
            
        return probing

    def insertItem(self, key:str, storage:str, item:str):
        idx = self.getIndex(key)
        if self.map[idx] is None:
            return print(f"{key} does not exist and so cannot insert {item}")
        else:
            self.map[idx].addItemtoStorage(storage, item)
            
    def printAllRooms(self):
        if self.numKeys == 0:
            print("There are no rooms")
            return 
        for node in self.map:
            if node is not None:
                print(node.room)
            
    def deleteRoom(self, key:str):
        # There is def a better way to do this, I just wanted to test out this way 
        # other way would be to get index of key first and then check if it exists and if so del it 
        if self.numKeys == 0:
            return print("There are no rooms to delete")
        for node in self.map:
            if node is not None:
                if node.room == key:
                    #be careful with this as it could be the cause of a bug when deleting a hashNode and setting map[] to none
                    idx = self.getIndex(key)
                    self.map[idx] = None
                    del node
                    self.numKeys = self.numKeys - 1
                    print(f"Successfully deleted {key}")
                    return
        print(f"Error: {key} does not exist")
        
        
    # New shit
    def to_dict(self):
        return {
            'map': [room.to_dict() for room in self.map if room is not None],
            'mapSize': self.mapSize,
            'numKeys': self.numKeys
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        for room in data['map']:
            key = HashNode.from_dict(room)
            instance.addKeyValue(key.room)  #issue when loading from json we essentially create a new room but dont bring with it its components
            # we are essentially overwriting the newly added key value because it was just a placeholder for the key variable we got which holds the full hashnode, the other was naked with only its room name and nothing else
            idx = instance.getIndex(key.room)
            instance.map[idx] = key
            
        instance.mapSize = data['mapSize']
        instance.numKeys = data['numKeys']
        return instance
        

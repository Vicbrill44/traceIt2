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
        self.mapSize = 61
        self.numKeys = 0     #number of rooms in the hashMap
        self.collFunCollisions = 0   #number of collisions caused by the collision handling function
        self.hashCollisions = 0 #number of collisions caused by the hash function
        
        self.map = [None] * self.mapSize
        
        
    def addKeyValue(self, key: str, value:str = None):
        """ The key is the room and the value is a storage"""
        idx = self.getIndex(key)
        if self.map[idx] == None:
            if value is None:
                self.map[idx] = HashNode(key)
            else:
                self.map[idx] = HashNode(key, value)
        
            self.numKeys += 1
        else:
            if value is None:
                return print(f"{key} already exist in the map")
            else:
                self.map[idx].addStorage(value)
        
        #rehash if over 70% 
        load = int(((self.mapSize * 70) / 100))
        if self.numKeys >= load:
            self.reHash()
        
        
    def getIndex(self, key:str) -> int:
        idx = self.calcHash(key)
        if self.map[idx] == None or self.map[idx].room == key:
            return idx
        else:
            # We have a collision
            self.hashCollisions += 1
            idx = self.collisonFunction(idx, key)
            return idx
            

    def calcHash(self, k: str) -> int:
        stringSize = len(k)
        h = 0 
        prime = 11
        if stringSize == 1:
            h = ord(k[0]) % self.mapSize
        elif stringSize == 2:
            h = ((ord(k[0])) + (ord(k[1]) * prime)) % self.mapSize
        else:
            h = ((ord(k[0])) + (ord(k[1]) * prime) + (ord(k[2]) * (prime*prime))) % self.mapSize           
        
        return h 

    def reHash(self):
        pass

    def collisonFunction(self, idx: int, key:str) -> int:
        counter = 0
        probing = idx
        while self.map[probing] != None:
            if self.map[probing].room == key:
                self.collFunCollisions += 1
                break
            probing = (probing + int(pow(counter, counter))) % self.mapSize
            counter += 1
            if probing > self.mapSize:
                probing = 0
            self.collFunCollisions += 1
        
        return probing

    def insertItem(self, key:str, storage:str, item:str):
        idx = self.getIndex(key)
        if self.map[idx] is None:
            return print(f"{key} does not exist and so cannot insert {item}")
        else:
            self.map[idx].addItemtoStorage(storage, item)
            
        
        
        
        
        
        
        
        
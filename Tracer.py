from HashMap import HashMap

""" 
A tracer will essentially be the program itself it will...
    - create the interface
    - create the hashmap 

Class variables:
    - HashMap *map  //The hashmap containing all of the rooms
    
Class methods:
    //constructors
    - tracer()
    - void interface()  //an interface that talks to the user
    - void addRoom()    //allow the user to add a room 
    - void removeRoom() //allow the user to remove a room
    - void performOperation() //allow the user to perform an operation on a room
    - void endProgram() //end the program
    - void printAllRooms() //print all the rooms
    
"""

""" 
Notes: 
    - we are not going to allow the user to intitiliaze a tracer with an item or storage, we will make them go through the interface
"""

class Tracer:
    
    def __init__(self):
        self.tracer = HashMap()
        self.interface()

    def interface(self):
        choice = 0
        #write code that checks first to see if the user already has a json file with content in it
        #if so then we can bypass this tutorial part and just go straight to the interface
        #we need to make sure that when we load the json file, it loads as a hashmap 
        #Also right off the bat we should dump all of the room names so the user can see them
        print("Welcome to TraceIt")
        tutorial_room = input("Lets start by creating a room. A room can be anything from a bedroom, living room, bathroom, garage, truck, etc.\nEnter the name of your first room:\n")
        tutorial_storage = input("Now that we we have a room, lets add a storage in that room. A storage can be a desk, vanity, folder, locker, etc.\nEnter the name of your storage:\n") 
        tutorial_item = input("Now that we have a room and a storage in that room, lets add an item in that storage. An item can be a pencil, check, pen, paper, etc.\nEnter the name of an item:\n")
        
        #code to add a room and a storage and an item       
        self.tracer.addKeyValue(tutorial_room, tutorial_storage)
        self.tracer.insertItem(tutorial_room, tutorial_storage, tutorial_item)
        self.tracer.map[self.tracer.getIndex(tutorial_room)].addStorage("shelf")
        self.tracer.map[self.tracer.getIndex(tutorial_room)].printStorages()
        print(self.tracer.map[self.tracer.getIndex(tutorial_room)].storages.first.next.storedItems[0] + " made it here")
        self.tracer.map[self.tracer.getIndex(tutorial_room)].addItemtoStorage("shelf", "pencil")
        self.tracer.addKeyValue("sebasRoom")
        self.tracer.map[self.tracer.getIndex("sebasRoom")].addStorage("wall hanger")
        self.tracer.map[self.tracer.getIndex("sebasRoom")].printStorages()
        
        """
        while(choice != 5):
            print("What would you like to do?")
            print("\t1. Create a new room")
            print("\t2. Perform an operation on a room")
            print("\t3. Delete a room")
            print("\t4. Show all rooms")
            print("\t5. Quit")
            choice = input("Enter: ")
            
            if choice == 1:
                #code
            elif choice == 2:
                #code
            elif choice == 3:
                #code
            elif choice == 4:
                #code
            elif choice == 5:
                break
            else:
                print("Invalid choice, try entering a valid choice.")
                
        """
                
                
                
                
                
            
                
                
                
    
        



















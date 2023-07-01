from HashMap import HashMap
import json

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
        self.tracer = self.load_data()          # new shit, old: HashMap()
        self.interface()

    def interface(self):
        choice = 0
        #write code that checks first to see if the user already has a json file with content in it
        #if so then we can bypass this tutorial part and just go straight to the interface
        #we need to make sure that when we load the json file, it loads as a hashmap 
        #Also right off the bat we should dump all of the room names so the user can see them
        # print("Welcome to TraceIt")
        # tutorial_room = input("Lets start by creating a room. A room can be anything from a bedroom, living room, bathroom, garage, truck, etc.\nEnter the name of your first room:\n")
        # tutorial_storage = input("Now that we we have a room, lets add a storage in that room. A storage can be a desk, vanity, folder, locker, etc.\nEnter the name of your storage:\n") 
        # tutorial_item = input("Now that we have a room and a storage in that room, lets add an item in that storage. An item can be a pencil, check, pen, paper, etc.\nEnter the name of an item:\n")
        # self.tracer.addKeyValue(tutorial_room, tutorial_storage)
        # self.tracer.insertItem(tutorial_room, tutorial_storage, tutorial_item)
        
        while(choice != "5"):
            print("What would you like to do?")
            print("\t1. Create a new room")
            print("\t2. Perform an operation on a room")
            print("\t3. Delete a room")
            print("\t4. Show all rooms")
            print("\t5. Quit")
            choice = input("Enter: ")
            
            
            if choice == "1":
                new_room = input("Enter the name of the room you want to add: ")
                self.tracer.addKeyValue(new_room)
                print("")
            elif choice == "2":
                self.performOperationRoom()
                print("")
            elif choice == "3":
                delete_room = input("Enter the name of the room you want to delete: ")
                self.tracer.deleteRoom(delete_room)
                print("")
            elif choice == "4":
                # Error here when we add a room, then delete it, then add it back, and then try to show all rooms 
                # it tells me that no rooms exist
                # pretty sure it comes from self.numKeys equalling 0 for some reason when it 
                # update: seems to be working now after changing self.numKeys -= 1 to explicit
                print("Here are all the current rooms:")
                self.tracer.printAllRooms()
                print("")
            elif choice == "5":
                print("")
                self.save_data()    #new shit
                print("GOODBYE!")
                break
            else:
                print("Invalid choice, try entering a valid choice.")
                print("")
            
    def performOperationRoom(self):
        print("Here are all the current rooms:")
        self.tracer.printAllRooms()
        room_name = input("Enter the name of the room you want to perform the operation on: ")
        idx = self.tracer.getIndex(room_name)   # get the index of the room for all purposes
        
        if self.tracer.map[idx] is None:
            print(f"Error: The room '{room_name}' does not exist.")
            return 
        while True:
            print(f"\nOperations for room '{room_name}':")
            print("1. Add a storage")
            print("2. Perform an operation on a storage")
            print("3. Remove a storage")
            print("4. Pop a storage (remove the most recently added storage in the room)")
            print("5. Show all storages")
            print("6. Done")
            print("")
            
            operation = input("Enter an operation: ")
            
            if operation == "1":
                storage = input("Please enter the name of the storage you want to add: ")
                self.tracer.map[idx].addStorage(storage)
            elif operation == "2":
                self.performOperationStorage(idx)
            elif operation == "3":
                storage = input("Please enter the name of the storage you want to remove: ")
                self.tracer.map[idx].storages.remove(storage)
            elif operation == "4":
                items = self.tracer.map[idx].delRecentlyAddedStorage()
                if items is None:
                    return
                print("Here are all the items from the deleted storage: ")
                for item in items:
                    print(f"{item}")
            elif operation == "5":
                self.tracer.map[idx].printStorages()
            elif operation == "6":
                break
            else:
                print(f"Error: Invalid operation '{operation}'")
                
                
                
    def performOperationStorage(self, idx:int):
        self.tracer.map[idx].storages.printList()   # print all the storages in the room
        storage_name = input("Enter the name of the storage you want to perform the operation on: ")
        strExist = self.tracer.map[idx].storages.findStorage(storage_name)
        if strExist == -1:
            print(f"Error: The storage '{storage_name}' does not exist")
            return
        
        while True:
            print(f"\nOperations for storage '{storage_name}':")
            print("1. Add an item")
            print("2. Remove item")
            print("3. show all items")
            print("4. Done")
            print("")
        
            operation = input("Enter an operation: ")
            
            if operation == "1":
                item = input("Enter the item you want to add: ")
                self.tracer.map[idx].storages.addItem(storage_name, item)
                print(f"Succesfully added the item: '{item}' to '{storage_name}'")
            elif operation == "2":
                item = input("Enter the item you want to remove: ")
                self.tracer.map[idx].storages.removeItemfromStorage(storage_name, item)
            elif operation == "3":
                self.tracer.map[idx].storages.printStorageItems(storage_name)
            elif operation == "4":
                break
            else:
                print(f"Error: Invalid operation '{operation}'")
        
    # new shit
        
    def load_data(self):
        try:
            with open('tracer_data.json', 'r') as f:
                data = json.load(f)
            print("Loaded data from file.")
            return HashMap.from_dict(data)
        except FileNotFoundError:
            print("No data file found, starting fresh.")
            return HashMap()

    def save_data(self):
        with open('tracer_data.json', 'w') as f:
            json.dump(self.tracer.to_dict(), f, indent=4)
        print("Saved data to file.")
                
            
                
                
                
    
        



















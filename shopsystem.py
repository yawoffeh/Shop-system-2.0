from database import Database

class Shopsystem(Database):
    def __init__(self):
        Database.__init__(self)
    def update(self, filename, new_arr):
        try:
            file = open(filename, "w")
            file.write(f"shops = {new_arr}" )
            file.close
            return "Done"
        except:
            return False

    def addshop(self):
        name = input("Please enter the shop name: ")
        id = input("Enter shopid number: ")
        specialties = input("Enter shop specialties: ")
        owner = input("Enter owner's name: ")
        Database().setitem(id, name, specialties, owner)
        self.update("data.py", self.arr)
        print("Done")

    def updatedetails(self):
        pass

    def removeshop(self):
        id = input("Please enter the shop id: ")
        print(Database().delitem(id))
        self.update("data.py", self.arr)

    def view_shop(self):
        id = input("Enter the shop Id: ")
        print(Database().getitem(id))

    def view_allshops(self):
        pass

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
        action = Database().setitem(id, name, specialties, owner)
        if (action):
            self.update("data.py", self.arr)
        else:
            print("Shop with same ID already exists")

    def updatedetails(self):
        try:
            id = input("Please enter shop id: \n")
            shop_details = Database().get(id)
            selection = int(input("What will you like to edit: \n"))
            if selection == 1:
                name = shop_details.pop(0)
                new_name = input("\nPlease enter the new name for the shop: \n")
                if new_name:
                    hash = Database().get_hash(id)
                    shop_details.insert(0, new_name)
                    self.arr[hash].append(shop_details)
                    self.update("data.py", self.arr)
                    print("Done!")
                else:
                    print("Invalid operation, Please make sure you entered a name")
            elif selection == 2:
                hash = Database().get_hash(id)
                det = shop_details.pop(1)
                new_det = input("Please enter shop administrator's name: \n")
                det["owner"] = new_det
                shop_details.append(det)
                self.arr[hash].append(shop_details)
                self.update("data.py", self.arr)
                print("Done!")

            elif selection == 3:
                hash = Database().get_hash(id)
                det = shop_details.pop(1)
                new_det = input("Please enter shop specialties: \n")
                det["specialties"] = new_det
                shop_details.append(det)
                self.arr[hash].append(shop_details)
                self.update("data.py", self.arr)
                print("Done!")
        except:
            print("Invalid operation")

    def removeshop(self):
        id = input("Please enter the shop id: ")
        print(Database().delitem(id))
        self.update("data.py", self.arr)

    def view_shop(self):
        id = input("Enter the shop Id: ")
        print(Database().getitem(id))

    def view_allshops(self):
        result = []
        for i in self.arr:
            if i:
                for x in i:
                    result.append(x[0])
        print(*result)

from data import shops
class Database:
    def __init__(self):
        self.arr = shops

    def get_hash(self, shopid):
        hash = 0
        for i in shopid:
            if i.isalpha():
                hash += ord(i)
            else:
                hash += int(i)
        return hash%len(self.arr)

    def setitem(self, shopid, shop_name, shop_specialties, owner_name):
        hash = self.get_hash(shopid)
        if self.arr[hash]:
            for j in self.arr[hash]:
                if j[1]["shopid"] == shopid:
                    print(shopid)
                    return False
        (self.arr[hash]).append([shop_name, {"shopid": shopid,"specialties": shop_specialties, "owner": owner_name}])
        return True

    def getitem(self, shopid):
        hash = self.get_hash(shopid)
        for j in self.arr[hash]:
            if j[1]["shopid"] == shopid:
                details = j
                format = f"""
                        Shop name------> {details[0]}
                        Owner's name --> {details[1]["owner"]}
                        Shop specialties ---> {details[1]["specialties"]}
                        """
                return format
        return "Invalid shop id"

    def delitem(self, shopid):
        hash = self.get_hash(shopid)
        for i, j in enumerate(self.arr[hash]):
            if j[1]["shopid"] == shopid:
                self.arr[hash].pop(i)
                return "Done"
        return "Invalid shopid"

    def get(self, shopid):
        hash = self.get_hash(shopid)
        details = ""
        for i, j in enumerate(self.arr[hash]):
            if j[1]["shopid"] == shopid:
                details = self.arr[hash].pop(i)
        if details:
            return details
        else:
            return None

# Shop-system-2.0

A simple program where a large shop or supermarket or mall manager can keep track of all the shops currently working in the supermarket or mall

# Storage

[1] All shops are given a unique shopid which the manager can use to get access to the shop details

[2] The manager can store more shop details as time goes on and can also remove shops details

[3] shop details can also be edited by the manager as time goes on



## Database

The shops are stored using hash tables

The address of the shop in the database is calculated when you provide the shopid

```python
def get_hash(self, shopid):
    hash = 0
    for i in shopid:
        if i.isalpha():
            hash += ord(i)
        else:
            hash += int(i)
    return hash%len(self.arr)
```


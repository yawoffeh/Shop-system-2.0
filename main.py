from shopsystem import Shopsystem
options = """
[1]-- View all shops
[2]-- Add a new shop details
[3]-- Modify an existing shop's details
[4]-- Get a shop's details
[5]-- Remove a shop
"""
def main():
    user = Shopsystem()
    print(options)
    selection = int(input())
    if selection == 1:
        user.view_allshops()
    if selection == 2:
        user.addshop()
    if selection == 3:
        user.updatedetails()
    if selection == 4:
        user.view_shop()
    if selection == 5:
        user.removeshop()



if __name__ == "__main__":
    main()

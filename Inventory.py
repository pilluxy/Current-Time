from termcolor import colored

#Create a new list
inventory = []

#Add items to the list
inventory.append("torch")
inventory.append("gold coin")
inventory.append("key")
inventory.append("pick axe")

#Showing the inventor before dropping an item
for counter in range (len(inventory)):
    print(inventory[counter])

#Asking the user to select an item
item_drop = input("Type item to drop: ")

#Dropping items
if item_drop == ("gold coin"):
    inventory.remove("gold coin")
    print(colored("gold coin dropped!", "cyan"))

if item_drop == ("torch"):
    inventory.remove("torch")
    print(colored("torch dropped!", "cyan"))

if item_drop == ("key"):
    inventory.remove("key")
    print(colored("key dropped!", "cyan"))

if item_drop == ("pick axe"):
    inventory.remove("pick axe")
    print(colored("pick axe dropped!", "cyan"))

#Sort the items into alphabetical order
inventory.sort()

#Output all the items in the list after dropping an item
for counter in range (len(inventory)):
    print(inventory[counter])



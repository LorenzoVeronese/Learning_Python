'''Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary 
representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like 
dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. 
Note that the addedItems list can contain multiples of the same item.'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    total = 0
    print('Inventory:')
    for item in inventory.items():
        total = total+int(item[1])
        print(int(item[1]), end=' ')
        print(str(item[0]))
    print('Total number of items:', end=' ')
    print(total)

#I use len(added): this function gets the number of elements contained in the list (so I can generalize to other 
# loots rather than only the dragon's one)
def add_to_inventory(inventory, added):
    for i in range(len(added)):
        if str(added[i]) in inventory.keys():
            inventory[str(added[i])]+=1
        else:
            inventory[str(added[i])]=1

add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)

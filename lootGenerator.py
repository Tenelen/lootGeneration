#A complex loot generator
#secondary test
"""
We want to create a function that will roll a 1-6 number of mods on an item,
it will then roll from a pool of pre-existing mods
and for each of the mods we want the function to roll a number for how much
that item adds of that certain mod.
For example: If we roll Life as one of our mods, we want it to roll 1-99
for how much life that item gives.
"""
import random

#Start with a simple idea: Roll for number of mods (1-6)

#For now we're going to make all item types the same generator



class LootGeneration():
    def __init__(self, name, givenRarity='default'):
        self.equipped = False
        self.givenRarity = givenRarity
        self.realRarity = ''
        self.name = name
        self.baseMods = 1
        self.maxMods = 1
        self.numOfMods = 0

        self.rarityChart = ['normal', 'magic', 'rare', 'legendary']

        self.mod_pool = {
        "max life": random.randint(1,99),
        "physical damage": random.randint(1,30),
        "cold damage": random.randint(1,30),
        "lightning damage": random.randint(1,30),
        "fire damage": random.randint(1,30),
        "fire resistance": random.randint(1,30),
        "max mana": random.randint(1,99),
        "chaos resistance": random.randint(1,20),
        "physical resistance": random.randint(1,30),
        "ice resistance": random.randint(1,30),
        "light resistance": random.randint(1,30),
        }

        #Rolls the number of modifiers that the loot will have (1-6)
    def roll_mods(self):
        if self.givenRarity == 'default':
            self.realRarity = (random.sample(self.rarityChart, 1))[0]
        else:
            self.realRarity = self.givenRarity

        if self.realRarity == 'normal':
            self.baseMods = 1
            self.maxMods = 1
        elif self.realRarity == 'magic':
            self.baseMods = 1
            self.maxMods = 2
        elif self.realRarity == 'rare':
            self.baseMods = 2
            self.maxMods = 4
        elif self.realRarity == 'legendary':
            self.baseMods = 4
            self.maxMods = 6
        self.numOfMods = random.randint(self.baseMods, self.maxMods)

        #Picks the mods from the mod_pool based on the number of mods found above
        #puts them into a list based on the Key from Mod_Pool
        #
    def pick_mods(self):
        self.potentialMods = []
        self.pickedMods = []
        #Takes the keys from the Mod_pool dictionary and turns them into a list of
        #potential mods
        for key in self.mod_pool:
            self.potentialMods.append(key)

        #samples from the list of potential mods, and picks out (numOfMods) unique
        #values and adds them to the pickMods list
        self.pickedMods = (random.sample(self.potentialMods, self.numOfMods))

        #takes the keys from the pickedMods list, compares them to
        #the values established in the mod_pool and
        #sorts the mods into a format that's better for the player
    def sort_mods(self):
        self.createdItemData = {}
        self.formatted_mods = ''
        #takes items from the pickedMods and adds them to a dictionary of
        #the item data based on the key pMod and the value that relates from mod_pool
        for pMod in self.pickedMods:
            self.createdItemData.update({pMod:self.mod_pool[pMod]})
        #formats the mod into a "+ NUM to STAT format"
        for mod in self.createdItemData:
            self.formatted_mods += "+" + str(self.createdItemData[mod]) + " To " + str(mod).title() + '\n'

        #global_mods = self.createdItemData

    def print_item_entirity(self):
        #Prints a complete format for the item (name, num of mods, rarity, mods )
        #Optional debug for createdItemData dictionary to print here as well
        print ('\n' + self.name.title())
        print("Number of Mods: " + str(self.numOfMods))
        print(self.realRarity.title())
        #print(self.createdItemData)
        print(self.formatted_mods)
        print("\n")

    def equip_item(self):
        #checks in the item is equipped, for future purposes
        self.equipped = True
        print(self.equipped)

    #def add_itemStats_to_player(self)

    def create_item(self):
        self.roll_mods()
        self.pick_mods()
        self.sort_mods()

        #self.print_item_entirity()

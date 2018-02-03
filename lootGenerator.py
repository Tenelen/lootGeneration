#A complex loot generator
#laksdjfasdfk
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
    def __init__(self, name, rarity='normal'):
        self.rarity = rarity
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
        self.rarity = (random.sample(self.rarityChart, 1))[0]
        if self.rarity == 'normal':
            self.maxMods = 1
        elif self.rarity == 'magic':
            self.maxMods = 2
        elif self.rarity == 'rare':
            self.baseMods = 2
            self.maxMods = 4
        elif self.rarity == 'legendary':
            self.baseMods = 4
            self.maxMods = 6
        self.numOfMods = random.randint(self.baseMods, self.maxMods)
        print ('\n' + self.name.title())
        """print (str(self.numOfMods) + " Mod(s)")"""

        #Picks the mods from the mod_pool based on the number of mods found above
        #puts them into a list based on the Key from Mod_Pool
        #
    def pick_mods(self):
        self.pickedMods = []
        self.potentialMods = []
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
        for pickedMod in self.pickedMods:
            formatted_mod = "+" + str(self.mod_pool[pickedMod]) + " To " + str(pickedMod).title()
            print(formatted_mod)

    def create_item(self):
        self.roll_mods()
        self.pick_mods()
        self.sort_mods()

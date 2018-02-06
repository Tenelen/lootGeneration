"""File name doesn't accurately display what's happening here. This is
actually both the character genration test area, as well as a stat field for
testing the players base stats.
We can also equip items here to test out the players stats with those as an addition"""

import item_roller
class PlayerCharacter():
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.life = 10
        self.playerDamage = 1
        self.equippedDamage = item_roller.damage
        self.totalDamage = self.playerDamage + self.equippedDamage
        self.playerStats = {
        'player damage': self.playerDamage,
        'life': self.life + level,
        }

    def playerStatChart(self):
        print(self.name.title())
        print('Level: ' + str(self.level))
        for stat in self.playerStats:
            print (str(stat).title() + ': ' + str(self.playerStats[stat]).title())
        print("Total Damage: " + str(self.totalDamage))

    def levelUp(self):
        self.level += 1
        self.playerStatChart()

scrub = PlayerCharacter('Scrub')
scrub.playerStatChart()

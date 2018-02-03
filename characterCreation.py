class PlayerCharacter():
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.life = 10
        self.playerStats = {
        'damage': 1,
        'life': self.life + level,
        }

    def playerStatChart(self):
        print(self.name.title())
        print('Level: ' + str(self.level))
        for stat in self.playerStats:
            print (str(stat).title() + ': ' + str(self.playerStats[stat]).title())

    def levelUp(self):
        self.level += 1
        self.playerStatChart()

scrub = PlayerCharacter('Scrub')
scrub.playerStatChart()
scrub.levelUp()
scrub.playerStatChart()

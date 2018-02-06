from lootGenerator import LootGeneration

star_destroyer = LootGeneration('star destroyer', givenRarity='legendary')
rusted_dagger = LootGeneration('rusted dagger', givenRarity='legendary')

equipped_items = []

rusted_dagger.equip_item()


if rusted_dagger.equipped == True:
    equipped_items.append(rusted_dagger)

print(equipped_items)

rusted_dagger.create_item()
#print(rusted_dagger.name)
#print(rusted_dagger.createdItemData)


damage = 0
"""print(damage)

if rusted_dagger.equipped == True:
    for key in rusted_dagger.createdItemData:
        if key == "physical damage":
            damage += rusted_dagger.createdItemData[key]
        elif key == "cold damage":
            damage += rusted_dagger.createdItemData[key]
        elif key == "lightning damage":
            damage += rusted_dagger.createdItemData[key]
        elif key == "fire damage":
            damage += rusted_dagger.createdItemData[key]
else:
    print("This item is not equipped.")
print(damage)
"""

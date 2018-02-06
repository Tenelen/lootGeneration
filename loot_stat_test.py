import random
"""
mod_pool = {
"life": random.randint(1,99),
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
"""

mod_pool = ['life', 'damage', 'cold res', 'fire res', 'chaos res', 'lightning res']
life = 10
damage = 1
cold_res = 0
chaos_res = 0
lightning_res = 0
fire_res = 0

lifeRoll = random.randint(1,99)
damageRoll = random.randint(1,99)
fireResRoll = random.randint(1,99)
coldResRoll = random.randint(1,99)
chaosResRoll = random.randint(1,99)
lightningResRoll = random.randint(1,99)

pickedMods = []
pickedMods = random.sample(mod_pool, 3)

for mod in pickedMods:
    if mod == 'life':
        life +=lifeRoll
    elif mod == 'damage':
        damage +=damageRoll
    elif mod == 'cold res':
        cold_res += coldResRoll
    elif mod == 'fire res':
        fire_res += fireResRoll
    elif mod == 'chaos res':
        chaos_res += chaosResRoll
    elif mod == 'lightning res':
        lightning_res += lightningResRoll
    else:
        print("You hacked the system. Reported.")


print (pickedMods)
print(lifeRoll)
print("Life: " + str(life))
print("Damage: " + str(damage))
print("Cold Res: " + str(cold_res))
print("Fire Res: " + str(fire_res))
print("Chaos Res: " + str(chaos_res))
print("Lightning Res: " + str(lightning_res))

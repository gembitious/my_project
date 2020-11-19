import json

# moveKor = {}
# pokeKor = {}
data = {}
# with open("../data/moveKor.json", "r", encoding='utf-8') as f:
    # moveKor = json.load(f)
with open("../data/pokeKor.json", "r", encoding='utf-8') as f:
    pokeKor = json.load(f)
with open("../data/gamemaster.json", "r", encoding='utf-8') as f:
    data = json.load(f)
# print(moveKor)
# print(pokeKor)
# print(data)

for poke in data["pokemon"]:
    if "tags" in poke:
        if "shadow" in poke["tags"]:
            poke["speciesNameKor"] += "(그림자)"
        if "alolan" in poke["tags"]:
            poke["speciesNameKor"] += "(알로라)"
        if "galarian" in poke["tags"]:
            poke["speciesNameKor"] += "(가라르)"
    # poke["speciesNameKor"] = pokeKor[poke["dex"]-1]["speciesNameKor"]

# for move in data["moves"]:
#     # for m in moveKor:
#         # if m["name"] == move["name"]:
#             # move["nameKor"] = m["nameKor"]
#     type = ""
#     power = 0
#     energy = 0
#     energygain = 0
#     buffs = []
#     bufftarget = ""
#     buffapplychance = ""
#     ctype = False
#     cpower = False
#     cenergy = False
#     cenergygain = False
#     cbuffs = False
#     cbufftarget = False
#     cbuffapplychance = False
#     if "cooldown" in move:
#         del move["cooldown"]
#     if "type" in move:
#         type = move["type"]
#         del move["type"]
#         ctype = True
#     if "power" in move:
#         power = move["power"]
#         del move["power"]
#         cpower = True
#     if "energy" in move:
#         energy = move["energy"]
#         del move["energy"]
#         cenergy = True
#     if "energyGain" in move:
#         energygain = move["energyGain"]
#         del move["energyGain"]
#         cenergygain = True
#     if "buffs" in move:
#         buffs = move["buffs"]
#         del move["buffs"]
#         cbuffs = True
#     if "buffTarget" in move:
#         bufftarget = move["buffTarget"]
#         del move["buffTarget"]
#         cbufftarget = True
#     if "buffApplyChance" in move:
#         buffapplychance = move["buffApplyChance"]
#         del move["buffApplyChance"]
#         cbuffapplychance = True
#     if ctype:
#         move["type"] = type
#     if cpower:
#         move["power"] = power
#     if cenergy:
#         move["energy"] = energy
#     if cenergygain:
#         move["energyGain"] = energygain
#     if cbuffs:
#         move["buffs"] = buffs
#     if cbufftarget:
#         move["buffTarget"] = bufftarget
#     if cbuffapplychance:
#         move["buffApplyChance"] = buffapplychance


# print(data)

with open("../data/gamemaster.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent="\t", ensure_ascii=False)
equipa = {}
equipa['luis'] = 'manel'
print(equipa)
equipa['rosa'] = 'mota'
print(equipa)
print("manel" in equipa)
print(equipa.keys())
print(list(equipa.keys()))
print(tuple(equipa.keys()))
print(equipa.values())
equipa["maria"] = "joao"
for key in equipa.keys():
    print(key) #prints keys
print("------------------")
for key in equipa.keys():
    print(equipa[key]) #prints values
print("------------------")
print(equipa.items())
for key in equipa.items():
    print(key)
for key,value in equipa.items():
    print(key,"->", value)

equipa2 = equipa #works like pointer
equipa2['luis'] = 'malmequer'
print(equipa2)
print(equipa)

equipa2 = equipa.copy() #copy only key and values
equipa2['luis'] = 'cyoz'
print(equipa2)
print(equipa)
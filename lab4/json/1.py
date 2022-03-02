import json

with open("sample-data.json", "r") as json_file:
    a = json_file.read()
data = json.loads(a)


print('Interface Status')
print('=====================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')

# print(type(data))

# print(len(data['imdata']))   #list

for i in range(3):
    print(data['imdata'][i]['l1PhysIf']['attributes']['dn'], end='                              ')
    print(data['imdata'][i]['l1PhysIf']['attributes']['speed'], end='   ')
    print(data['imdata'][i]['l1PhysIf']['attributes']['mtu'])
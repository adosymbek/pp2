import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<10}{:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data['imdata']:
    dn = interface['topSystem']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '9150')
    print("{:<50}{:<20}{:<10}{:<10}".format(dn, description, speed, mtu))

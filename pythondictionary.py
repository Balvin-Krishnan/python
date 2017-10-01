import random
import sys
import os

super_villians = {"Fiddler":"Issac", "captain Cold": 'Leo', 'Weather wiz':'Mark'}

print(super_villians['captain Cold'])
#print(s)

print()

del super_villians['Fiddler']

super_villians['Piped pepper'] = 'Hartley'

print(len(super_villians))

print(super_villians.get('Piped pepper'))

print(super_villians.keys());

print(super_villians.values())
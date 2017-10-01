import random
import sys
import os

grocery_list = ['Juince', 'Tomato', 'Potatos']

print("First Item ", grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick up kids', 'Cash Check']

to_do_list = [grocery_list, other_events]

print(to_do_list)

print(to_do_list[1][1])

grocery_list.append('Onion')

print(to_do_list)

grocery_list.remove('Tomato')

print(to_do_list)

to_do_list2 = other_events+grocery_list
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
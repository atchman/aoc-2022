# day 03

import os
import string


REL_PATH = os.path.relpath('../input/03', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

LOWERCASE_VALUE = dict((x,y) for y, x in enumerate(string.ascii_lowercase, start=1))
UPPERCASE_VALUE = dict((x, y) for y, x in enumerate(string.ascii_uppercase, start=27))

def main():
    char_value = []
    
    with open(PATH, 'r') as FILE:
        for line in FILE:
            rucksack_one, rucksack_two = split_rucksack(line.strip())
            same_char = appear_in_both(rucksack_one, rucksack_two)
            char_value.append(get_char_value(same_char))
            
            print(rucksack_one)
            print(rucksack_two)
            
    print(char_value)
    print(sum(char_value))
        

def split_rucksack(whole):
    whole_half = int(len(whole) / 2)
    part_one = whole[:whole_half]
    part_two = whole[whole_half:]
    return part_one, part_two


def appear_in_both(rucksack_one, rucksack_two):
    for i in rucksack_one:
        for j in rucksack_two:
            if i == j:
                appear = i
                break
    return appear


def get_char_value(char):
    lower = LOWERCASE_VALUE.get(char, -1)
    upper = UPPERCASE_VALUE.get(char, -1)
    if lower > 0:
        return lower
    if upper > 0:
        return upper
    
  
if __name__ == '__main__':
    main()
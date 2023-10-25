# day 03

import os
import string


REL_PATH = os.path.relpath('../input/03', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

LOWERCASE_VALUE = dict((x,y) for y, x in enumerate(string.ascii_lowercase, start=1))
UPPERCASE_VALUE = dict((x, y) for y, x in enumerate(string.ascii_uppercase, start=27))

def main():
    char_value_one = []
    char_value_two = []
    line_num = 0
    group = ['','','']
    with open(PATH, 'r') as FILE:
        for line in FILE:
            rucksack_one, rucksack_two = split_rucksack(line.strip())
            same_char = appear_in_both(rucksack_one, rucksack_two)
            char_value_one.append(get_char_value(same_char))
            
            if line_num < 3:
                group[line_num] = line.strip()
                line_num +=1
            else:
                group_char = appear_in_group(group)
                char_value_two.append(get_char_value(group_char))
                group[0] = line.strip()
                line_num = 1
        else:
            group_char = appear_in_group(group)
            char_value_two.append(get_char_value(group_char))
                       
            
    print(char_value_one)
    print(sum(char_value_one))
    print(char_value_two)
    print(sum(char_value_two))
        

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
    
    
def appear_in_group(group):
    line_one = group[0]
    line_two = group[1] 
    line_three = group[2]
    for i in line_one:
        for j in line_two:
            for k in line_three:
                if i == j and j == k:
                    appear = i
                    break
    return appear
    
  
if __name__ == '__main__':
    main()
# day 02

import os


REL_PATH = os.path.relpath('../input/02', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

def main():
    global score_part_one
    global score_part_two
    score_part_one = []
    score_part_two = [] 
    
    with open(PATH, 'r') as FILE:
        for line in FILE:
            player,me = line.strip().split(' ')
            part_one(player, me)
            part_two(player, me)
     
    print(score_part_one)
    print(sum(score_part_one))
    print(score_part_two)
    print(sum(score_part_two))      
            
def part_one(player, myanswer):
    match myanswer:
        case 'X':
            score_part_one.append(1 + round_outcome(player, 'A'))
        case 'Y':
            score_part_one.append(2 + round_outcome(player, 'B'))
        case 'Z':
            score_part_one.append(3 + round_outcome(player, 'C'))
        case _:
            print('ERROR')
    
            
def round_outcome(player, myanswer):
    if player == myanswer:
        return_value = 3
    else:
        if player == 'A' and myanswer == 'B':
            return_value = 6
        elif player == 'B' and myanswer == 'C':
            return_value = 6
        elif player == 'C' and myanswer == 'A':
            return_value = 6
        else:
            return_value = 0
    return return_value


def part_two(player, myanswer):
    match myanswer:
        case 'X':
            score_part_two.append(0)
            match player:
                case 'A':
                    score_part_two.append(3)
                case 'B':
                    score_part_two.append(1)
                case 'C':
                    score_part_two.append(2)               
        case 'Y':
            score_part_two.append(3)
            match player:
                case 'A':
                    score_part_two.append(1)
                case 'B':
                    score_part_two.append(2)
                case 'C':
                    score_part_two.append(3)    
        case 'Z':
            score_part_two.append(6)
            match player:
                case 'A':
                    score_part_two.append(2)
                case 'B':
                    score_part_two.append(3)
                case 'C':
                    score_part_two.append(1)    
        case _:
            print('ERROR')
        
     
if __name__ == '__main__':
    main()
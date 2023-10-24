# day {{ num }}

import os


REL_PATH = os.path.relpath('../input/02-sample', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

def main():
    score = []
    
    with open(PATH, 'r') as FILE:
        for line in FILE:
            player,myanswer = line.strip().split(' ')
            
            match myanswer:
                case 'X':
                    score.append(1 + round_outcome(player, 'A'))
                case 'Y':
                    score.append(2 + round_outcome(player, 'B'))
                case 'Z':
                    score.append( 3 + round_outcome(player, 'C'))
                case _:
                    print('ERROR')
    print(score)
    print(sum(score))
        
                 
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
        
        
if __name__ == '__main__':
    main()
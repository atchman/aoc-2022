# day 1

import os


REL_PATH = os.path.relpath('../input/01', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    elf = 0
    food = 0
    global total_food
    total_food = [0,0,0]
    
    with open(PATH, 'r') as FILE:
        x = 0
        for line in FILE:
            line = line.strip()
            if line == '':
                elf += 1
                check_food(food)
                food= 0
            else:
                food = food + int(line)
            x+=1
        else:
            check_food(food)
            
    print(total_food)
    print(sum(total_food))
         
            
def check_food(food):
    if food > total_food[0]:
        total_food[2] = total_food[1]
        total_food[1] = total_food[0]
        total_food[0] = food
    elif food < total_food[0] and food > total_food[1]:
        total_food[2] = total_food[1]
        total_food[1] = food
    elif food > total_food[2]:
        total_food[2] = food
        
           
if __name__ == '__main__':
    main()
    
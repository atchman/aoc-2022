# day 03

import os


REL_PATH = os.path.relpath('../input/03-sample', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

def main():
    with open(PATH, 'r') as FILE:
        for line in FILE:
            print(line.strip())
        
    
    
    
    
if __name__ == '__main__':
    main()
def adv2_1(instrs):
    keypad = [ [1,2,3], [4,5,6], [7,8,9] ]
    pos_x, pos_y = 1 , 1
    nums = []
    for instr in instrs:
        for key in instr:
            if key == 'L':
                pos_y = max(0, pos_y - 1)
            elif key == 'R':
                pos_y = min(2, pos_y + 1)
            elif key == 'U':
                pos_x = max(0, pos_x - 1)
            else:
                pos_x = min(2, pos_x + 1)
        nums.append( keypad[pos_x][pos_y] )
    return nums

def min_for(x):
    if x == 0 or x == 4:
        return 2
    if x == 1 or x == 3:
        return 1
    return 0

def max_for(x):
    if x == 0 or x == 4:
        return 2
    if x == 1 or x == 3:
        return 3
    return 4

def adv2_2(instrs):
    keypad = [
        [None, None, 1, None, None] ,
        [None, 2   , 3, 4   , None] ,
        [5   , 6   , 7, 8   , 9   ] ,
        [None, 'A' , 'B' , 'C', None ] ,
        [None, None, 'D', None, None]
    ]
    pos_x, pos_y = 2 , 0
    nums = []
    for instr in instrs:
        for key in instr:
            if key == 'L':
                pos_y = max(min_for(pos_x), pos_y - 1)
            elif key == 'R':
                pos_y = min(max_for(pos_x), pos_y + 1)
            elif key == 'U':
                pos_x = max(min_for(pos_y), pos_x - 1)
            else:
                pos_x = min(max_for(pos_y), pos_x + 1)
        nums.append( keypad[pos_x][pos_y] )
    return nums

def read_file(path):
    with open(path, 'r') as file:
        instrs = [ line.strip() for line in file.readlines() ]
        return adv2_2(instrs)

instrs = ["ULL",
"RRDDD",
"LURDL",
"UUUUD"]

read_file("input2.txt")

#adv2_2(instrs)
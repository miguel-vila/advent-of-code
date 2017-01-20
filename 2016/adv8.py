def rect(cols, rows, screen):
    for i in range(0, rows):
        for j in range(0, cols):
            screen[i][j] = True

def rotate_row(row, n, screen):
    row_copy = [ state for state in screen[row] ]
    for j in range(len(row_copy)):
        screen[row][j] = row_copy[(j - n)%len(row_copy)]
        
def rotate_col(col, n, screen):
    col_copy = [ row[col] for row in screen ]
    for i in range(len(col_copy)):
        #print "{} -> {}".format(i, (i + n)%len(col_copy))
        screen[i][col] = col_copy[(i - n)%len(col_copy)]
        
def count_on(screen):
    return sum(map(sum,screen))

def execute(command, screen):
    parts = command.split()
    if parts[0] == 'rect':
        parts2 = parts[1].split("x")
        [cols,rows] = map(int, parts2)
        rect(cols,rows,screen)
    elif parts[1] == 'row':
        n = int(parts[-1])
        row = int(parts[2].split('=')[1])
        rotate_row(row, n, screen)
    elif parts[1] == 'column':
        n = int(parts[-1])
        col = int(parts[2].split('=')[1])
        rotate_col(col, n, screen)
    else:
        raise Error("unrecognized {}".format(command))
        
def part1():
    rows = 6
    cols = 50
    screen = [[False for j in range(cols)] for i in range(rows)]
    with open('input8.txt', 'r') as file_h:
        for command in file_h.readlines():
            execute(command, screen)
        print count_on(screen)
    print_screen(screen)

def print_screen(screen):
    print "\n".join(map(lambda row: "".join(map(lambda b: '#' if b else '.', row)), screen))
    
part1()

rows = 3
cols = 7

screen = [[False for j in range(cols)] for i in range(rows)]

print "-----"

rect(3,2,screen)
print_screen(screen)
print "-----"

rotate_col(1,1, screen)
print_screen(screen)
print "-----"

rotate_row(0,4, screen)
print_screen(screen)
print "-----"

rotate_col(1,1, screen)
print_screen(screen)
print "-----"

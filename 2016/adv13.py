from collections import deque

puzzle_input = 1350
#puzzle_input = 10

def is_open(y,x):
    n = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    ones = 0
    while n >= 2:
        if n%2 != 0:
            ones += 1
        n /= 2
    ones += n
    return ones % 2 == 0

def to_char(x,y):
    return '.' if is_open(x,y) else '#'

def print_board(n,m):
    for i in range(n):
        print "".join([ to_char(i,j) for j in range(m)])

def neighbours(y0,x0):
    possible = [ (y0+dy,x0+dx) for dy,dx in [(0,-1),(-1,0),(1,0),(0,1)] ]
    valid_ones = [ (y,x) for y,x in possible if y >= 0 and x >= 0 and is_open(y,x) ]
    return valid_ones

print neighbours(1,1)

q = deque()
target = (39,31)
source = (1,1)

q.append(source)
dist = dict()
dist[source] = 0
visited = set()

while len(q)>0:
    y,x = q.popleft()
    #print "visiting {}".format((y,x))
    if (y,x) == target:
        print "found in {} steps!".format(dist[target])
        #break
    if (y,x) in visited:
        continue
    visited.add((y,x))
    for n in neighbours(y,x):
        if n not in visited:
            q.append(n)
            dist[n] = dist[(y,x)] + 1

print len(filter(lambda d: d <= 50, dist.values()))

class Disk:

    def __init__(self, disk_number, positions, initial_position):
        self.disk_number = disk_number
        self.positions = positions
        self.initial_position = initial_position

    def position_at(self, offset_time):
        return (self.disk_number + offset_time + self.initial_position) % self.positions

    def open_at(self, offset_time):
        return self.position_at(offset_time) == 0

d1 = Disk(1, 5, 4)
d2 = Disk(2, 2, 1)

def all_open(offset, disks):
    for disk in disks:
        if not disk.open_at(offset):
            return False
    return True

def all_open_at(disks):
    i = 0
    while not all_open(i, disks):
        i += 1
    return i

print(all_open_at([d1, d2]))

def parse_disk(disk_str):
    parts = disk_str.split()
    disk_number = int(parts[1][1:])
    positions = int(parts[3])
    initial_position = int(parts[-1][:-1])
    return Disk(disk_number, positions, initial_position)

# part 1
with open('input15.txt', 'r') as f_handle:
    disks1 = [ parse_disk(line) for line in f_handle.readlines() ]
print(all_open_at(disks1))

#part 2

new_disks = disks1 + [Disk(disks1[-1].disk_number+1, 11, 0)]
print(len(disks1))
print(len(new_disks))
print(all_open_at(new_disks))

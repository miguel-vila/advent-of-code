def valid(s1, s2, s3):
    return s1 + s2 > s3

def is_triangle(sides):
    return all([
        valid(sides[0],sides[1],sides[2]),
        valid(sides[1],sides[2],sides[0]),
        valid(sides[2],sides[0],sides[1]),
    ])

# part 1
#if __name__ == "__main__":
#    with open('input3.txt','r') as file_handle:
#        splitted = [line.split() for line in file_handle.readlines() ]
#        print splitted
#        nums = [map(int, nums) for nums in splitted ]
#        total = 0
#        for sides in nums:
#            print sides
#            if is_triangle(sides):
#                total += 1
#                print "Triangle!"
#            else:
#                print "Not triangle!"
#        print total

# part 2
if __name__ == "__main__":
    with open('input3.txt','r') as file_handle:
        splitted = [line.split() for line in file_handle.readlines() ]
        #print splitted
        nums = [map(int, nums) for nums in splitted ]
        total = 0
        for i in range(len(nums)/3):
            for k in range(3):
                total += 1 if is_triangle([ nums[i*3+j][k] for j in range(3) ]) else 0
        print total

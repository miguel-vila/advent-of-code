def decompress(s):
    i = 0
    decompressed = ""
    while i < len(s):
        #print "s[i] = {}".format(s[i])
        if s[i] == '(':
            j = i + 1
            while s[j] != ')':
                j += 1
            marker = s[i+1:j].split('x')
            #print "marker = {}".format(marker)
            #print "length = {}".format(length)
            [chars, times] = map(int, marker)
            decompressed += s[j+1:j+1+chars]*times
            i = j + chars + 1
            #print "i = {}".format(i)
        else:
            decompressed += s[i]
            i += 1
    #print length
    return decompressed

def dec_length(data):
    i = 0
    total = 0
    while i < len(data):
        #print "data[i] = {}".format(data[i])
        if data[i] == '(':
            i += 1
            marker = ""
            while data[i] != ')':
                marker += data[i]
                i += 1
            print "marker = {}".format(marker)
            #print "total = {}".format(total)
            [length, amount] = map(int, marker.split('x'))
            total += length*amount
            i += length
            #print "i = {}".format(i)
        else:
            total += 1
        i += 1
    #print total
    return total

assert dec_length("ADVENT") == 6
assert decompress("ADVENT") == "ADVENT"

assert dec_length("A(1x5)BC") == 7
assert decompress("A(1x5)BC") == "ABBBBBC"

assert dec_length("(3x3)XYZ") == 9
assert decompress("(3x3)XYZ") == "XYZXYZXYZ"

assert dec_length("A(2x2)BCD(2x2)EFG") == 11
assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"

assert dec_length("(6x1)(1x3)A") == 6
assert decompress("(6x1)(1x3)A") == "(1x3)A"

assert dec_length("X(8x2)(3x3)ABCY") == 18
assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"

assert dec_length("(1x14)I") == 14

assert dec_length("(12x5)XTXXAJCPTWYL(1x14)I") == (14+12*5)
assert dec_length("(9x4)BRUWUPCJY(12x5)XTXXAJCPTWYL(1x14)I") == (14+12*5+9*4)
assert dec_length("(39x2)(8x12)NJBFXFDD(5x14)ORZCE(9x4)BRUWUPCJY(12x5)XTXXAJCPTWYL(1x14)I") == (14+12*5+39*2)
assert dec_length("(70x1)(39x2)(8x12)NJBFXFDD(5x14)ORZCE(9x4)BRUWUPCJY(12x5)XTXXAJCPTWYL(1x14)I") == 70

print "passed!"

def decompressed_length(data):
    i = 0
    total = 0
    while i < len(data):
        if data[i] == '(':
            i += 1
            newstring = ""
            while data[i] != ')':
                newstring += data[i]
                i += 1
            length = int(newstring.split('x')[0])
            amount = int(newstring.split('x')[1])
            #total += amount*decompressed_length(data[i+1:i+length+1])
            total += amount*length 
            i += length
        else:
            total += 1
        i += 1
    return total

with open('input9.txt','r') as file_h:
    file_content = file_h.read()
    #print file_content
    print dec_length(file_content)
    print decompressed_length(file_content)
    print len(decompress(file_content))


import hashlib

puzzle_input = "ahsbgdzn"

def md5(str):
    return hashlib.md5(str).hexdigest()

def md5_2016(hash):
    hash_2016 = hash
    for _ in range(2016):
        hash_2016 = md5(hash_2016)
    return hash_2016

#hashes = [ md5(puzzle_input+str(i)) for i in range(31500) ]
hashes = [ md5_2016(md5(puzzle_input+str(i))) for i in range(31500) ]

def reps(hash):
    rep3_char = rep3(hash)
    rep5_chars = reps5s(hash)
    return (hash, rep3_char, rep5_chars)

def rep3(hash):
    for i in range(len(hash) - 3 + 1):
        part = hash[i:i+3]
        if all(map(lambda b: b == part[0], part)):
            return part[0]
    return None

def reps5s(hash):
    rep5s_chars = []
    for i in range(len(hash) - 5 + 1):
        part = hash[i:i+5]
        if all(map(lambda b: b == part[0], part)):
            rep5s_chars.append(part[0])
    return rep5s_chars

hashes_and_reps = map(reps, hashes)

def is_key(i):
    hash, rep3_char, _ = hashes_and_reps[i]
    if rep3_char is None:
        return False
    for j in range(i+1,min(i+1000+1, len(hashes))):
        _, _, rep5_chars = hashes_and_reps[j]
        if any(map(lambda c: c == rep3_char, rep5_chars)):
            #print "found!"
            return True
    return False

keys = []
i = 0

while len(keys) < 64:
    if is_key(i):
        keys.append(i)
    i += 1
print keys[-1]

print hashes[0]

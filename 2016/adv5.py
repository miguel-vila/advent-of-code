import hashlib

def password1(doorId):
    i = 0
    password = ""
    while len(password)<8:
        hash = hashlib.md5(doorId + str(i)).hexdigest()
        if hash.startswith("0"*5):
            print "found!"
            password = password + hash[5]
        i+=1
    return password

#password1("cxdnnyjw")

def password2(doorId):
    i = 0
    k = 0
    password = [None]*8
    while k < 8:
        hash = hashlib.md5(doorId + str(i)).hexdigest()
        if hash.startswith("0"*5) and '0' <= hash[5] <= '7':
            if password[int(hash[5])] is None:
                password[int(hash[5])] = hash[6]
                k += 1
        i+=1
    return "".join(password)

password2("cxdnnyjw")
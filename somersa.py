import hashlib

def modpow(b, e, m):  
    result = 1
    while (e > 0):
        if e & 1:
            result = (result * b) % m
        e = e >> 1
        b = (b * b) % m
    return result
	
def str_to_int(string):  
    n = 0
    for i in range(len(string)):
        n = n << 8
        n += ord(string[i])
    return n
	
	
def rsa(data, n):
    e = '10001'
    result = modpow(str_to_int(data), long(e, 16), long(n, 16))
    return hex(result)[2:-1]


n = '8f4be304d041801171659fbe7e4e3b490d680ff0fc23c18f41d56a5b8b4db90761b9ddfc688b4a7addee4b1553e3d3809e399a095511c32c85e9046acad7cf67'
print rsa("1140340116", n)
print rsa("xxxx", n)
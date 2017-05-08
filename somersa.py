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

# n = '98289d260169a74317dd3ad91b831623e5589a344848b0ccceb74542212fc2390a13d8f15b037c56eabf2a4ef7b1e06c32c9f6280288373ee23efc87d350056b'  
# print rsa("xxx", n)
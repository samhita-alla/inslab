import numpy as np
from numpy.linalg import inv
data = 'wopvzpuyujnorf'
key = np.array([[2,3],[5,7]])

# inverse the key
invkey = inv(key).astype('int') # converting to int since inv will return float

# convert cipher text to numbers
cipher = []
for each in data:
	cipher.append(ord(each)-97)

#consider two elements at a time and decrypt
plain = []
for i in range(0,len(cipher),2):
	elements = np.array([cipher[i],cipher[i+1]])
	decrypted = invkey.dot(elements)%26
	plain.append(chr(decrypted[0]+97))
	plain.append(chr(decrypted[1]+97))

print ''.join(plain)
print ''.join(plain[:-1]) # removing pad byte 
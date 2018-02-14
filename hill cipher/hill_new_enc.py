# initial setup and data
import numpy as np
from numpy.linalg import inv
data = 'sekharkaredla'
key = np.array([[2,3],[5,7]])

# pad data if not even
if len(data)%2 != 0:
	data += 'x' # pad byte

# convert data to ascii
plain = []
for each in data:
	plain.append(ord(each)-97)

# consider 2 elements at a time and encrypt
cipher = []
for i in range(0,len(plain),2):
	elements = np.array([plain[i],plain[i+1]])
	encrypted = key.dot(elements)%26
	cipher.append(chr(encrypted[0]+97))
	cipher.append(chr(encrypted[1]+97))

print ''.join(cipher) #convert list to string


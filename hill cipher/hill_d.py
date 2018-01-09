from numpy.linalg import inv
import numpy as np
s = 'a`tgda'
rand = np.array([[2,3],[5,7]])
rand = inv(rand)
out = ' '
plain_text=[]
for k in s:
	plain_text.append((ord(k)-96))
i = 0
for k in range(0,len(plain_text)/2):
	temp = np.array([[plain_text[i]],[plain_text[i+1]]])
	i+=2
	result = rand.dot(temp)
	out = out + chr(int(result.item(0))%26+96)+chr(int(result.item(1))%26+96)
out = out[1:]
print out
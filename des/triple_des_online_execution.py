#use this for online execution (repl.it)
from pyDes import *
data = 'sekharkaredlaCBIT'
e = triple_des('ABCDEFGHIJKLMNOP',ECB,pad = '~',padmode = PAD_NORMAL)
encrypted_data = e.encrypt(data)
with open('encrypted.txt','w') as file:
  file.write(encrypted_data)
  file.close()
print "decrypted data is : " + e.decrypt(encrypted_data)

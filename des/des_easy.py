from pyDes import *
data = 'sekharkaredlaCBIT'
e = des('HIHIHIHI',ECB,pad = '~',padmode = PAD_NORMAL)
encrypted_data = e.encrypt(data)
print "encrypted data is : " + encrypted_data
print "decrypted data is : " + e.decrypt(encrypted_data)

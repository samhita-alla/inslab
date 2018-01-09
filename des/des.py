from pyDes import *

data = "sekhar karedla"

e = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

encrypted_data = e.encrypt(data)

print "encrypted data is : "+encrypted_data

print "decrypted data is : "+e.decrypt(encrypted_data)
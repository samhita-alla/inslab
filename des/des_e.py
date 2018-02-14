from pyDes import *
data = 'sekharkaredlaCBIT'
e = encrypt('HIHIHIHI',ECB,pad = '~',padmode = PAD_NORMAL)
encrypted = e.encrypt(data)

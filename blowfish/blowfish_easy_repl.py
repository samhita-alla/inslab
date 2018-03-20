from Crypto.Cipher import Blowfish

class BFCipher:
  def __init__(self,key):
    self.cipher = Blowfish.new(key)
    self.pad_bytes = 0
  
  def encrypt(self,data):
    return self.cipher.encrypt(self.pad_data(data))
  
  def decrypt(self,data):
    return self.unpad_data(self.cipher.decrypt(data))
  
  def pad_data(self,data):
    self.pad_bytes = 8 - (len(data)%8)
    pad_data = '~'*self.pad_bytes
    data += pad_data
    return data
  
  def unpad_data(self,data):
    return data[:-self.pad_bytes]

data = 'sekhar karedla CBIT'
key = 'abcd'
cip = BFCipher(key)
encrypt = cip.encrypt(data)
with open('encrypt.txt','w') as file:
  file.write(encrypt)
  file.close()
decrypt = cip.decrypt(encrypt)
print decrypt

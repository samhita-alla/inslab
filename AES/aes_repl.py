# while using repl.it , create the file enc.txt
from Crypto.Cipher import AES

key = '12345678123456781234567812345678'
IV = 16 * '\x00'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

plain_text = raw_input("enter plain text(length=16): ")
print "encryption-------------------------"
encrypted_text = encryptor.encrypt(plain_text)
with open('enc.txt','w') as file:
  file.write(encrypted_text)
  file.close()
print 'encrypted_text written to file enc.txt'

print "decryption-------------------------"
decryptor = AES.new(key, mode, IV=IV)
decrypted_text = decryptor.decrypt(encrypted_text)
print "decrypted text is: " + str(decrypted_text)

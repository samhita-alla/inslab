from Crypto.Cipher import AES

key = '12345678123456781234567812345678'
IV = 16 * '\x00'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

plain_text = raw_input("enter plain text(length=16): ")
print "encryption-------------------------"
encrypted_text = encryptor.encrypt(plain_text)
print "encrypted text is: " + str(encrypted_text)

print "decryption-------------------------"
decryptor = AES.new(key, mode, IV=IV)
decrypted_text = decryptor.decrypt(encrypted_text)
print "decrypted text is: " + str(decrypted_text)

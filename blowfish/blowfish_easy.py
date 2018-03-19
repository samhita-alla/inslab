from Crypto.Cipher import Blowfish

class BFCipher:
    def __init__(self,key):
        self.cipher = Blowfish.new(key)
        self.pad_bytes = 0

    def encrypt(self,data = ''):
        ciphertext = self.cipher.encrypt(self.pad_data(data))
        return ciphertext

    def decrypt(self,data = ''):
        return self.unpad_data(self.cipher.decrypt(data))

    def pad_data(self,data):
        self.pad_bytes = 8 - (len(data) % 8)
        pad_data = '~'*self.pad_bytes # '~' is the padding character
        data += pad_data
        return data

    def unpad_data(self,data):
        return data[:-self.pad_bytes]


if __name__ == '__main__':
    data = 'sekharkaredla'
    # key of 32 bit
    key32 = 'abcd'
    bfc = BFCipher(key32)
    encrypt = bfc.encrypt(data)
    print encrypt
    decrypt = bfc.decrypt(encrypt)
    print decrypt

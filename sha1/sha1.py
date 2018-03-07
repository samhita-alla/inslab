from hashlib import sha1
print sha1(raw_input('enter data:').encode('utf-8')).hexdigest()

# md5 is a hashing process , it is a one way process , there is no possible way to decode it except brute-force

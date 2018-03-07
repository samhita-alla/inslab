from hashlib import md5
print md5(raw_input('enter data:').encode('utf-8')).hexdigest()

# md5 is a hashing process , it is a one way process , there is no possible way to decode it except brute-force

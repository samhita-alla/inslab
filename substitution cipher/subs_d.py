data = 'frxune xnerqyn'

dec = ' ' 

for each in data:
	val = ord(each) - 97
	if(val >= 0 and val < 13):
		dec = dec + chr(97 + (val + 13))
	elif(val >= 13 and val < 26):
		dec = dec + chr(97 + (val - 13))
	else:
		dec = dec + chr(97 + val)

print 'decrypted values is : ' + dec[1:]

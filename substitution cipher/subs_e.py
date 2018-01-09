data = 'sekhar karedla'

enc = ' ' 

for each in data:
	val = ord(each) - 97
	if(val >= 0 and val < 13):
		enc = enc + chr(97 + (val + 13))
	elif(val >= 13 and val < 26):
		enc = enc + chr(97 + (val - 13))
	else:
		enc = enc + chr(97 + val)

print 'encrpted values is : ' + enc[1:]

data = raw_input('enter encrypted data: ')
out = []
for each in data:
	temp = ord(each) - 97
	temp = temp - 1
	if(temp < 0):
		temp = temp + 26
	out.append(chr(temp+97))
print ''.join(out)

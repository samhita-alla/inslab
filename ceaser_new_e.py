data = raw_input('enter data: ')
out = []
for each in data:
	temp = ord(each) - 97
	temp = (temp + 1)%26
	out.append(chr(temp+97))
print ''.join(out)

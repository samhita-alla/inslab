inp = open('out.txt','r')
out = open('text.txt','w')
for j in inp.readlines():
	list = []
	for k in j:
		list.append(chr(ord(k)-1))

	out.write(''.join(list))


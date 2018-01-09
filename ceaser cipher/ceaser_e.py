inp = open('text.txt','r')
out = open('out.txt','w')
for j in inp.readlines():
	list = []
	for k in j:
		list.append(chr(ord(k)+1))

	out.write(''.join(list))


p = input()
q = input()
e = input()
n = p * q
phi = (p - 1) * (q - 1)
d=1
s=0
while(s!=1):
  s = (d*e)%phi
  d+=1
d-=1
data = raw_input()
enc = []
for each in data:
  count = e
  p = ord(each)
  c = 1
  while count>0:
    c = (c*p)%n
    count-=1
  enc.append(c)
print enc
dec = []
for each in enc:
  count = d
  p = 1
  while count>0:
    p = (each*p)%n
    count-=1
  dec.append(chr(p))
print ''.join(dec)

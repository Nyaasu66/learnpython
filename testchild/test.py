a1 = open('a.txt','r').read()
a2 = open('a.txt','wb')
a2.write(a1.encode('UTF-8'))
a2.close()

b1 = open('b.txt','r').read()
b2 = open('b.txt','wb')
b2.write(b1.encode('UTF-8'))
b2.close()

print('Done')

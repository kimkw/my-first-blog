print('Hello, Django girls!')

if 3<2:
	print('It works')
else :
	print('It is not works')

	
def hi():
	print('hi there')
	print('how are yu?')

hi()


def bye(name):
	if name== 'kw':
		print('bye kw')
	elif name == 'sy':
		print('byt sy')
	else :
		print('bye everyone')


bye('kw')
bye('sy')
bye('hoho');

def hiname(name):
	print('hi ' + name)


girls= ['kw', 'sy', 'student']
for name in girls:
	hiname(name)
	print('next')


for i in range(1,10):
	print(i)

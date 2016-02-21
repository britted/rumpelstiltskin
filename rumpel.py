import numpy

letters = []
abc_keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values = numpy.zeros(len(abc_keys))
i = 0
matrix = open('Rumpelstiltskin.txt', 'rb')
for line in matrix:
	for char in line:
		letters.append(char)
for each in abc_keys:
	for letter in letters:
		if letter == each:
			i = i+1
	values[abc_keys.index(each)] = i
	i = 0
hash = dict(zip(abc_keys, values))
print hash

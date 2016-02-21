import numpy 

words = []
first_letters = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
abc_keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values = numpy.zeros(len(abc_keys))
i = 0
matrix = open('Rumpelstiltskin.txt', 'rb')
for line in matrix:
	words.append(line.split())
	
for par in words:
	for word in par:
		if word[0] == '"':
			first_letters.append(word[1])
		else:
			first_letters.append(word[0])

for key in abc_keys:
	for each in first_letters:
		if key == each:
			i += 1 
			values[abc_keys.index(each)] = i
	i = 0
hash = dict(zip(abc_keys, values))
print hash
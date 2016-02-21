import numpy

abc_keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values = numpy.zeros(len(abc_keys))
letters = []
i = 0

matrix = open('Rumpelstiltskin.txt', 'r')
for line in matrix:
	words = line.split()
	for eachWord in words:
		n = 0
		if eachWord[n].isalpha():
			print 'testing'
			letters.append(eachWord[n])
		else:
			if len(eachWord) > 1:
				n= n+1 
				letters.append(eachWord[n])

for each in abc_keys:
	for eachLetter in letters:
		if eachLetter == each:
			i = i+1
	values[abc_keys.index(each)] = i
	i = 0

hash = dict(zip(abc_keys, values))
print hash
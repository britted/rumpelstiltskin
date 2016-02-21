import numpy 

words = []
first_letters = []
abc_keys = 'abcdefghijklmnopqrstuvwxyz'
values = numpy.zeros(len(abc_keys))
i = 0
matrix = open('Rumpelstiltskin.txt', 'r')
for line in matrix:
	words = ''.join([character.lower() for character in line if(character in abc_keys or character.isspace())])
	blah = words.split()
print words
print blah
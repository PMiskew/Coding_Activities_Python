#This is a core algorithm is an example
#that loops through a list and prints 
#out words lrager than a specific size

words = ["word1","word2","word3"]

for i in range(0, len(words), 1):
	if (len(words[i]) > 10):
		print(words[i])



''' Write a Python program to count the occurrences of each word in a given sentence..'''

str=input("Enter String:")
counts = dict()
txt = str.split(" ")           # is function
for word in txt:
	if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1
print(counts)


''' Write a Python program to count the occurrences of each word in a given sentence..'''

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

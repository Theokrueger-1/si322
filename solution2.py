#Reads from file
#add strings to list 

words = []
with open("words.txt", "r") as f:
    onestring = f.read()
    words = onestring.split()



#count ocurrences and store string + count in a dictionary
from collections import Counter
word_counts = {} #make a dictionary to store word : count
for word in words:
    word_counts[word] = word.get(word,0) + 1

sorted_words = dict(sorted(word_count.items()))


#Print the dictionary
print(sorted_words)
name = '/Users/lunar/Projects/Grojects/words.txt'

handle = open(name, 'r')

counts = dict()
for line in handle:
    #print("line: " + line)
    words = line.split()
    print("words: " + words)
    for word in words:
        counts[word] = counts.get(word,0) + 1
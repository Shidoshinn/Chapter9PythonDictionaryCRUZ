file = open('words.txt')
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
    print('Counts', counts)


jjj = ('chuck' : 1, 'fred' : 42, 'jan' : 100)
    for aaa,bbb in jjj.items() :
        print(aaa, bbb)


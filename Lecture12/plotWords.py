import pylab
import string

vowels = 'EYUIOA'
consonants = 'QWRTPSDFGHJKLZXCVBNM'
vowelCnt = [0,0,0,0,0,0,0,0,0,0]
consonantsCnt = [0,0,0,0,0,0,0,0,0,0]

inFile = open('words.txt')
for line in inFile.readlines():
    word = line.strip()
    for c in word:
        if c in vowels:
            vowelCnt[len(word) - 1] += 1
        if c in consonants:
            consonantsCnt[len(word) - 1] += 1

pylab.figure(1)
pylab.plot(range(1, len(vowelCnt)+1), vowelCnt, label='Vowels')
pylab.plot(range(1, len(consonantsCnt)+1), consonantsCnt, 'r', label='Consonants')
pylab.title('Number of Vowels and Consonants in the words\n of a given length (words.txt from PS4)')
pylab.xlabel('Word Length')
pylab.ylabel('Number of Characters')
pylab.legend(loc = 'best')
pylab.show()


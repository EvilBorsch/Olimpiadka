import operator
path = 'C:\\text2.txt'
with open(path, 'r') as f:
    text = f.read().split()
slov = dict()
t_slov = dict()
wordlist = set()
minlet = 'a'

for word in text:
    wordlist.add(word)
wordlist = list(wordlist)
wordlist.sort()

for word in wordlist:
    slov[word] = {}
    t_slov[word] = 0

for word in slov:
    slov[word] = t_slov.copy()

# print(slov)

wordnum = 0

for wordnum in range(text.__len__() - 1):
    word = text[wordnum]
    nextword = text[wordnum + 1]
    slov[word][nextword] = slov[word][nextword] + 1
print(slov)

kolvolist = []
chistiylist = []
sum = 0

for word in wordlist:
    for word2 in wordlist:
        if (slov[word][word2] not in kolvolist):
            if slov[word][word2] > 1:
                kolvolist.append(slov[word][word2])
        else:
            kolvolist.remove(slov[word][word2])
    sum = sum + kolvolist.__len__()
    chistiylist.append(kolvolist.copy())
    print(kolvolist)
    kolvolist.clear()

print(sum)
# for word in wordlist:
#    for word2 in wordlist:
#        for num in range(0,chistiylist.__len__()-1):

print(chistiylist)

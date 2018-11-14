import operator

path = 'C:\\text2.txt'
with open(path, 'r') as f:
    text = f.read().split()

slov = dict()
t_slov = dict()

for word in text:
    if word not in slov:
        slov[word] = 0
        t_slov[word] = 0

for word in slov:
    slov[word] = t_slov.copy()

for num in range(text.__len__() - 1):
    slov[text[num]][text[num + 1]] += 1

print(slov)
"""
max_word = 'test'
max_a = -2
povtor = 0
count = 0
a_list = list()
#print()

for word_s in slov:
    for word in slov[word_s]:
        a = slov[word_s][word]
        a_list.append([a, word])
    a_list.sort(reverse=True)
    
    i = 0
    print(a_list,' ',a_list[2][0])
    while (a_list[i][0] > 1) and (a_list[i][0] == a_list[i+1][0]) and (i<slov.__len__()-1):
        print(a_list[0][i])
        i=i+1
    a_list.clear()
"""
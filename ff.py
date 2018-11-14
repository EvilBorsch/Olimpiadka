lis=[0, 0, 2, 0, 3, 4, 3, 4]

newl=[]
print(new)
counter=0
for i in lis:
    if i not in newl:
        newl.append(i)
    else:

        print(newl.index(i))
        newl.remove(i)
print(newl)
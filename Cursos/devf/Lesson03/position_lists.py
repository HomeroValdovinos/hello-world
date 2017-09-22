myList = [1, 2, 3, 4, 5]
m = 0
for i in range(len(myList)):
    if m < myList[i]:
        m = myList[i] + m
    print i, m

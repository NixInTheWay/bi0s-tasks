def sortinator3000(List):
    n = len(List)
    for i in range(1,n):
        value = List.pop()
        ind = i
        for j in range(i-1,-1,-1):
            if List[j] > value:
                ind = j
        List.insert(ind,value)
    return List
while True:
    list = eval(input("Enter list:"))
    num = int(input("Enter number: "))
    sortedlist=sortinator3000(list)
    print(sortedlist)
    print(num in sortedlist)

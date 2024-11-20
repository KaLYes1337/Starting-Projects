def sublistSumFinder(firstInput,secondInput,placeHolder):
    emptyList=[]
    for i in firstInput:
        for j in secondInput:
            if len(firstInput) > len(secondInput):
                emptyList.append(i)
                emptyList.append(placeHolder)
            emptyList.append(j)
    print(emptyList)
            

sublistSumFinder([1, 2, 3],[4, 5],None)
def selectionSort(L):
    for i in range (len(L)-1):
        print(L)
        minInd = i
        minVal = L[i]
        j = i+1
        while j< len(L):
            if minVal > L[j]:
                minInd = j
                minVal = L[j]
            j+=1
        temp = L[i]
        L[i] = L[minInd]
        L[minInd] = temp
    return L

test = [1,5,2,8,9,0,3,5,7]
print(selectionSort(test))

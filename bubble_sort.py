def bubble_sort(L):
    swap=False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                swap= False
                temp = L[i]
                L[i] = L[i-1]
                L[i-1] = temp

    return L

List1 = [5,3,7,2,8,9,1,0]
print(bubble_sort(List1))

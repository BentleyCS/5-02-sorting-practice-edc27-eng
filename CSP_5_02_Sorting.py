import random


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0
    ordered = False
    while not(ordered):
        ordered = True
        for i in range(0,len(items)-1):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
                comparisons +=1
                swaps+=1
                ordered = False
            else:
                comparisons+=1
    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    for i in range(1,len(items)):
        n = i
        while n > 0:
            comparisons +=1
            if items[n] < items[n-1]:
                temp = items[n]
                items[n] = items[n-1]
                items[n-1] = temp
                swaps +=1
                n -=1
            else:
                break

    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0
    full = len(items)
    for i in range(full-1):
        smol = i
        for n in range(i+1, full):
            comparisons+=1
            if items[n] < items[smol]:
                smol = n
        temp = items[i]
        items[i] = items[smol]
        items[smol] = temp
        swaps+=1
    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))

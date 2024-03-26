"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
Its time complexity is O(n^2)
"""

def bubbleSort(n):
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp
    return n

n = [1,2,232,213,43,3]
print(bubbleSort(n))
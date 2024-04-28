def bubbleSort(n):
    length = len(n)
    for i in range(length, 1, -1):
        for j in range(0, i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

n = [123,32,1,2,434,3, 2121, 32, 4, 1, 2, 2.4]
print(bubbleSort(n))
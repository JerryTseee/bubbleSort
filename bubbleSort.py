def bubbleSort(n):
    length = len(n)
    for i in range(length):
        for j in range(length-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

n = [123,32,1,2,434,3]
print(bubbleSort(n))
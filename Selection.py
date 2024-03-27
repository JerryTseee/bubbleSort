

def Selection(n):
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp
    return n

n = [1,2,232,213,43,3]
print(Selection(n))

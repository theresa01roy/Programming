n=input("Enter number:")
n=int(n)
l=[0,1]
def fibonacci(l):
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l
print(fibonacci(l))

dict1 = {}
dict2 = {}
res = {}

n = int(input("Enter number of elements in dict1: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

m = int(input("Enter number of elements in dict2: "))
for _ in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

def newdict(dict1, dict2):
    a = set(dict1.keys())
    b = set(dict2.keys())
    c = a.intersection(b)
    res = {k: dict1[k] for k in c if dict1[k] == dict2[k]}
    return res

print(newdict(dict1, dict2))

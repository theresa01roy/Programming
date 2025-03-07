lst=input("Enter list elements: ").split()
def find_max(lst):
    temp=0
    for i in lst:
        if (int(i)>int(temp)):
            temp=i
    return temp
print(find_max(lst))
    
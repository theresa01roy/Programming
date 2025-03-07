lst=input("Enter the list of strings:").split()
def remove_duplicates(lst):
    new_lst=set(lst)
    new_lst=list(new_lst)
    return new_lst
print(remove_duplicates(lst))
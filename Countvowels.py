string=input("Enter your string: ")
count=0
def count_vowels(string,count):
    vowels=['A','E','I','O','U','a','e','i','o','u']
    for i in string:
        if i in vowels:
            count=count+1
    return count
print(count_vowels(string,count))

        

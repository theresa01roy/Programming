string=input("enter string : ")
def is_palindrome(string):
    a=string
    rev=a[::-1]
    if(string==rev):
        print("The string {} is pallindrome".format(string))
    else:
        print("The string {} is not pallindrome".format(string))
is_palindrome(string)
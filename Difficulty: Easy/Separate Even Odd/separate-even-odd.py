#User function Template for python3


def evenOdd(arr):
    even = []
    odd = []

    #Write your code below to append odd elements in numbers to odd list
    #Write your code below to append even elements in numbers to even list
    for item in arr:
        if(item%2==0):
            even.append(item)
        else:
            odd.append(item)
    return (even, odd)  #This is the return statement

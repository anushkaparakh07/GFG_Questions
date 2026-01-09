#User function Template for python3

def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    l = []
    for i in arr:
        if(i>=0):
            l.append(i)
    return sum(l)/len(l)
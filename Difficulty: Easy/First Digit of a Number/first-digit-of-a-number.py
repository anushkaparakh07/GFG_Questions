def firstDigit(n):
    #code here
    l = []
    while(n!=0):
        lastdigit = n%10
        l.append(lastdigit)
        n//=10
    return l[len(l)-1]
    
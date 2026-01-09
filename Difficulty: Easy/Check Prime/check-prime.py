#User function Template for python3
import math
n = int(input())
if(n<2):
    print(False)
# Your code here
isPrime = True
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        isPrime = False

if(isPrime):
    print(True)
else:
    print(False)
class Solution:    
    def printNos(self,n,a=1):
        #Code here
        if(a>n):
            return 
        print(a,end=' ')
        self.printNos(n,a+1)
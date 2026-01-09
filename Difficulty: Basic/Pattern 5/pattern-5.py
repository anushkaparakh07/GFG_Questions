#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(0,N):
            for j in range(N-i):
                print('*',end=' ')
            print()
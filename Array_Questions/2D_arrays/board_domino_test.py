class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.h = {}
        self.M = 10**9 + 7
        return self.dfs(N, 0)
        
    def dfs(self, N, state):
        key = (N,state)
        
        if key in self.h:
            return self.h[key]
        
        if N<=1:
            ans = 1

        elif N==2:
            ans = 2 if state==0 else 1
            
        elif state==0:
            ans = self.dfs(N-1,0) + self.dfs(N-1,2) + self.dfs(N-1,1) + self.dfs(N-2,0)
        
        elif state==1:
            ans = self.dfs(N-1,2) + self.dfs(N-2,0)
        
        elif state==2:
            ans = self.dfs(N-1,1) + self.dfs(N-2,0)
            
        ans %= self.M
        self.h[key] = ans
        return ans

print(Solution.numTilings(1))
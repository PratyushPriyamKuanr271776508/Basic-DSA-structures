#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        intervals = sorted([(i-g, i+g) for i, g in enumerate(gallery) if g != -1], reverse=True)
        reachable, best, res = 0, 0, 0
        
        # We are given intervals first sort them according to the requirement
        
        while reachable < n:
            # We have to start from 0 till n to see the munimum intervals required to cover the whole space
            # This is a Sweep Line Algorithm Problem
            # The if part is used to find the longest interval which starts with reachable
            # The below if means the if there is a group overlap you keep on poping and setting the max end value
            if intervals and intervals[-1][0] <= reachable:
                s, e = intervals.pop()
                best = max(best, e+1)
            
            # This statement sets the next reachable point or the ending point
            elif best > reachable:
                reachable = best
                res += 1
            else:
                return -1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends
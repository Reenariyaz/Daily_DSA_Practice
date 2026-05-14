class Solution:
    def findMinDiff(self, arr, m):
        n=len(arr)
        arr.sort()
        left=0
        right=m-1
        min_diff=float('inf')
        while right<n:
            min_diff=min(arr[right]-arr[left],min_diff)
            left+=1
            right+=1
        return min_diff
                
arr= [3, 4, 1, 9, 56, 7, 9, 12]
obj=Solution()
print(obj.findMinDiff(arr,5))

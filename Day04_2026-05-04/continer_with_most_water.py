class Solution:
    def maxWater(self, arr):
        n=len(arr)
        left=0
        right=n-1
        max_area=0
        while left < right:
            height= min(arr[left],arr[right])
            width=right-left
            area=height*width
            max_area=max(max_area,area)
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return max_area
    
height=[1,8,6,2,5,4,8,3,7]
obj=Solution()
print(obj.maxWater(height))


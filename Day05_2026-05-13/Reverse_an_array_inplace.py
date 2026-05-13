class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        left=0
        right=n-1
        while right>left:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
arr=[1,2,3,4,5]
obj=Solution()
print(obj.reverseArray(arr))
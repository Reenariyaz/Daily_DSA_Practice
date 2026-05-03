class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        left = 0
        for right in range(n):
            if arr[right] != 0:
                arr[left] = arr[right]
                left += 1
        while left < n:
            arr[left] = 0
            left += 1
        return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]
obj = Solution()
print(obj.pushZerosToEnd(arr))

class Solution:
    def Brute_findTriplets(self, arr):
            n= len(arr)
            ans=False
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        if arr[i]+arr[j]+arr[k]==0: #here target is Zero
                            ans= True
            return ans

    def  Optimized_findTriplets(self, arr):
            n= len(arr)
            arr.sort()
            for i in range(n-2):
                target = -arr[i]
                left=i+1
                right=n-1
                while right>left:
                    if arr[left]+arr[right]>target:
                        right-=1
                    elif arr[left]+arr[right]<target:
                        left+=1
                    else:
                        return True
            return False

arr=[-1,0,1,2,-1,-4]
obj=Solution()
print(obj.Brute_findTriplets(arr))
print(obj.Optimized_findTriplets(arr))

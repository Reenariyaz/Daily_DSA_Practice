class solution:
    def removeDuplicates_using_set(self, arr):
        unique=set()
        result=[]
        for n in arr:
            if n not in unique:
                unique.add(n)
                result.append(n)
        return result
    
    def removeDuplicates_using_two_pointers(self, arr):
        left=0
        n=len(arr)
        for right in range(1,n):
            if arr[left]!=arr[right]:
                left+=1
                arr[left]=arr[right]
        return arr[:left+1]

arr=[1,1,2,2,3,3,4]
obj=solution()
print(obj.removeDuplicates_using_set(arr))
print(obj.removeDuplicates_using_two_pointers(arr))

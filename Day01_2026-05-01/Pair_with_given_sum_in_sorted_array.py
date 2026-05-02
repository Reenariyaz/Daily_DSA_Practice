#Brute-force
def Brute_pair_with_given_sum(arr, sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

def Optimized_countPairs (arr, target) : 
        #Complete the function
        n=len(arr)
        left=0
        right=n-1
        ans=0
        while right>left:
            curr=arr[left]+arr[right]
            if curr>target:
                right-=1
            elif curr<target:
                left+=1
            else:                     #from here the duplicates are also handled
                e1,e2=arr[left],arr[right]
                c1,c2=0,0
                while(left<=right and arr[left]==e1): #we count how many times the left indexed element appears in the array 
                    left+=1
                    c1+=1
                while(left<=right and arr[right]==e2): #we count how many times the right indexed element appears in the array 
                    right-=1
                    c2+=1
                if (e1==e2):   #both elements are same, i.e., duplicates
                    ans+=(c1*(c1-1))//2
                else:     #both are diff
                    ans+=c1*c2
        return ans

def countPairs_using_hashmap(self, arr, target):
        #code here
        freq={}
        n=len(arr)
        count=0
        for i in range(n):
            val=target-arr[i]
            if val in freq:
                count+=freq[val]
            freq[arr[i]]=freq.get(arr[i],0)+1
        return count
print(Optimized_countPairs([-1,1,5,5,7], 6))
print(Brute_pair_with_given_sum([-1,1,5,5, 7],6))

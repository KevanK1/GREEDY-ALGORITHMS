def kInt(arr:list[int], k:int)->list[int]:
    if len(arr)<k:
        return arr.sort()
    arr.sort(reverse=True)   #nlog(n) 
    return arr[:k]
print(kInt([51,1,44,7,2,1,88],3))

#  TC: O(n*log(n))
#  SC: 0
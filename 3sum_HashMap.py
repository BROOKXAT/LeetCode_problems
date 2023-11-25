class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid_3lets = []
        n = len(nums)
        #edge cases
        if n<3 : return []
        if nums[0]>0 : return []
        #creating a dictionnary as a hashmap
        hashMap = {}
        #Hashing indeces
        for i in range(n) :
            hashMap[nums[i]] = i
        i=0
        while i < n-1 :
            if nums[i] > 0 : break
            j = i+1
            while j < n:
                complement = -nums[i]-nums[j]
                if complement in hashMap and hashMap.get(complement) > j :
                    valid_3lets.append([nums[i],nums[j],complement])
                j = hashMap.get(nums[j]) +1
            i = hashMap.get(nums[i]) + 1

        return valid_3lets
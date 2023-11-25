class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid_3lets = []
        n = len(nums)
        for i in range(n) :
            # if the current element is greather then 0 break 
            if nums[i] > 0 : break
            #check for duplicated values
            if i>0 and nums[i] == nums[i-1] : continue
            #two pointers low and high
            low , high = i+1 , n-1
            #
            while low < high :
                sum = nums[i]+nums[low]+nums[high]
                #if the 3 sum is greather than 0 we lower the high pointer
                if sum > 0 : high -= 1
                #if the 3 sum is smaller than 0 we upper the low pointer
                elif sum < 0 : low += 1
                else :
                    valid_3lets.append([nums[i],nums[low],nums[high]])
                    lastLowOccurrence, lastHighOccurrence = nums[low],nums[high]
                    while low < high and nums[low] == lastLowOccurrence :
                        low += 1
                    while low < high and nums[high] == lastHighOccurrence :
                        high -= 1
        return valid_3lets
        

        
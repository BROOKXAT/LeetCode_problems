class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0]+ nums[1]+ nums[2]
        if n==3 : return closest
        for i in range(n-2) :
            if nums[i] > target :
                sum = nums[i]+ nums[i+1]+ nums[i+2]
                if abs(sum-target) < abs(closest-target) : 
                    return sum
                
            low , high = i+1 , n-1 
            while low < high :
                sum = nums[i]+ nums[low]+ nums[high]
                if abs(sum-target) < abs(closest-target) : closest = sum
                if sum > target : high -= 1
                elif sum < target : low += 1
                else : return sum
        return closest


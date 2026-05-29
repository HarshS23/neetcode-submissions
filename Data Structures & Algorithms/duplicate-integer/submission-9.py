class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            j = i + 1 
            if (nums[i] == nums[j]):
                return True 
        return False 

























        # nums.sort() # sort the array that takes O(nlogn)
        # for i in range(len(nums) - 1): # lopp takes O(n) 
        #     if nums[i] == nums[i+1]: # O(1)
        #         return True # O(1)
        # return False # O(1)

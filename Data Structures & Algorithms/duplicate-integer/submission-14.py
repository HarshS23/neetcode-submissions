class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Using a Hashmap 
        hashset = set()

        for i in nums:

            if i in hashset:
                return True 
            
            hashset.add(i)
        
        return False


        # nums.sort() # must be sorted first O(nlog) - worst case
        # for i in range(len(nums) - 1): # check until the end but not i +1 O(n)
        #     j = i + 1 
        #     if (nums[i] == nums[j]): # O(1)
        #         return True 
        # return False 

        # # so in total the run time is O(n log n)























        # nums.sort() # sort the array that takes O(nlogn)
        # for i in range(len(nums) - 1): # lopp takes O(n) 
        #     if nums[i] == nums[i+1]: # O(1)
        #         return True # O(1)
        # return False # O(1)

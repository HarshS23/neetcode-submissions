class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums[i] + nums[j] = target 
        # nums[i] = target - nums[j]
        # ^ 
        # | -------- difference 




        temp = {} # hash table 
        array = [] # output array 
        for i in range(len(nums)): # iterate through nums array O(n)
            difference = target - nums[i] 

            if difference in temp:
                array.append(temp[difference]) # get the differnce we stored
                array.append(i) # current index
            else:
                temp[nums[i]] = i # store the value 
        return array




        #OutputArray = []

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (i != j and nums[i] + nums[j] == target):
        #             OutputArray.append(i)
        #             OutputArray.append(j)
        #             return OutputArray
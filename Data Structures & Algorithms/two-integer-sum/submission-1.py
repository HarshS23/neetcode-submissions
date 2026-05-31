class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        OutputArray = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    OutputArray.append(i)
                    OutputArray.append(j)
                    return OutputArray
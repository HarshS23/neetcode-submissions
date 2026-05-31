class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        temp = {}
        array = []
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in temp:
                array.append(temp[difference])
                array.append(i)
            else:
                temp[nums[i]] = i
        return array




        #OutputArray = []

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (i != j and nums[i] + nums[j] == target):
        #             OutputArray.append(i)
        #             OutputArray.append(j)
        #             return OutputArray
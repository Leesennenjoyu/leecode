
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            another = target - num
            if another in nums:
                if another == num and not nums.count(num)>1:
                    continue
                return [index , nums.index(another,index +1)]

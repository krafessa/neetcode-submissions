class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialOperands = dict()
        for firstOperand in nums: 
            potentialOperands[target - firstOperand] = firstOperand
        for i in range(len(nums)):
            if nums[i] in potentialOperands:
                indexOfPotential = nums.index(potentialOperands[nums[i]])
                if i != indexOfPotential:
                    return [i, indexOfPotential]
                elif nums.count(potentialOperands[nums[i]]) != 1:
                    return [i, nums.index(potentialOperands[nums[i]], i+1)]
                



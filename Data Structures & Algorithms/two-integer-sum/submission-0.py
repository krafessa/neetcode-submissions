class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialOperands = dict()
        for firstOperand in nums:
            secondOperand = target - firstOperand
            potentialOperands[secondOperand] = firstOperand
        for i in range(len(nums)):
            if nums[i] in potentialOperands:
                potential = potentialOperands[nums[i]]
                indexOfPotential = nums.index(potential)
                if i != indexOfPotential:
                    return [i, indexOfPotential]
                elif nums.count(potential) != 1:
                    return [i, nums.index(potential, i+1)]
                



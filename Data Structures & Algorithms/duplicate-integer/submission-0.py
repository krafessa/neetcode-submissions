class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurrences = dict()
        for element in nums:
            if occurrences.get(element, False) is True:
                return True
            occurrences[element] = True
        return False

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = defaultdict(int)
        for number in nums:
            occurrences[number] += 1
        sortedBy = {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1], reverse = True)}
        return list(sortedBy.keys())[:k]

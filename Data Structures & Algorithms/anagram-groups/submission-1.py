class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for string in strs:
            key = tuple(sorted(string))
            l = groups.get(key, list())
            l.append(string)
            groups[key] = l
        return list(groups.values())

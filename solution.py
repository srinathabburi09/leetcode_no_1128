class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq_dict = {}
        count = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            freq = freq_dict.get(key, 0)
            count += freq
            freq_dict[key] = freq + 1
        return count

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_length = 0
        char_index_map = {}

        start = 0

        for end in range(n):
            if s[end] in char_index_map:
                start = max(start, char_index_map[s[end]] + 1)
            char_index_map[s[end]] = end
            max_length= max(max_length, end - start + 1)

        return max_length
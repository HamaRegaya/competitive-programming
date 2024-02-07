class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                result = chr(num + 96) + result
                i -= 3
            else:
                result = chr(int(s[i]) + 96) + result
                i -= 1

        return result
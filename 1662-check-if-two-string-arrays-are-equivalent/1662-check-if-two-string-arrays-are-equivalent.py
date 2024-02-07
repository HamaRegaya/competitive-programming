class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        concatenated_word1 = "".join(word1)
        concatenated_word2 = "".join(word2)
        return concatenated_word1 == concatenated_word2
        
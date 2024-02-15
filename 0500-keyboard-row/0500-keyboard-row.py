class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        
        for word in words:
            word_set = set(word.lower()) 
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                result.append(word)
                
        return result
            
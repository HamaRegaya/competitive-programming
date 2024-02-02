class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #create a dictionary to store the count of each number
        num_count = {}
        
        #count occurrences of each number
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        #calculate the number of good pairs
        result = 0
        for count in num_count.values():
            if count > 1:
                result += count * (count - 1) // 2
                
        return result

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize candidates and their counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # Step 1: Find the candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Count occurrences of candidates
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Check if candidates appear more than n/3 times
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        
        return result
        
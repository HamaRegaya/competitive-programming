class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Create a dictionary to store indices of strings in list1
        indices = {string: i for i, string in enumerate(list1)}
        
        # Initialize variables for minimum index sum and result
        min_index_sum = float('inf')
        result = []
        
        # Iterate through list2 to find common strings
        for j, string in enumerate(list2):
            # Check if the string is in list1
            if string in indices:
                # Calculate the index sum
                index_sum = j + indices[string]
                # If index sum is smaller than current minimum, update result
                if index_sum < min_index_sum:
                    result = [string]
                    min_index_sum = index_sum
                # If index sum equals current minimum, append to result
                elif index_sum == min_index_sum:
                    result.append(string)
        
        return result
class Solution(object):
    def sortPeople(self, names, heights):
        n = len(heights)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True
            if not swapped:
                break
        return names

        
class Solution(object):
    def pancakeSort(self, arr):
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            idx = arr.index(target)
            if idx != target - 1:
                if idx != 0:
                    result.append(idx + 1)
                    arr[:idx + 1] = reversed(arr[:idx + 1])
                result.append(target)
                arr[:target] = reversed(arr[:target])
        return result
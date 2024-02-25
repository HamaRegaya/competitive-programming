class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                delete_count += 1
        return delete_count
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_occurrence:
                last_occurrence[s[i]] = i

        partitions = []
        partition_start = 0
        partition_end = 0
        index = 0

        while index < len(s):
            char = s[index]
            partition_end = max(partition_end, last_occurrence[char])
            if index == partition_end:
                partitions.append(partition_end - partition_start + 1)
                partition_start = index + 1
            index += 1

        return partitions
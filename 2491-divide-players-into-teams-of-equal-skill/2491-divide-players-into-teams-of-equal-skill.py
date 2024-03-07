class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        if n % 2 != 0:
            return -1

        skill.sort()
        target_sum = sum(skill) // (n // 2)

        chemistry_sum = 0
        left, right = 0, n - 1
        while left < right:
            team_sum = skill[left] + skill[right]
            if team_sum != target_sum:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry_sum
        
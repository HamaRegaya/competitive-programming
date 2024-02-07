class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            ans =''
            if i%3==0 and i%5==0:
                ans = 'FizzBuzz'
            elif i%3==0:
                ans = 'Fizz'
            elif i%5==0:
                ans = 'Buzz'
            else:
                ans=str(i)
            result.append(ans)
        return result
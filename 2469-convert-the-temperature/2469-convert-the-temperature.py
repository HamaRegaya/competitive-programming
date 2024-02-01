class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        if(0 <= celsius <= 1000):
            return [round(celsius+273.15,5),round(celsius*1.80+32.00,5)]
        else:
            raise ValueError("0 <= celsius <= 1000")
        
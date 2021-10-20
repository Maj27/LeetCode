class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour*30+minutes*0.5)
        minutes_angle = minutes*6
        angle =  abs(minutes_angle-hour_angle)   
        return angle if angle<180 else 360-angle
                      
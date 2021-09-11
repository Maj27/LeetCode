class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direction = 90
        curr = [0,0]

        for i in range(4):
            for ins in instructions:
                if ins=='L':
                    direction+=90
                    if direction==360:
                        direction = 0


                elif ins=='R':
                    direction-=90
                    if direction==-90:
                        direction = 270

                else:#G
                    if direction ==90:
                        curr[1] += 1
                    elif direction ==270:
                        curr[1] -= 1
                    elif direction ==0:
                        curr[0] += 1
                    elif direction ==180:
                        curr[0] -= 1

            if curr== [0,0] and direction==90:
                return True  

        if curr == [0,0] and direction==90:
            return True
        else: 
            return False
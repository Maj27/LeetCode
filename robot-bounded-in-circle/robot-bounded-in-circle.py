class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        position = [0,0]
        direction = 90
        
        def move(ins, position, direction):
            if direction == 0:
                position[0] += 1
            elif direction == 180:
                position[0] -= 1
            elif direction == 90:
                position[1] += 1
            else:#270
                position[1] -= 1
                
        for ins in instructions:
            if ins == 'G':
                move(ins,position,direction)
            else:
                if ins=='L':
                    direction = (direction+90)%360
                if ins=='R':
                    direction = (direction+270)%360

        if position == [0,0] or direction !=90:
            return True
        return False
    

    
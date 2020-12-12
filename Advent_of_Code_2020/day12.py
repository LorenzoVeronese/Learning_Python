"""
---PART ONE---
"""
"""
NOTES
      N,90°
W,180°      E,0°
      S,270°
"""

import math

direction_map = (
    ('E', 0),
    ('N', 90),
    ('W', 180),
    ('S', 270)
)
class Ship(object):
      def __init__(self, x, y, angle):
            """
            PARAMETHERS
            x: int, starting orizontal position of the ship (east is pos, west neg)
            y: int, starting vertical position of the ship (north is pos, south neg)
            angle: string, starting direction of the ship
            """    
            self.x = x
            self.y = y
            self.angle = angle

      def __str__(self):
            return "X: " + str(self.x) + " | Y: " + str(self.y) + " | Angle: " + str(self.angle)

      def get_x(self):
            return self.x

      def get_y(self):
            return self.y

      def change_angle(self, move_angle):
            """
            PARAMETHER
            new_angle: string, new ship's direction
            """
            self.angle += move_angle
            #I want only positive angles
            if self.angle < 0:
                  self.angle += 360
            #I want angles smaller or equal to 360
            if self.angle >= 360:
                  self.angle -= 360

      def go_head(self, dist):
            """
            PARAMETHER
            dist: int, distance to travel in the current direction

            changes the position of the ship going in the current direction
            """
            #NB: cos and sin would never return 0 due to cumputational limits
            self.x += dist * int(math.cos(math.radians(self.angle)))
            self.y += dist * int(math.sin(math.radians(self.angle)))
      
      def move_x(self, dist):
            """
            PARAMETHER
            dist: int, distance to travel along x
            """
            self.x += dist
      
      def move_y(self, dist):
            """
            PARAMETHER
            dist: int, distance to travel along y
            """
            self.y += dist
      
      def change_position(self, instruction):
            #global index (for debugging)
            """
            PARAMETHER
            instruction: string, with structure 'ActionValue' indicating 
                  how to move the ship
            """
            action = instruction[0]
            value = int(instruction[1 : len(instruction)])

            #E, N, W, S
            if action == 'E':
                  self.move_x(value)
            elif action == 'N':
                  self.move_y(value)
            elif action == 'W':
                  self.move_x((-1) * value)
            elif action == 'S':
                  self.move_y((-1) * value)
            #L R
            elif action == 'L':
                  self.change_angle(value)
            elif action == 'R':
                  self.change_angle((-1) * value)
            #F
            elif action == 'F':
                  self.go_head(value)

            #print(index, ship)
            #index += 1
            
filename = "day12.txt"
ship = Ship(0, 0, 0)
#index = 1
with open(filename, 'r') as fd:
      for line in fd:
            if line[len(line) - 1] == '\n':
                  line = line[0 : len(line) - 1]
            ship.change_position(line)

#print(ship)
print(abs(ship.get_x()) + abs(ship.get_y()))

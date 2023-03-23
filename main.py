import math
from circleIntersection import get_intersections

# configuration of a specific arm
# angles are stored in radians
class ArmSetup:
  def __init__(self, _l1, _l2, _l3, _a1, _a2, _a3):
    self.l1 = _l1
    self.l2 = _l2
    self.l3 = _l3
    
    self.angle1 = _a1
    self.angle2 = _a2
    self.angle3 = _a3

  def calculateTorque(self):
    t1 = 39.2 * self.l1 * (self.l1 * math.cos(self.angle1) / 2) 
    t2 = 19.6 * self.l2 * ((self.l1 * math.cos(self.angle1)) + (self.l2 * math.cos(self.angle2) / 2))
    t3 = 9.8 * self.l3 * ((self.l1 * math.cos(self.angle1)) + (self.l2 * math.cos(self.angle2)) + (self.l3 * math.cos(self.angle3) / 2))
    weight = 9.8 * 5 * ((self.l1 * math.cos(self.angle1)) + (self.l2 * math.cos(self.angle2)) + (self.l3 * math.cos(self.angle3)))

    return t1+t2+t3 + weight

  def isValid(self):
    return self.l1 + self.l2 + self.l3 >= 1

  def print(self):
    print("L1", self.l1, "L2", self.l2, "L3", self.l3)
    print("A1", math.degrees(self.angle1), "A2", math.degrees(self.angle2), "A3", math.degrees(self.angle3))

# final position of the arm
class FinalPosition:
  def __init__(self, x, y, angle):
    self.x = x
    self.y = y
    self.angle = angle

# x and y coordinates
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  

# calculate the dimensions of an arm
def calculatePosition(l1, l2, l3, finalPosition):
  thirdJoint = Point(finalPosition.x - math.cos(finalPosition.angle), finalPosition.y - math.sin(finalPosition.angle))

  secondPoints = get_intersections(thirdJoint.x, thirdJoint.y, l2, 0, 0, l1)
  secondPoint1 = Point(secondPoints[0], secondPoints[1])
  secondPoint2 = Point(secondPoints[2], secondPoints[3])

  print(secondPoint1.x, secondPoint1.y)

  secondAngle1 = math.asin((thirdJoint.y - secondPoint1.y) / l2)
  secondAngle2 = math.asin((thirdJoint.y - secondPoint2.y) / l2)

  if thirdJoint.x - secondPoint1.x < 0:
    secondAngle1 = math.pi - abs(secondAngle1)

  if thirdJoint.x - secondPoint2.x < 0:
    secondAngle2 = math.pi - abs(secondAngle2)

  firstAngle1 = math.asin((secondPoint1.y - 0) / l1)
  firstAngle2 = math.asin((secondPoint2.y - 0) / l1)

  if secondPoint1.x < 0:
    firstAngle1 = math.pi - abs(firstAngle1)
    
  if secondPoint2.x < 0:
    firstAngle2 = math.pi - abs(firstAngle2)

  angle3 = finalPosition.angle

  return [ArmSetup(l1, l2, l3, firstAngle1, secondAngle1, angle3), ArmSetup(l1, l2, l3, firstAngle2, secondAngle2, angle3)]


def main():

  finalPosition1 = FinalPosition(0.75, 0.1, -math.pi/3)
  finalPosition2 = FinalPosition(0.5,0.5,0)
  finalPosition3 = FinalPosition(0.2, 0.6, math.pi/4)


# loop thru here
  for l1 in range (1, 100):
    for l2 in range (1, 100):
        for l3 in range (1, 100):
            # later uwu
  
  # armSetups = calculatePosition(1, 1, 1, finalPosition1)
  # armSetups[0].print()
  # armSetups[1].print()
  # print(armSetups[0].calculateTorque())
  # print(armSetups[1].calculateTorque())


if __name__ == "__main__":
  main()
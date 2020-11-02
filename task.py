import random

def GetRandomRate():
  return random.randrange(0,360)

def GetRandomAngle():
  rate_of_correction = GetRandomRate()
  return random.gauss(0, 2*rate_of_correction)

if __name__ == "__main__":

  roll_orientation = 0
  pitch_orientation = 0
  yaw_orientation = 0

  print("Roll orientation: {}, pitch orientation: {}, yaw orientation: {}. \n". format(roll_orientation,pitch_orientation,yaw_orientation))

  while(True):
    roll_angle = GetRandomAngle()
    pitch_angle = GetRandomAngle()
    yaw_angle = GetRandomAngle()

    roll_orientation += roll_angle
    pitch_orientation += pitch_angle
    yaw_orientation += yaw_angle

   

    print("Roll orientation: {}, pitch orientation: {}, yaw orientation: {}. \n". format(roll_orientation,pitch_orientation,yaw_orientation))

    
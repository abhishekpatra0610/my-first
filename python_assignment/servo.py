angles =[30,-15,45,200,60,90]
def valid_angle(angle):
    return 0 <= angle <= 180

valid_angles = list(filter(valid_angle,angles))

def servo_command(angle):
 return angle *10

servo_commands = list(map(servo_command ,valid_angles))

print("valid angles:",valid_angles)
print ("servo commands:",servo_commands)




import time
from proxy import motionProxy, postureProxy, motion

def wave_hand():
    # Lift the right arm
    motion.angleInterpolationWithSpeed("RShoulderPitch", -0.5, 0.2)  # Arm up
    motion.angleInterpolationWithSpeed("RElbowYaw", 1.5, 0.2)         # Elbow out
    
    # Wave by rotating the wrist
    for _ in range(3):
        motion.angleInterpolationWithSpeed("RWristYaw", -1.0, 0.2)  # Rotate hand outward
        motion.angleInterpolationWithSpeed("RWristYaw", 1.0, 0.2)   # Rotate hand inward

    # Return arm to resting position
    motion.angleInterpolationWithSpeed("RShoulderPitch", 1.5, 0.2)  # Arm down
    motion.angleInterpolationWithSpeed("RElbowYaw", 0.0, 0.2)       # Elbow back in
    motion.angleInterpolationWithSpeed("RWristYaw", 0.0, 0.2)       # Wrist to neutral


def nod_head():
    # Nod head motion
    motionProxy.setStiffnesses("Head", 1.0)

    names = ["HeadPitch"]
    angles = [0.2, -0.2]  # Nod down and up
    times = [1.0, 2.0]  # Timing for nodding
    isAbsolute = True

    # Perform head nod
    motionProxy.angleInterpolation(names, angles, times, isAbsolute)
    motionProxy.setStiffnesses("Head", 0.0)

def stand_up():
    # Make the robot stand straight
    # postureProxy.goToPosture("StandInit", 0.5)
    motion.wakeUp()
# Final transition to the standing posture
    # postureProxy.goToPosture("Stand", 0.5)  # Go to "Stand" posture with gradual speed

    postureProxy.goToPosture("Crouch", 0.5)  # Use "Sit" posture for a more stable position
    time.sleep(2)
    postureProxy.goToPosture("Stand", 0.5)  # Use "Sit" posture for a more stable position


    print("Nao has safely stood up.")


# Execute the function

# Introduce Nao with natural body language
def introduce_nao():

    #tts.say("Hello! My name is Nao. I heard your are a great teacher. so I'm here to learn English pronunciation with you.")
    motion.angleInterpolationWithSpeed("HeadYaw", 0.3, 0.2)  # Small head tilt
    motion.angleInterpolationWithSpeed("RShoulderPitch", 1.0, 0.2)  # Lift right arm slightly
    #time.sleep(1)

def celebration():
#    # Raise both arms at the same time
#     motion.angleInterpolationWithSpeed(["LShoulderPitch", "RShoulderPitch"], [-0.5, -0.5], 0.2)  # Arms up
#     motion.angleInterpolationWithSpeed(["LElbowYaw", "RElbowYaw"], [-1.5, 1.5], 0.2)  # Elbows out

#     # Wave both hands simultaneously
#     for _ in range(3):
#         motion.angleInterpolationWithSpeed(["LWristYaw", "RWristYaw"], [-1.0, -1.0], 0.2)  # Hands outward
#         motion.angleInterpolationWithSpeed(["LWristYaw", "RWristYaw"], [1.0, 1.0], 0.2)   # Hands inward

#     # Lower both arms at the same time
#     motion.angleInterpolationWithSpeed(["LShoulderPitch", "RShoulderPitch"], [1.5, 1.5], 0.2)  # Arms down
#     motion.angleInterpolationWithSpeed(["LElbowYaw", "RElbowYaw"], [0.0, 0.0], 0.2)  # Elbows neutral
#     motion.angleInterpolationWithSpeed(["LWristYaw", "RWristYaw"], [0.0, 0.0], 0.2)  # Wrists neutral
    #  Raise both arms
    make_nao_sit()
    motion.angleInterpolationWithSpeed(["LShoulderPitch", "RShoulderPitch"], [-0.5, -0.5], 0.2)  # Arms up
    motion.angleInterpolationWithSpeed(["LElbowYaw", "RElbowYaw"], [-1.5, 1.5], 0.2)  # Elbows out

    # Lower elbows
    # motion.angleInterpolationWithSpeed(["LElbowRoll", "RElbowRoll"], [-1.5, 1.5], 0.3)  # Elbows down
    time.sleep(0.3)

    # Raise elbows back up
    # motion.angleInterpolationWithSpeed(["LElbowRoll", "RElbowRoll"], [-0.5, -0.5], 0.1)  # Elbows up
    # time.sleep(0.3)
        # # motion.angleInterpolationWithSpeed(["LElbowYaw", "RElbowYaw"], [0.0, 0.0], 0.2)  # Elbows neutral
    # # motion.angleInterpolationWithSpeed(["LElbowRoll", "RElbowRoll"], [0.0, 0.0], 0.2)  # Wrists neutral

    # Lower arms back to neutral
    # motion.angleInterpolationWithSpeed(["LElbowRoll", "LElbowRoll"], [1.5, -1.5], 0.2)  # Elbows neutral
    # motion.angleInterpolationWithSpeed(["LShoulderPitch", "RShoulderPitch"], [0.4, 0.4], 0.2)  # Arms down
    # # motion.angleInterpolationWithSpeed(["LElbowRoll", "RElbowRoll"], [0.0, 0.0], 0.2)  # Wrists neutral

    postureProxy.goToPosture("Sit", 0.5)  # Use "Sit" posture for a more stable position



# Main sequence for interaction
def interaction_sequence():
    # Start by making the robot stand up straight
    # stand_up()

    # Add a greeting wave
    make_nao_sit()
    time.sleep(2)
    wave_hand()
    time.sleep(7)
    make_nao_sit()
    # nod_head()

def make_nao_sit():
    motion.wakeUp()
    postureProxy.goToPosture("Sit", 0.5)
    print("Nao has safely sat down.")

import time
from proxy import postureProxy, motion

# Example Function to make NAO stand up
def stand_up():
    motion.wakeUp()  # Activate NAO's motors
    postureProxy.goToPosture("Crouch", 0.5)  # Transition through a crouch for stability
    time.sleep(2)  # Allow time for balance
    postureProxy.goToPosture("Stand", 0.5)   # Move to standing posture
    print("Nao has safely stood up.")

# Example Function to make NAO sit down
def sit():
    motion.wakeUp()  # Activate NAO's motors
    postureProxy.goToPosture("Sit", 0.5)  # Move to sitting posture
    print("Nao has safely sat down.")


# Example Function to make NAO wave its hand
def wave_hand():
    # Lift the right arm to prepare for waving
    motion.angleInterpolationWithSpeed("RShoulderPitch", -0.5, 0.2)  # Arm up
    motion.angleInterpolationWithSpeed("RElbowYaw", 1.5, 0.2)         # Elbow out to the side

    # Perform the waving motion by rotating the wrist back and forth
    for _ in range(3):  # Repeat 3 times for a waving gesture
        motion.angleInterpolationWithSpeed("RWristYaw", -1.0, 0.2)  # Rotate hand outward
        motion.angleInterpolationWithSpeed("RWristYaw", 1.0, 0.2)   # Rotate hand inward

    # Return the arm to its resting position
    motion.angleInterpolationWithSpeed("RShoulderPitch", 1.5, 0.2)  # Arm down
    motion.angleInterpolationWithSpeed("RElbowYaw", 0.0, 0.2)       # Elbow back in
    motion.angleInterpolationWithSpeed("RWristYaw", 0.0, 0.2)       # Wrist to neutral

# Example Function to make NAO nod its head
def nod_head():
    motion.setStiffnesses("Head", 1.0)  # Enable head movement

    names = ["HeadPitch"]               # Define the joint for nodding
    angles = [0.2, -0.2]                # Nod down and then up
    times = [1.0, 2.0]                  # Timing for the nod motion
    isAbsolute = True                   # Move to absolute angles

    # Perform head nodding motion
    motion.angleInterpolation(names, angles, times, isAbsolute)
    motion.setStiffnesses("Head", 0.0)  # Relax the head after nodding

# Example Function to introduce NAO with natural body language
def introduce_nao():
    motion.angleInterpolationWithSpeed("HeadYaw", 0.3, 0.2)          # Small, friendly head tilt
    motion.angleInterpolationWithSpeed("RShoulderPitch", 1.0, 0.2)  # Slightly raise right arm for a welcoming gesture

# Example Function for a celebration gesture
def celebration():
    sit()  # Start in a seated position for stability
    motion.angleInterpolationWithSpeed(["LShoulderPitch", "RShoulderPitch"], [-0.5, -0.5], 0.2)  # Raise both arms in celebration
    motion.angleInterpolationWithSpeed(["LElbowYaw", "RElbowYaw"], [-1.5, 1.5], 0.2)             # Elbows out to create an expressive pose
    time.sleep(0.3)  # Brief pause to emphasize the pose
    postureProxy.goToPosture("Sit", 0.5)  # Return to a stable sitting position

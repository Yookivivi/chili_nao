from naoqi import ALProxy

# ============================
# Robot Configuration
# ============================

# Replace with your robot's credentials if needed
username = 'nao'                 # NAO's username (used for CHILI Nao, if applicable)
password = 'naotravelstochili'    # NAO's password (used for CHILI Nao, if applicable)

# Replace with Pepper's IP address and port
PEPPER_IP = "192.168.1.117"       # Robot's IP address
PEPPER_PORT = 9559                # NAOqi's default communication port

# ============================
# Basic Connection Test (Optional)
# ============================

# Uncomment to verify the connection and NAOqi version
# proxy = ALProxy("ALSystem", PEPPER_IP, PEPPER_PORT)
# print(proxy.systemVersion())  # Displays the NAOqi version running on the robot

# ============================
# Motion and Posture Control
# ============================

# Establish connections to key motion-related services
motion = ALProxy("ALMotion", PEPPER_IP, PEPPER_PORT)      # Controls robot's body movements
memory = ALProxy("ALMemory", PEPPER_IP, PEPPER_PORT)      # Accesses the robot's memory (e.g., sensor data)
postureProxy = ALProxy("ALRobotPosture", PEPPER_IP, PEPPER_PORT)  # Manages robot's postures

# ============================
# Face Tracking Setup
# ============================

# Setup face tracking
tracker = ALProxy("ALTracker", PEPPER_IP, PEPPER_PORT)
tracker.registerTarget("Face", 1)      # Registers "Face" as the tracking target (1 = approximate face size in meters)
tracker.track("Face")                  # Starts tracking the registered face
tracker.setMode("Head")                 # Makes only the head move to track the face
motion.setStiffnesses("Head", 1.0)     # Ensures the head is active and responsive

print("NAO is now tracking the user's face.")

# ============================
# Disable Autonomous Behaviors
# ============================

# Disabling built-in autonomous reactions to have full control over the robot
autonomous_life = ALProxy("ALAutonomousLife", PEPPER_IP, PEPPER_PORT)
autonomous_life.setState("disabled")   # Turns off autonomous life features

# Stop basic awareness (like automatic head movements to sounds)
basic_awareness = ALProxy("ALBasicAwareness", PEPPER_IP, PEPPER_PORT)
basic_awareness.stopAwareness()        # Stops the robot's basic awareness module

# ============================
# Audio Configuration
# ============================

# Audio device proxy to control input/output volume
audio = ALProxy("ALAudioDevice", PEPPER_IP, PEPPER_PORT)
audio.closeAudioInputs()               # Disables microphones to prevent the robot from listening

# Stop any ongoing microphone recordings
audio_recorder = ALProxy("ALAudioRecorder", PEPPER_IP, PEPPER_PORT)
audio_recorder.stopMicrophonesRecording()

# Manage audio playback settings
audio_player = ALProxy("ALAudioPlayer", PEPPER_IP, PEPPER_PORT)
audio.setOutputVolume(100)             # Sets speaker volume (0-100)

# ============================
# (Optional) Speech Capabilities
# ============================

# Uncomment if you need text-to-speech or dialog capabilities
# tts = ALProxy("ALTextToSpeech", PEPPER_IP, PEPPER_PORT)  # Enables text-to-speech
# dialog = ALProxy("ALDialog", PEPPER_IP, PEPPER_PORT)     # Dialog system for conversation-like interactions

# ============================
# (Optional) Speech Recognition
# ============================

# Uncomment if you want the robot to recognize specific words
# asr = ALProxy("ALSpeechRecognition", PEPPER_IP, PEPPER_PORT)
# asr.unsubscribe("Test_ASR")                 # Clean slate for ASR
# asr.setLanguage("English")                 # Set language for recognition
# vocab = ["yes", "no", "hello", "start"]    # Words to recognize
# asr.pause(True)                            # Pause before setting vocabulary
# asr.setVocabulary(vocab, True)             # Set vocabulary (True = word spotting enabled)

# ============================
# (Optional) Microphone Volume Control
# ============================

# Uncomment to adjust microphone sensitivity
# audio_device = ALProxy("ALAudioDevice", PEPPER_IP, PEPPER_PORT)
# audio_device.setInputVolume(0)  # Set mic input volume (0 = mute, 100 = max)

#import sys
#sys.path.append('/Users/yujingzhang/Documents/nao/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231/lib/python2.7/site-packages')
#import naoqi
from naoqi import ALProxy

username = 'nao'  # Username for Nao robot
password = 'naotravelstochili'  # Password for Nao robot (if applicable)

PEPPER_IP = "192.168.1.117"  # Replace with Pepper's IP
PEPPER_PORT = 9559


# Initialize proxies for required services
# tts = ALProxy("ALTextToSpeech", PEPPER_IP, PEPPER_PORT)
# dialog = ALProxy("ALDialog", PEPPER_IP, PEPPER_PORT)
motion = ALProxy("ALMotion", PEPPER_IP, PEPPER_PORT)
memory = ALProxy("ALMemory", PEPPER_IP, PEPPER_PORT)
# Speech recognition setup (Optional Extension)
# asr = ALProxy("ALSpeechRecognition", PEPPER_IP, PEPPER_PORT)
#asr.unsubscribe("Test_ASR")
# asr.setLanguage("English")
# vocab = ["yes", "no", "hello", "start"]
# asr.pause(True)
# asr.setVocabulary(vocab, True)

# Initialize proxies
tracker = ALProxy("ALTracker", PEPPER_IP, PEPPER_PORT)
# # Set the mode to "Move" to adjust body position while tracking
tracker.setMode("Head")
# Start tracking the face
tracker.registerTarget("Face", 1)  # 1 is the face size estimation in meters
tracker.track("Face")

motion.setStiffnesses("Head", 1.0)  # Ensure head movement is active
print("Nao is now tracking the user's face.")

# Connect to the ALAutonomousLife service
autonomous_life = ALProxy("ALAutonomousLife", PEPPER_IP, PEPPER_PORT)

# Set the robot to "disabled" state
autonomous_life.setState("disabled")

speech_recognition = ALProxy("ALSpeechRecognition", PEPPER_IP, PEPPER_PORT)
speech_recognition.pause(True)

# Connect to ALBasicAwareness
basic_awareness = ALProxy("ALBasicAwareness", PEPPER_IP, PEPPER_PORT)

# Stop all basic awareness behaviors
basic_awareness.stopAwareness()

print("Autonomous Life disabled.")

audio = ALProxy("ALAudioDevice", PEPPER_IP, PEPPER_PORT)
# # Set the input volume for the microphone
audio.closeAudioInputs()
print("Audio inputs are now disabled (microphone off).")

# print("Microphone channels are enabled and volume is set.")

audio_recorder = ALProxy("ALAudioRecorder",  PEPPER_IP, PEPPER_PORT)
audio_recorder.stopMicrophonesRecording()
audio_player = ALProxy("ALAudioPlayer", PEPPER_IP, PEPPER_PORT)
audio.setOutputVolume(100)
# audio_device = ALProxy("ALAudioDevice", PEPPER_IP, PEPPER_PORT)
# audio_device.setInputVolume(0)
# Proxies for movement and speech
motionProxy = ALProxy("ALMotion", PEPPER_IP, PEPPER_PORT)
postureProxy = ALProxy("ALRobotPosture", PEPPER_IP, PEPPER_PORT)
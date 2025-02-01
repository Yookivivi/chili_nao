# Import NAOqi libraries
import time
from proxy import audio_player, tracker
from robot_motion import wave_hand, stand_up, nod_head, interaction_sequence, celebration
from transfer_file_to_nao import transfer_file_to_nao, transfer_file_from_nao
from proxy import PEPPER_IP, PEPPER_PORT, username, password
from naoqi import ALProxy
# from speech_recognition import start_listening, respond_to_user

def celebration_phase():
    celebration()

def introduction_phase():
    # local_file_path = "audio_file/playlist/lbt_pre.wav"
    nao_file_path = "/home/nao/lbtaudio/playlist/self_intro.wav"
    # transfer_file_to_nao(local_file_path, nao_file_path, PEPPER_IP, username, password)
    interaction_sequence()
    audio_player.playFile(nao_file_path)
    # tracker.setMode("Head")
    # # Start tracking the face
    # tracker.registerTarget("Face", 1)  # 1 is the face size estimation in meters
    # tracker.track("Face")
    # #motion.setStiffnesses("Head", 1.0)  # Ensure head movement is active
    # print("Nao is now tracking the user's face.")
    # tts.say("Can you help me learn some English words today?")
    # user_response= start_listening()
    # if user_response:
    #     respond_to_user(user_response)
    # else:
    #     tts.say("I didn't catch that. Could you repeat?")
    # tts.say("let's start learning")
    #time.sleep(2)

# def teaching_phase(words):
#     for word in words:
#         tts.say("Can you teach me how to say the word {}? I will listen closely and try to say it after you".format(word))
#         time.sleep(3)  # Wait for the child to say the word
#         pepper_response(word)
#         time.sleep(2)


# def pepper_response(word):
#     # Simulating an intentional mispronunciation (For example, changing "cat" to "caat")
#     wrong_pronunciation = word.replace("a", "aa")  # Simple simulation of a mistake
#     tts.say("Did I say that right? {}? Oh no, that does not sound right".format(wrong_pronunciation))
#     time.sleep(2)
#     tts.say("You are the teacher! Can you help me say it the right way?")
#     time.sleep(2)

# # 4. Feedback Phase (Encouragement)
# def feedback_phase():
#     tts.say("Yes! I did it! Thanks to your awesome teaching")
#     time.sleep(2)
#     tts.say("You are really good at this. Let's try another word")
#     time.sleep(2)

# # 5. Ending Phase
# def ending_phase():
#     tts.say("Wow! I've learned so much from you today.")
#     time.sleep(2)
#     tts.say("You are a fantastic teacher. Can we do this again tomorrow?")
#     time.sleep(2)

#introduction_phase()

from ice_breaking import introduction_phase, celebration_phase
from proxy import PEPPER_IP, username, password, audio_player, tracker, motion
from transfer_file_to_nao import transfer_file_to_nao
import shutil
import qi
import time
import os
from flask import Flask, jsonify
import requests
import glob
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app) 




BACKEND_URL = "http://127.0.0.1:5000"  # Replace with your backend URL

# current_word_id=0
# def connect_to_nao(ip, port):
#     session = qi.Session()response = requests.get(f"{BACKEND_URL}/get_word/{current_word_id}")

#Use glob to find all files in the directory

files = glob.glob(os.path.join("audio_file/playlist", '*'))

# Loop through and delete each file
for file in files:
    if os.path.basename(file) != "self_intro.wav" and os.path.basename(file) != "lbt_pre.wav":
        try:
            os.remove(file)
            # print(f"Deleted: {}")
        except Exception as e:
            print("Error deleting")


@app.route('/nao/play_lbt_audio/<word>', methods=['POST'])
def play_lbt_audio(word):
    # print("Received request to play audio for word: {}".format(word))
    try:
        # Ensure word is URL-encoded
        encoded_word = word.encode('utf-8')

        nao_file_path = "/home/nao/lbtaudio/playlist/{}.wav".format(encoded_word)

        audio_player.playFile(nao_file_path)
        # is_tracking = tracker.isTargetTracked()
        # print("Is target being tracked:", is_tracking)


        return jsonify({"message": "Audio played successfully."})

    except Exception as e:
        print("Error: {}".format(str(e)))  # Print the error message for debugging
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/nao/get_lbt_audio/<word>/<path:path>', methods=['POST'])
def get_lbt_audio(path, word):
    # print("Word is: {}".format(word))
    local_file_path = "audio_file/playlist/{}.wav".format(word.encode('utf-8'))
    nao_file_path = "/home/nao/lbtaudio/playlist/{}.wav".format(word.encode('utf-8'))

    # Ensure path is properly encoded to UTF-8
    encoded_path = path.encode('utf-8')

    # Get the audio data from the backend
    word_audio_response = requests.get("{}/get_audio_for_nao/{}".format(BACKEND_URL, encoded_path))

    # Save the audio content
    with open(local_file_path, 'wb') as f:
        f.write(word_audio_response.content)

    transfer_file_to_nao(local_file_path, nao_file_path, PEPPER_IP, username, password)
    print("Audio file saved from {} to {}".format(local_file_path, nao_file_path))
    # is_tracking = tracker.isTargetTracked()
    # print("Is target being tracked:", is_tracking)
    return jsonify({"message": "Audio transferred successfully."})


@app.route('/nao/update_lbt_audio/<word>/<path:path>', methods=['POST'])
def update_lbt_audio(path, word):
    # print("Word is: {}".format(word))
    local_file_path = "audio_file/playlist/{}.wav".format(word.encode('utf-8'))
    nao_file_path = "/home/nao/lbtaudio/playlist/{}.wav".format(word.encode('utf-8'))

    # Ensure path is properly encoded to UTF-8
    encoded_path = path.encode('utf-8')
    print("encoded path", encoded_path)

    # Get the audio data from the backend
    word_audio_response = requests.get("{}/get_audio_for_nao/{}".format(BACKEND_URL, encoded_path))
    
    # Save the audio content
    with open(local_file_path, 'wb') as f:
        f.write(word_audio_response.content)

    transfer_file_to_nao(local_file_path, nao_file_path, PEPPER_IP, username, password)
    print("Audio file saved from {} to {}".format(local_file_path, nao_file_path))
    audio_player.playFile(nao_file_path)
    # is_tracking = tracker.isTargetTracked()
    # print("Is target being tracked:", is_tracking)
    time.sleep(10)
    return jsonify({"message": "Audio transferred successfully."})


@app.route('/nao/introduce', methods=['GET'])
def nao_say():
    introduction_phase()
    active_target = tracker.getActiveTarget()
    if active_target == "Face":
        print("The robot is actively tracking the face.")
    else:
        print("The robot is not tracking the face.")
    tracker.setMode("Head")
    # Start tracking the face
    tracker.registerTarget("Face", 1)  # 1 is the face size estimation in meters
    tracker.track("Face")

    motion.setStiffnesses("Head", 1.0)  # Ensure head movement is active

    if active_target == "Face":
        print("The robot is actively tracking the face.")
    else:
        print("The robot is not tracking the face.")

    return jsonify({"status": "success"})

@app.route('/nao/celebration', methods=['GET'])
def nao_celebrate():
    celebration_phase()
    active_target = tracker.getActiveTarget()
    if active_target == "Face":
        print("The robot is actively tracking the face.")
    else:
        print("The robot is not tracking the face.")
    tracker.setMode("Head")
    # Start tracking the face
    tracker.registerTarget("Face", 1)  # 1 is the face size estimation in meters
    tracker.track("Face")
    motion.setStiffnesses("Head", 1.0)  # Ensure head movement is active

    if active_target == "Face":
        print("The robot is actively tracking the face.")
    else:
        print("The robot is not tracking the face.")

    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Different port for NAO control


# NAO Robot Basic Control Tutorial

This repository contains basic code and explanations to control the NAO robot in Chili Lab.

## Environment Setup

### Python Version
- Required: **Python 2.7.18**  
  *Note:* The NAO robot controller is not compatible with newer Python versions.

### Install Required Packages
```bash
[Path to Python 2.7.18] -m pip install -r requirements.txt
```

### Install NAOqi SDK
- Version: **2.1.2.17**  
- [Download Link](https://drive.google.com/drive/folders/1PCg9qDySdTktadaOfWFolK0RKZ5wKZ_V?usp=sharing)

Ensure there are no errors when running:
```python
import naoqi
```

---

### NAO Turn-on and Turn-off

Although the official documentation states that turning on the robot requires a short click on the chest button ([NAO Turn-on Guide](http://doc.aldebaran.com/2-8/family/nao_user_guide/nao-turn-on.html)), the NAO robot in the CHILI lab requires a long press of the chest button until the LED lights turn on.

After that, wait approximately 3-4 minutes (sometimes longer if there are updates in progress; for detailed information, refer to the [NAO Boot Process Guide](http://doc.aldebaran.com/2-8/family/nao_user_guide/boot_process_nao.html#boot-process-nao)).

When the NAO says "OGNAK GNOUK," it has successfully powered on.

To turn off the NAO, ensure it is in a safe, stable area, then long-press the chest button until all the LED lights are off.


### Connecting to NAO

1. **Network Setup:**  
   Connect both the NAO robot and your computer to the same Wi-Fi network.  
   **Note:** Avoid networks requiring login credentials (e.g., school networks). Use:
   - **Wi-Fi Name:** `Clem-is-excited`  
   - **Password:** `naotravelstochili`

2. **Get NAO's IP Address:**  
   Press the chest button (short press). NAO will announce its IP address (e.g., `192.168.1.117`).

3. **Access NAO's Web Interface:** *(Optional but useful)*  
   - Open a browser and go to `http://[NAO_IP]` or `nao.local`.
   - Login:  
     - **Username:** `nao`  
     - **Password:** `naotravelstochili`
   - This interface allows you to adjust settings like voice, battery status, etc.

4. **Configure IP in Code:**  
   - In `proxy.py`, set `PEPPER_IP` to NAO's IP address.

#### Connecting to a New Network
- Via NAO's Web Interface: Navigate to the network settings, click "Add Network," and input the necessary credentials.
- If NAO is not connected to any network:
   - Use an Ethernet cable to connect NAO, like [Wired Connection Guide](http://doc.aldebaran.com/2-8/family/nao_user_guide/nao-connecting.html)
   - Visit `http://nao.local` to manage network settings.

### Code Overview
- All basic NAO setup details are in `proxy.py` with detailed comments.

---

## Motion Control

- Use `ALRobotPosture` and `ALMotion`, defined in `proxy.py`, to control motions.
- Example motions can be found in `robot_motion.py`.
- Documentation:
   - [ALRobotPosture](http://doc.aldebaran.com/1-14/naoqi/motion/alrobotposture.html)
   - [ALMotion API](https://fileadmin.cs.lth.se/robot/nao/doc/naoqi/motion/almotion-api.html)

---

## Audio Playback (WAV Format)

### Uploading Audio Files to NAO

#### Method 1: Using Choregraphe (Ubuntu in Chili Lab)
1. Open Choregraphe.
2. Connect to NAO (Wi-Fi icon should turn green).
3. Navigate: `Connect > Advanced > File Transfer`.
4. Upload audio files to NAO's shared folder.

#### Method 2: Using SSH (via `transfer_file_to_nao.py`)
Example to upload and play an audio file:
```python
remote_audio_path = "/home/nao/audio/wav/lbt_pre_1.wav"
transfer_file_to_nao("audio_file/lbt_pre_1.wav", remote_audio_path, PEPPER_IP, username, password)
audio_player.playFile(remote_audio_path)
```
*Note:* If the file is static, upload it once and reuse it.

### Playing Audio Files
```python
from proxy import audio_player

nao_file_path = "/home/nao/audio/wav/filename.wav"
audio_player.playFile(nao_file_path)
```

---

## Additional Functionalities

### Text-to-Speech (TTS)
- Uses `ALTextToSpeech` (configured in `proxy.py`).
- Guide: [TTS Documentation](http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-tuto.html)

### Speech Recognition
- Uses `ALSpeechRecognition`.
- Guide: [Speech Recognition Documentation](http://doc.aldebaran.com/2-8/naoqi/audio/alspeechrecognition.html)

---

## Troubleshooting
- Ensure Python 2.7.18 is active when running scripts.
- Verify network connections if NAO is unresponsive.
- Check NAO's battery status via the web interface.

For any issues, refer to the NAOqi official documentation or contact the Chili Lab support team.

---

# Robotic Arm Control Project

This project demonstrates controlling a 3DOF robotic arm using Python. It integrates voice commands, natural language parsing (Google Gemini), inverse kinematics, servo control, and camera capture. 

- **intent_parser.py**: Uses Google Gemini (Gemini-2.5-Pro) to parse commands into action, color, object:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}.
- **voice_command.py**: Captures microphone input with SpeechRecognition and Google’s Web Speech API.
- **inverse_kinematics.py**: Computes joint angles from a 3D (x, y, z) position for the arm (3 DOF).
- **servo_controller.py**: Controls servos via the PCA9685 (Adafruit) PWM driver over I2C (channels: base, shoulder, elbow, gripper):contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}.
- **camera_capture.py**: Captures an image using the Raspberry Pi camera (PiCamera or OpenCV):contentReference[oaicite:17]{index=17}.
- **main.py**: Command-line interface for typing commands; parses and moves the arm.
- **main_voice.py**: Voice-activated interface using microphone input and Gemini parsing.

## Setup

1. Run `chmod +x setup.sh` and then `./setup.sh` to install system and Python dependencies.
2. Obtain a Google Gemini API key (Gemini 2.5 Pro) and save it in a file named `.env` at the project root, e.g.:
3. Connect and power the Raspberry Pi camera and the PCA9685 servo driver. Attach servos on channels 0-3.
4. Adjust the link lengths in `inverse_kinematics.py` and object positions in `main.py`/`main_voice.py` as needed.

## Usage

- **Text commands:** Run `python3 main.py` and enter a command such as `pick up the red ball`.  The program will print the parsed intent and the servo movements.
- **Voice commands:** Run `python3 main_voice.py` and speak a command such as “move the green cube”. The program will recognize your speech and perform the motion.

This end-to-end demo shows voice capture, NLP parsing, inverse kinematics, and servo control working together:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}.

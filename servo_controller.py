# robotic-arm/servo_controller.py
import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Define PCA9685 channels for joints
BASE_CHANNEL     = 0
SHOULDER_CHANNEL = 1
ELBOW_CHANNEL    = 2
GRIPPER_CHANNEL  = 3

# Initialize I2C and PCA9685
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # 50 Hz for servos:contentReference[oaicite:7]{index=7}

# Create servo objects (Adafruit ServoKit uses similar Servo class)
base_servo     = servo.Servo(pca.channels[BASE_CHANNEL])
shoulder_servo = servo.Servo(pca.channels[SHOULDER_CHANNEL])
elbow_servo    = servo.Servo(pca.channels[ELBOW_CHANNEL])
gripper_servo  = servo.Servo(pca.channels[GRIPPER_CHANNEL])

def set_base(angle):
    print(f"Setting base to {angle}°")
    try:
        base_servo.angle = angle
    except:
        print("[Simulated] Base servo moved.")

def set_shoulder(angle):
    print(f"Setting shoulder to {angle}°")
    try:
        shoulder_servo.angle = angle
    except:
        print("[Simulated] Shoulder servo moved.")

def set_elbow(angle):
    print(f"Setting elbow to {angle}°")
    try:
        elbow_servo.angle = angle
    except:
        print("[Simulated] Elbow servo moved.")

def set_gripper(angle):
    print(f"Setting gripper to {angle}°")
    try:
        gripper_servo.angle = angle
    except:
        print("[Simulated] Gripper servo moved.")

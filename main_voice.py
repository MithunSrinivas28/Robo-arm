# robotic-arm/main_voice.py
import voice_command
import intent_parser
import inverse_kinematics
import servo_controller

def main():
    print("Please say a command (e.g. 'pick up the blue cube').")
    command = voice_command.listen()
    if not command:
        print("No command detected.")
        return
    print(f"Heard command: {command}")
    intent = intent_parser.parse_intent(command)
    print(f"Parsed intent: {intent}")
    # Example hard-coded object positions
    if intent.get("object") == "cube" and intent.get("color") == "blue":
        x, y, z = 15, 0, 5
    else:
        print("Unknown object/color; using default position (0,0,0).")
        x, y, z = 0, 0, 0
    try:
        base, shoulder, elbow = inverse_kinematics.calculate_angles(x, y, z)
        print(f"Computed joint angles: base={base:.1f}, shoulder={shoulder:.1f}, elbow={elbow:.1f}")
        servo_controller.set_base(base)
        servo_controller.set_shoulder(shoulder)
        servo_controller.set_elbow(elbow)
    except Exception as e:
        print(f"Error in kinematics or servo control: {e}")

if __name__ == "__main__":
    main()

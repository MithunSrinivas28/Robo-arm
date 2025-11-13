# robotic-arm/main.py
import intent_parser
import inverse_kinematics
import servo_controller

def main():
    command = input("Enter command (e.g. 'pick up the red ball'): ")
    intent = intent_parser.parse_intent(command)
    print(f"Intent parsed: {intent}")
    # Example hard-coded object positions
    if intent.get("object") == "ball" and intent.get("color") == "red":
        x, y, z = 10, 5, 2
    else:
        print("Unknown object/color; using default position (0,0,0).")
        x, y, z = 0, 0, 0
    try:
        base, shoulder, elbow = inverse_kinematics.calculate_angles(x, y, z)
        print(f"Moving to angles: base={base:.1f}, shoulder={shoulder:.1f}, elbow={elbow:.1f}")
        servo_controller.set_base(base)
        servo_controller.set_shoulder(shoulder)
        servo_controller.set_elbow(elbow)
    except Exception as e:
        print(f"Error in kinematics or servo control: {e}")

if __name__ == "__main__":
    main()

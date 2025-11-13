# robotic-arm/inverse_kinematics.py
import math

# Example link lengths (adjust to your arm's dimensions)
L1 = 10.0  # length of first arm segment
L2 = 10.0  # length of second arm segment

def calculate_angles(x, y, z):
    """
    Given a target (x, y, z), compute (base, shoulder, elbow) joint angles in degrees.
    Assumes base rotates around Z, and shoulder/elbow form a planar 2-link arm.
    """
    # Base rotation angle
    base_angle = math.degrees(math.atan2(y, x))
    # Planar distance to target
    r = math.sqrt(x*x + y*y)
    d = math.sqrt(r*r + z*z)
    # Check reachability
    if d > (L1 + L2) or d < abs(L1 - L2):
        raise ValueError("Target is out of reach")
    # Law of cosines
    cos_alpha = (L1*L1 + L2*L2 - d*d) / (2 * L1 * L2)
    cos_alpha = max(min(cos_alpha, 1.0), -1.0)
    alpha = math.acos(cos_alpha)
    cos_beta = (L1*L1 + d*d - L2*L2) / (2 * L1 * d)
    cos_beta = max(min(cos_beta, 1.0), -1.0)
    beta = math.acos(cos_beta)
    # Compute angles
    shoulder_angle = math.degrees(math.atan2(z, r) + beta)
    elbow_angle    = math.degrees(math.pi - alpha)
    return base_angle, shoulder_angle, elbow_angle

# robotic-arm/camera_capture.py
import time
try:
    from picamera import PiCamera
except ImportError:
    import cv2  # use OpenCV if picamera is not available

def capture_image(filename="image.jpg"):
    """
    Capture an image from the Pi camera and save to filename.
    """
    try:
        camera = PiCamera()
        camera.resolution = (640, 480)
        time.sleep(2)  # camera warm-up
        camera.capture(filename)
        camera.close()
        print(f"Image captured to {filename}")
    except Exception:
        # Fall back to OpenCV capture
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(filename, frame)
                print(f"Image saved to {filename}")
            cap.release()

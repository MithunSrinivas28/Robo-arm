# robotic-arm/voice_command.py
import speech_recognition as sr

def listen():
    """
    Capture speech from the microphone and return the recognized text (English).
    Uses the SpeechRecognition library with Google Web Speech API.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    return ""

# voice/voice_output.py

import pyttsx3


# Initialize Text-to-Speech engine
engine = pyttsx3.init()


def speak(message):
    """
    Convert text into speech.
    """

    print("Voice:", message)

    engine.say(message)
    engine.runAndWait()


def obstacle_alert(object_name, distance, direction):
    """
    Give voice warning when an obstacle is detected.
    """

    message = (
        f"Obstacle detected. "
        f"{object_name} is {distance} meters away. "
        f"Move {direction}."
    )

    speak(message)


def turn_instruction(direction):
    """
    Give turning instruction.
    """

    speak(f"Turn {direction}.")


def continue_forward():
    """
    Tell the user to continue forward.
    """

    speak("Keep going.")


def destination_reached(destination):
    """
    Inform the user that the destination is reached.
    """

    speak(f"Destination reached. You are at {destination}.")


def welcome_message():
    """
    Starting message.
    """

    speak("Smart Indoor Path Guidance System started.")


# Test the voice module
if __name__ == "__main__":

    print("Smart Indoor Navigation - Voice Module")
    print("---------------------------------------")

    welcome_message()

    continue_forward()

    turn_instruction("left")

    obstacle_alert(
        "chair",
        1.2,
        "right"
    )

    destination_reached("Lab 2")

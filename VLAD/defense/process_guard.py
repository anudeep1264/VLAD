import time
from voice.listener import VoiceListener
from voice.speaker import VoiceSpeaker
from brain.ai_brain import AIBrain
from defense.defense_core import DefenseCore

WAKE_WORD = "mars"

def main():
    speaker = VoiceSpeaker()
    listener = VoiceListener()
    brain = AIBrain()
    defense = DefenseCore()

    speaker.speak("System online. Say mars to wake me up.")

    while True:
        try:
            text = listener.listen()
            if not text:
                continue

            text = text.lower()
            print(f"You said: {text}")

            if WAKE_WORD in text:
                speaker.speak("Yes. I am listening.")
                command = listener.listen()

                if command:
                    print(f"Command: {command}")
                    response = brain.process(command)
                    speaker.speak(response)

            defense.monitor()

        except Exception as e:
            print("Error:", e)
            time.sleep(1)

if __name__ == "__main__":
    main()

import time
import sys
from pathlib import Path

# Ensure project root is on path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# ---------------- IMPORTS ----------------
from voice.listener import VoiceListener
from voice.speaker import Speaker
from defense.defender import Defender
from brain.ai_brain import AIBrain

# ----------------------------------------


def main():
    speaker = Speaker()
    listener = VoiceListener(wake_word="mars")  # wake word = mars
    defender = Defender(speaker)

    speaker.say("System online. Say mars to wake me up.")
    print("VLAD running... (Ctrl+C to stop)")

    try:
        while True:
            # Passive defense runs always (24/7)
            alerts = defender.scan()
            if alerts:
                for alert in alerts:
                    print("[ALERT]", alert)
                    speaker.say(alert)

            # Wait for wake word
            print("VLAD is listening...")
            listener.wait_for_wake_word()

            speaker.say("Yes. I am listening.")
            print("Wake word detected")

            # Listen for command
            command = listener.listen_command()
            if not command:
                speaker.say("I did not understand.")
                continue

            print("User said:", command)

            # --- BASIC COMMAND HANDLING (TEMP) ---
            if "open youtube" in command:
                speaker.say("Opening YouTube")
                import webbrowser
                webbrowser.open("https://www.youtube.com")

            elif "open chrome" in command:
                speaker.say("Opening Chrome")
                import os
                os.system("start chrome")

            elif "time" in command:
                speaker.say(time.strftime("The time is %H:%M"))

            elif "exit" in command or "stop" in command:
                speaker.say("Shutting down. Stay safe.")
                break

            else:
                speaker.say("Command received. AI brain will handle this soon.")

            time.sleep(1)

    except KeyboardInterrupt:
        speaker.say("System interrupted. Shutting down safely.")
        print("Exiting...")


if __name__ == "__main__":
    main()

import threading
from system.automation import Automation

class TaskRouter:

    def __init__(self, speaker, brain):
        self.speaker = speaker
        self.brain = brain

    def handle(self, command: str):
        threads = []

        # SYSTEM TASKS
        if "open youtube" in command:
            t = threading.Thread(target=self._open_youtube)
            threads.append(t)

        if "open chrome" in command:
            t = threading.Thread(target=self._open_chrome)
            threads.append(t)

        # AI THINKING (always allowed)
        t = threading.Thread(target=self._ai_reply, args=(command,))
        threads.append(t)

        for t in threads:
            t.start()

    def _open_youtube(self):
        self.speaker.speak("Opening YouTube.")
        Automation.open_youtube()

    def _open_chrome(self):
        self.speaker.speak("Opening Chrome.")
        Automation.open_chrome()

    def _ai_reply(self, command):
        reply = self.brain.think(command)
        self.speaker.speak(reply)

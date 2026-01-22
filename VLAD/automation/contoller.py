import os
import webbrowser
import subprocess

class AutomationController:

    def execute(self, command: str) -> str:
        command = command.lower()

        # Open applications
        if "open chrome" in command:
            subprocess.Popen("chrome")
            return "Opening Chrome."

        if "open notepad" in command:
            subprocess.Popen("notepad")
            return "Opening Notepad."

        if "open calculator" in command:
            subprocess.Popen("calc")
            return "Opening Calculator."

        # Open websites
        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube."

        if "open google" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Google."

        # Open files
        if "open downloads" in command:
            os.startfile(os.path.expanduser("~/Downloads"))
            return "Opening Downloads folder."

        return "Command not supported yet."

import os
import webbrowser
import subprocess

class Automation:

    @staticmethod
    def open_chrome():
        webbrowser.open("https://www.google.com")

    @staticmethod
    def open_youtube():
        webbrowser.open("https://www.youtube.com")

    @staticmethod
    def open_folder(path):
        if os.path.exists(path):
            os.startfile(path)

    @staticmethod
    def open_file(path):
        if os.path.exists(path):
            os.startfile(path)

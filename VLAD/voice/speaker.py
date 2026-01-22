import pyttsx3

class VoiceSpeaker:
    def __init__(self, voice_type="female"):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 165)
        self.set_voice(voice_type)

    def set_voice(self, voice_type):
        voices = self.engine.getProperty("voices")

        if voice_type == "female":
            for v in voices:
                if "female" in v.name.lower() or "zira" in v.name.lower():
                    self.engine.setProperty("voice", v.id)
                    break
        else:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        print("VLAD says:", text)
        self.engine.say(text)
        self.engine.runAndWait()

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

class Speaker:
    def __init__(self):
        self.source = sr.Microphone()
        self.source.__enter__()
        self.r = sr.Recognizer()

    def calibrate(self, duration=0.5):
        self.r.adjust_for_ambient_noise(self.source, duration=duration)

    def wait_for_speech(self, max_time=15.0, match_text=None):

        if match_text is None:
            print("Waiting for speech")
            r.listen(self.source, timeout=max_time, phrase_time_limit=3.0)
        else:
            print("Waiting for speech: ", match_text)
            received_text = ""
            while received_text.lower() != match_text:
                received_text = self.grab_speech(max_time=max_time)
                print("got ", received_text)

    def grab_speech(self, max_time=10.0):
        try:
            audio2 = r.listen(self.source, timeout=max_time, phrase_time_limit=max_time / 3.0)
            # Using google to recognize audio
            received_text = self.r.recognize_google(audio2)
            received_text = received_text.lower()
            return received_text

        except sr.RequestError as e:
            # print("Could not request results {0}".format(e))
            return ""
        except sr.UnknownValueError:
            # print("unknown error occurred")
            return ""
        except sr.WaitTimeoutError:
            return ""

    def speak_text(self, command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
#

if __name__=="__main__":
    speaker = Speaker()
    print("calibrating")
    speaker.calibrate()
    speaker.speak_text("talk to me")
    speaker.wait_for_speech(match_text="hey computer")
    speaker.speak_text("i got it")



# # Function to convert text to
# # speech
# def speak_text(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#
# def wait_for_speech(max_time = 10.0):
#     try:
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.1)
#
#             # listens for the user's input
#             print("Listening")
#             audio2 = r.listen(source2, timeout=max_time)
#
#     except sr.RequestError as e:
#         print("Could not request results {0}".format(e))
#
#     except sr.UnknownValueError:
#         print("unknown error occurred")
#
# def grab_speech(max_time=10.0):
#     try:
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.05)
#
#             # listens for the user's input
#             print("Listening")
#             audio2 = r.listen(source2, timeout=max_time)
#
#             print("Converting")
#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
#     except sr.RequestError as e:
#         print("Could not request results {0}".format(e))
#
#     except sr.UnknownValueError:
#         print("unknown error occurred")
#     return MyText
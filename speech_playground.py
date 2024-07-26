import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def speak_text(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def grab_speech(max_time=10.0):
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            print("Listening")
            audio2 = r.listen(source2, timeout=10)

            print("Converting")
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
    except sr.RequestError as e:
        print("Could not request results {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
    return MyText

if __name__=="__main__":
    while (1):
        text = grab_speech(10.0)

        print("Did you say: \n\"", text, "\"")
        speak_text(text)


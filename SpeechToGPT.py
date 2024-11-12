import speech_recognition as sr;

def main():
    speech_to_text()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("start speaking...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            print("you said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

if __name__ == "__main__":
    main()


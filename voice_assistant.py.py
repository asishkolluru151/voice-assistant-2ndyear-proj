import speech_recognition as sr
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please say something.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
def handle_command(command):
    if "weather" in command:
        print("Checking the weather... It's sunny and 25°C outside.")
    elif "hello" in command or "hi" in command:
        print("Hello! How can I assist you today?")
    elif "exit" in command or "quit" in command:
        print("Goodbye!")
        return False
    else:
        print("Sorry, I don't know that command.")
    return True

def main():
    running = True
    while running:
        command = recognize_speech()
        if command:
            running = handle_command(command)
if __name__ == "__main__":
    main()

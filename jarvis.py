import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import re

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


# Create a function to save reminders to a text file
def saveReminder(reminder):
    with open("reminders.txt", "a") as file:
        file.write(reminder + "\n")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello boss, what can I do for you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        if "ok bye friday" in query.lower():
            speak("Bye, sir, see you later")
            exit()

    except Exception as e:
        speak("Sorry boss, can you repeat the statement?")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open replete" in query:
            webbrowser.open("www.replit.com")
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        elif "open amazon prime" in query:
            webbrowser.open("https://www.primevideo.com/")
        elif "open netflix" in query:
            webbrowser.open("https://www.netflix.com/browse")
        elif "play" in query:
            speak("Finding a relevant match for you")
            query = query.replace("play", "")
            try:
                search_url = f"https://open.spotify.com/search/{query}"
                webbrowser.open(search_url)
                speak("here's what you want")

            except Exception as e:
                print(e)
                speak(
                    "Sorry, I couldn't perform the search. Please check your internet connection."
                )

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\navdeep singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif "email to navdeep" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "nsb95696@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak(
        #             "Sorry boss! Not able to send the email at this moment. Please try again."
                # )

        elif "google" in query:
            speak("Finding a relevant match for you")
            query = query.replace("google", "")
            try:
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)
                speak("Found some results for you")

            except Exception as e:
                print(e)
                speak(
                    "Sorry, I couldn't perform the search. Please check your internet connection."
                )

        elif "youtube" in query:
            speak("Finding a relevant match for you")
            query = query.replace("youtube", "")
            try:
                search_url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(search_url)
                speak("here's what you want")

            except Exception as e:
                print(e)
                speak(
                    "Sorry, I couldn't perform the search. Please check your internet connection."
                )

        # # Adding a reminder feature
        # elif "set reminder" in query:
        #     try:
        #         speak("Please enter the reminder message:")
        #         reminder_message = takeCommand()
        #         speak("Please enter the time for the reminder (in seconds):")
        #         reminder_time = int(takeCommand())
        #         saveReminder(f"Reminder: {reminder_message} at {datetime.datetime.now() + datetime.timedelta(seconds=reminder_time)}")
        #         speak("Reminder set successfully!")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, I couldn't set the reminder.")

        # # Adding an alarm feature
        # elif "set alarm" in query:
        #     try:
        #         speak("Please enter the alarm message:")
        #         alarm_message = takeCommand()
        #         speak("Please enter the time for the alarm (in seconds):")
        #         alarm_time = int(takeCommand())
        #         time.sleep(alarm_time)
        #         speak(f"Alarm: {alarm_message}")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, I couldn't set the alarm.")
# def convert_time_to_seconds(time_str):
#     # Parse time in the format "3pm" or "3am" and convert it to seconds from now
#     current_time = datetime.datetime.now()
#     specified_time = datetime.datetime.strptime(time_str, "%I%p")

#     # If the specified time is in the past, assume it's for the next day
#     if specified_time < current_time:
#         specified_time += datetime.timedelta(days=1)

#     time_difference = specified_time - current_time
#     return int(time_difference.total_seconds())


# if __name__ == "__main__":
#     wishMe()
#     while True:
#         query = takeCommand().lower()

#         if "set alarm for" in query:
#             try:
#                 # Extract the time input from the query, e.g., "set alarm for 3pm"
#                 time_input = query.replace("set alarm for", "").strip()
#                 duration = convert_time_to_seconds(time_input)
#                 if duration > 0:
#                     speak(f"Alarm set for {time_input}")
#                     # Sleep for the specified duration before sounding the alarm
#                     time.sleep(duration)
#                     speak("Time's up! Your alarm is ringing.")
#                 else:
#                     speak("Invalid time input. Please try again.")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry, I couldn't set the alarm. Please try again.")

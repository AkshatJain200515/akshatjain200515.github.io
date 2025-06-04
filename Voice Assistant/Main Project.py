import speech_recognition 
import pyttsx3
import json
import re
import random_responses
import requests
import datetime
import time
import sys
import pywikihow

speaker=pyttsx3.init('sapi5')
speaker.setProperty('rate',175)
speaker.setProperty('volume',2)
voices=speaker.getProperty('voices')
r=speech_recognition.Recognizer()
r.energy_threshold = 0
speaker.setProperty('voice',voices[1].id)
recognizer=speech_recognition.Recognizer()

def wiki():
    from pywikihow import search_wikihow
    recognizer=speech_recognition .Recognizer()
    with speech_recognition .Microphone() as source: 
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("\nListening...")
        recordedaudio=recognizer.listen(source)

    try:
        print('Ok Let me Process that !')
        how=recognizer.recognize_google(recordedaudio,language='en-in')
        print('You : ',format(how),"\n")
        max_result = 1
        how_to = search_wikihow(how, max_result)
        assert len (how_to) == 1
        how_to[0].print()
        speak(how_to[0].summary)
        home()
    except speech_recognition.UnknownValueError:
            recognizer = speech = speech_recognition.Recognizer()
            print("\nI can't hear your voice, can you please speak louder!")
            speaker.say("I can't hear your voice, can you please speak louder!")
            speaker.runAndWait()
            wiki()
            
def google(text):
    import wikipedia as google
    text = text.replace("google search for","")
    text = text.replace("search google for","")
    text = text.replace("google search","")
    text = text.replace("google","")
    text = text.replace("please","")
    text = text.replace("search","")
    try:
        result = google.summary(text,2)
        print(result)
        speak(result)
    except:
        recognizer = speech = speech_recognition.Recognizer()
        print("\nI can't found something related to your question, can you please speak something else!")
        speaker.say("I can't found something related to your question, can you please speak something else!")
        speaker.runAndWait()
        main()
        
def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir!")
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!")  
        speak("Good Afternoon Sir!")   

    else:
        print("Good Evening Sir!") 
        speak("Good Evening Sir!")  

    print("I am Climate Bot. Please tell me how may I help you Sir")
    speak("I am Climate Bot. Please tell me how may I help you Sir")  

def act():
            recognizer=speech_recognition .Recognizer()
            with speech_recognition .Microphone() as source: 
                recognizer.adjust_for_ambient_noise(source,duration=0.5)
                print("\nListening...")
                recordedaudio=recognizer.listen(source)

            try:
                recorded=recognizer.recognize_google(recordedaudio,language='en-in')
                print('You : ',format(recorded),"\n")
                if recorded == "yes":
                    speak("Please enter the city name!")
                    city_name=input("Enter the City name : ")
                    time.sleep(0.5)
                    wandt(city_name)
                else:
                    speak("No problem !")
                    home()
                    
            except speech_recognition.UnknownValueError:
                    recognizer = speech = speech_recognition.Recognizer()
                    print("\nI can't hear your voice, can you please speak louder!")
                    speaker.say("I can't hear your voice, can you please speak louder!")
                    speaker.runAndWait()
                    act()

def wandt(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature =str(int((y["temp"])-273))
        z = x["weather"]
        weather_description = str(z[0]["description"])
        weather_description=str(weather_description)
        print("The Temperature in "+ city_name + " is " + current_temperature + " degree celsius and Weather in " + city_name + " is " + weather_description + ".")
        speak("The Temperature in "+ city_name + " is " + current_temperature + " degree celcius and Weather in " + city_name + " is " + weather_description)
        print("Do I have to tell Another place temperature and weather ?")
        speak("Do I have to tell Another place temperature and weather too?  yes or no")
        act()

def weatherandtemp():
    wandt("berlin")

def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)

response_data = load_json("bot.json")

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response) 

    if input_string == "":
       return("Please say something I can reply:")

    if input_string =="what is weather today ":
        weatherandtemp()
       

    if best_response != 0:
        print(response_data[response_index]["bot_response"],"\n")
        speak(response_data[response_index]["bot_response"])
        home()
    else:
        x=random_responses.random_string()
        print(x)
        speaker.say(x)
        speaker.runAndWait()
        main()

def exit():
    sys.exit()
    
def main():
    recognizer=speech_recognition .Recognizer()
    with speech_recognition .Microphone() as source: 
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("\nListening...")
        recordedaudio=recognizer.listen(source)

    try:
        print('Ok Let me Process that !')
        text=recognizer.recognize_google(recordedaudio,language='en-in')
        text=(text.lower())
        print('You : ',format(text),"\n")
        if "weather" and "temperature" in text:
            weatherandtemp()
        if "exit" in text:
            sys.exit()
        if "wikipedia" in text:
            wiki()
        if "google" in text:
            google(text)
        else:
            get_response(text)
            home()
        home()
    except speech_recognition.UnknownValueError:
            recognizer = speech = speech_recognition.Recognizer()
            print("\nI can't hear your voice, can you please speak louder!")
            speaker.say("I can't hear your voice, can you please speak louder!")
            speaker.runAndWait()
            main()
            
def home():
    global variable
    speak("Please tell me what next I can do for you Sir")
    main()

wishMe()
main()

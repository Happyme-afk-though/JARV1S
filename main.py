import speech_recognition as sr 
import webbrowser
import pyautogui as pg
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pyaudio
import os as ass
import numpy as np


# Parameters
CHUNK = 1024  # Number of audio samples per buffer
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate (44.1kHz)
THRESHOLD = 155000  # Noise threshold

def detect_noise():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open audio stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    

    
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK)
        # Convert audio data to numpy array
        audio_data = np.frombuffer(data, dtype=np.int16)

            # Calculate the amplitude of the audio signal
        amplitude = np.linalg.norm(audio_data)

            # Detect noise
        if amplitude > THRESHOLD:
            break

        











chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# Specify the path to your Chrome driver executable

chrome_driver_path = r'C:\\Users\\u\\Desktop\\eve\\python\\chromedriver.exe'

# Create a Service object with the specified executable path
chrome_service = Service(chrome_driver_path)

# Create a Chrome driver instance with the specified options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")

# Navigate to the website

def speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        text_to_input = text
        element_to_click.send_keys(text_to_input)
        print(text_to_input)

        # Calculate sleep duration based on sentence length
        sleep_duration = min(0.1 + len(text) // 10, 100)  # Minimum sleep is 3 seconds, maximum is 10 seconds ??????

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed, e.g., log it, raise it again, etc.




def takeCommand():
    # It takes microphone input from the user and returns string.


    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        print("Listening...")
        
        #r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        
        audio = r.listen(source)


    try:
        
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        return"respond to this prompt with only a word hm"
    return query



import  google.generativeai as genai





GOOGLE_API_KEY ="AIzaSyCYnDqRBxWgB2AblN2vJ2pGM0WDuMWYHsM"
genai.configure(api_key=GOOGLE_API_KEY)
generate_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings= [
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },

]
    


model=genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generate_config,safety_settings=safety_settings)
convo = model.start_chat()






        
    
    








def main():
    detect_noise()
    while True:
        query = takeCommand().lower()
        

        

        


        if "jarvis" in query:
        
            convo.send_message("reply this with maximum 29 words and do not tell me that you are replying within 29 words or less" + query)
            speak(convo.last.text)

        
    
    

    
        elif "youtube per search karna" in query:
            query = query.replace("youtube per search karna","")
            speak("got you sir")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            #pywhatkit.playonyt(query)
            speak("which video you want me to play")





        elif 'google per search karna' in query:
            query = query.replace('google per search karna','')
            webbrowser.open("google.com")
            time.sleep(2.9)
            pg.typewrite(query)
            pg.hotkey('enter')
            speak("here are the top results.")
            time.sleep(2)

        elif "first" in query:
                pg.click(x=627, y=378)       
        elif "second" in query:
            pg.click(x=614, y=800)
        elif "stop" in query:
            pg.hotkey('k')
        elif "start" in query:
            pg.hotkey('k')
        elif "close" in query:
            pg.hotkey('alt','f4')
        elif "tab 1" in query:
            pg.hotkey("ctrl","1")
        elif "tab 2" in query:
            pg.hotkey("ctrl","2")
        elif 'band karna' in query:
            pg.hotkey('alt','f4')
        elif "close the tab" in query:
            pg.hotkey('ctrl', 'w')
        elif "skip the ad"in query:
            pg.hotkey('tab')
            pg.hotkey('tab')
            pg.hotkey('tab')
            pg.hotkey('tab')
            time.sleep(1)
            pg.hotkey('enter')


    #elif "" in query:
        #query = "respond this with nothing"
        #convo.send_message(query)
        #speak(convo.last.text)

        elif "weather" in query:
            search = "weather in sri ganganagar"
            url = f"https://www.google.co.in/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

    


        elif "tell me some tech news" in query:
            webbrowser.open("https://cybernews.com/news/")
            time.sleep(2)
            pg.hotkey("ctrl","shift","u")

        elif "show me some tech news" in query:
            webbrowser.open("https://cybernews.com/news/")
            time.sleep(2)
            pg.hotkey("ctrl","shift","u")

        elif "aaram" in query:
            speak("ok sir , call me when ever you want.")
            break

     
        elif "you can take a break now" in query:
            speak("ok sir , call me when ever you want.")
            break
    
        elif "let's trade" in query:
            pg.hotkey("win")
            time.sleep(1)
            pg.typewrite("trading")
            time.sleep(0.6)
            pg.hotkey("enter")            

        if query=="respond to this prompt with only a word hm":
            continue
        else:
            convo.send_message(query)
            speak(convo.last.text)
            
            
        
                 
            


main()
       





    
 


if __name__ == "__main__":
    while True:
    
            query = takeCommand().lower()
            if "jarvis" in query:
                speak("present sir")
                
                main()

    
    
    



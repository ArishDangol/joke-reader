# Program to download a joke from icanhazdadjoke.com
# And say it out loud using text-to-speech

    
import requests
import pyttsx3
from datetime import datetime
    
def output(text):
    print(text)
    voice.say(text)
    voice.runAndWait()
    
headers = {
    'User-Agent': 'YOUR_AGENT_NAME', # ADD YOUR OWN HERE
    'Accept': 'application/json'
}
    
try:
    data = requests.get("https://icanhazdadjoke.com/", headers=headers)
    joke = data.json().get('joke')
except:
    # standard joke here for if the random joke lookup fails
    joke = "What do clouds wear under their clothes? Thunderwear."
    
voice = pyttsx3.init()
voice.setProperty('rate', 170)
    
today = datetime.now()
day_of_week = today.strftime('%A')
output(f"This will brighten your {day_of_week}")
output(joke)

import requests
import json
import win32com.client as wincom

city = input("weather app\n enter the name of your city:\n")

r = requests.get(f"https://api.weatherapi.com/v1/current.json?key=5c654266652748b297c200239241301&q={city}")

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice")
print(f"the current weather in {city} is {w} degree celcius")
speak.speak(f"the current weather in {city} is {w} degree celcius")
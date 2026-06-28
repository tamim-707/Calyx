#Weather
import requests

def get_weather(city) :
   cities = {
        "dhaka": (23.8103, 90.4125),
        "keraniganj": (23.6833, 90.3500),
        "barishal": (22.7010, 90.3535),
        "bagerhat": (22.6516, 89.7859),
        "pirojpur": (22.5791, 89.9759)    
   }
   city = city.lower()

   if city not in cities :
      return "City not found"

   lat,lon = cities[city]

   url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
   
   try :
       response = requests.get(url,timeout=5) 
       if response.status_code != 200:
         return f"Weather API Error: {response.status_code}"
       data = response.json()
       if "current" not in data :
          return "Weather data Unavailabe"

       temp = data["current"]["temperature_2m"]
       wind = data["current"]["wind_speed_10m"]

       return f"{city.capitalize()}\nTemperature : {temp}°C\nWind Speed : {wind}km/h"

   except requests.ConnectionError :
      return "No Internet Connection!"
   except requests.Timeout:
      return "News Request Timedout!"
   except Exception as e :
      return f"Unexpcted error : {e}"
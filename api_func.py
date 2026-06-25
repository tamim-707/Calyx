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

   response = requests.get(url) 
   data = response.json()

   temp = data["current"]["temperature_2m"]
   wind = data["current"]["wind_speed_10m"]

   return f"{city.capitalize()}\nTemperature : {temp}°C\nWind Speed : {wind}km/h"

def get_news(category,country) :
   categories = [
      "sports",
      "general",
      "technology",
      "entertainment"
   ]

   category = category.lower()
   country = country.upper()
   url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=28916b043dc849e49a68eca7c5a84317 "

   if category not in categories :
      return "Category not found"
   
   response = requests.get(url)
   data = response.json()
   
   news = f"{category.capitalize()} News {country.capitalize()}\n"

   for article in data ["articles"][:3]:
      news += f"- {article['title']}\n"
   
   return news
   
import requests
import os
from dotenv import load_dotenv
load_dotenv()
news_api = os.getenv("news_api_key")
def get_news(category,country) :
   categories = [
      "sports",
      "general",
      "technology",
      "entertainment"
   ]

   category = category.lower()
   country = country.upper()
   if category not in categories :
      return "Category not found"
   
   url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={news_api} "

   try:
      response = requests.get(url,timeout=5)

      if response.status_code == 401 :
         return "Invalid News API Key"
      
      #other bad status code
      if response.status_code !=200:
         return f"API error : {response.status_code}"
      
      data = response.json()
      #news api sometimes returns error message 
      if data["status"] != "ok" :
         return data.get("message","News API error")
      if not data["articles"]:
         return "News not found"
   
      news = f"{category.capitalize()} News {country.capitalize()}\n"

      for article in data ["articles"][:3]:
       news += f"- {article['title']}\n"
   
      return news
   except requests.ConnectionError :
      return "No Internet Connection!"
   except requests.Timeout:
      return "News Request Timedout!"
   except Exception as e :
      return f"Unexpcted error : {e}"
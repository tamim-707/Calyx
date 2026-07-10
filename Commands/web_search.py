import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("tavily_api_key")

URL = "https://api.tavily.com/search"


def web_search(query):
    if not API_KEY:
        return "Error: Tavily API key not found."

    payload = {
        "api_key": API_KEY,
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        "max_results": 5,
        "include_raw_content": False,
        "include_images": False
    }

    try:
        response = requests.post(URL, json=payload, timeout=15)
        response.raise_for_status()

        data = response.json()

        # If Tavily generated an answer, use it.
        answer = data.get("answer")
        if answer:
            return answer

        # Otherwise summarize the first few search results.
        results = data.get("results", [])

        if results:
            output = "I couldn't generate a direct answer, but here's what I found:\n\n"

            for i, result in enumerate(results[:3], start=1):
                title = result.get("title", "No title")
                content = result.get("content", "No description")
                url = result.get("url", "")

                output += (
                    f"{i}. {title}\n"
                    f"{content}\n"
                    f"{url}\n\n"
                )

            return output.strip()

        return "No results found."

    except requests.exceptions.Timeout:
        return "Error: Request timed out."

    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to Tavily."

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e.response.status_code}"

    except Exception as e:
        return f"Unexpected Error: {e}"
"""
def web_search(query):
    -Creates a function to search the web.
    -query is the text the user wants to search.

url = "https://api.tavily.com/search"
    -This is the address where the search request is sent.

payload = {
        "api_key": API_KEY,
        "query": query,
        "search_depth": "basic"
    }
    -payload is a Python dictionary.
    -It contains the data sent to the API.

"api_key"
    -Proves that the request is authorized.

"query"
    -The user's search text.

"search_depth"
    -Tells Tavily how deeply to search.
    -"basic" is faster.
    -"advanced" searches more thoroughly but may take longer.

response = requests.post(url, json=payload)
    -Sends an HTTP POST request to the Tavily API.
    -json=payload automatically converts the dictionary into JSON.

response
    -Stores everything returned by the API.
    -This includes the status code and the search results.

    if response.status_code == 200:
    -Checks whether the request was successful.
    -200 means "OK" and the API returned data successfully.

data = response.json()
    -Converts the JSON response into a Python dictionary.
    -Now Python can access values using dictionary keys.

return data.get("answer", "No answer found.")
    -Gets the value of the "answer" key.
    -.get() avoids an error if the key does not exist.
    -If "answer" is missing, it returns "No answer found."

return f"Error: {response.status_code}"
    -Returns the HTTP error code.
    -Examples:
        401 -> Invalid API key
        403 -> Permission denied
        404 -> Resource not found
        429 -> Too many requests (rate limit)
        500 -> Server error

Flow
        Load .env file
        Read API key
        Receive search query
        Create request payload
        Send POST request
        Receive API response
        Check status code
        Convert JSON to dictionary
        Return answer
        Return error if request fails
"""
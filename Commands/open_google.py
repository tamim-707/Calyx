from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def google_search(query):
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com")

    search = driver.find_element(By.NAME, "q")
    search.send_keys(query)
    search.submit()
    return f"Searching Google for '{query}'."



"""
from selenium import webdriver
    -Imports Selenium's webdriver module.
    -WebDriver is used to control a web browser programmatically.

from selenium.webdriver.common.by import By
    -Imports the By class.
    -Used to locate elements on a webpage.
    -Examples:
        By.NAME
        By.ID
        By.CLASS_NAME
        By.XPATH
        By.CSS_SELECTOR

from selenium.webdriver.chrome.options import Options
    -Imports Chrome-specific browser options.
    -Allows customization of how Chrome starts.

def google_search(query):
    -Creates a function to perform a Google search.
    -query is the text the user wants to search.

options = Options()
    -Creates a Chrome Options object.
    -Used to configure Chrome before launching it.

options.add_experimental_option("detach", True)
    -"detach=True" tells Chrome to stay open after the Python program finishes.
    -Without this, Chrome usually closes when the script ends.

driver = webdriver.Chrome(options=options)
    -Starts a new Chrome browser controlled by Selenium.
    -A WebDriver object is created.
    -driver is used to control the browser.

driver.get("https://www.google.com")
    -Opens the Google homepage.
    -driver.get() navigates to the given URL.

search = driver.find_element(By.NAME, "q")
    -Finds Google's search box.
    -By.NAME means Selenium searches for an HTML element whose name attribute is "q".
    -Google's search box has:
        name="q"

search.send_keys(query)
    -Types the user's query into the search box.
    -send_keys() simulates keyboard typing.

search.submit()
    -Presses Enter automatically.
    -Submits the search form and displays the search results.
    
Flow
    Create Chrome options
    Enable detach mode
    Launch Chrome
    Open Google
    Find the search box
    Type the user's query
    Press Enter
    Display Google search results
    Return confirmation message
"""
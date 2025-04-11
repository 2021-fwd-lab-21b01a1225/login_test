# Intervue.io Automation Script

This project is a simple automation script built with Python and Selenium. It simulates a real user visiting Intervue.io, logging in as a company user, performing a search, and logging out — all through a Chrome browser.

---

## What This Script Does:

1. Opens the Intervue.io homepage  
2. Clicks the Login button and switches to the login tab  
3. And click on the login for companies  
4. Logs in using company credentials (email & password)  
5. Searches for the word "hello" on the dashboard  
6. Clicks on a user profile from the results  
7. Logs out of the application  

---

## 📋 What You’ll Need

To run this script, make sure you have:

1. Python 3.x  
2. Google Chrome installed on your machine  
3. ChromeDriver that matches your Chrome browser version  
4. The Selenium package  

---

## ⚙️ Setting It Up

Clone this repo or download the script file.

Install Selenium if you haven’t already:

```bash
pip install selenium
```

Download ChromeDriver from the official site:
https://chromedriver.chromium.org/downloads (match your chrome browser version)

Update the path in the script accordingly:
path = r'C:\path\to\your\chromedriver.exe'

---

## ▶️ Execution Instructions

Once everything’s set up, just run the script using:

```bash
python login.py
```

---

## Highlights

Here’s what makes the script work smoothly:
1.Uses both time.sleep() and WebDriverWait to handle page loads and dynamic content
2.Manages multiple tabs by switching between browser windows
3.Scrolls to elements and waits for them to be clickable before clicking
4.Logs out and closes the browser safely

---

## 📸 Output Demo (Video)
👉 [(https://drive.google.com/file/d/1FSRtZfWt9g3O3--3l3hoJKI8bRUPZ9LW/view?usp=sharing)]

This video demonstrates the end-to-end automated flow — from login to search and logout on intervue.io using Selenium with Python.






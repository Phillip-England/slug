# automation-engine

ABOUT
===========

This automation engine is built around selenium and pyautogui. It is intended to automate tasks in my workplace to increase productivity. 

The login for my workplace has heavy authentication and I have not found a way to crack it using http requests, so I have resorted to manually crawling through the pages to download the reports with the needed data.

My ultimate intention is to scrape tons of data from different pdfs using this engine, collect that data, and use it to build "The morning report".

This report will contain tons of data our business needs to know on a daily basis.

I plan to build a website which houses the data and display it on a tv screen using signpresenter.com

USAGE
===========

Dotenv - If you intend to use this bot, you will need to stash all your important usernames and passwords in a dotenv file.

Engine - The engine houses all of the classes needed for implementation. In main.py, the engine is fired up by using engine.run()

Routes - Routes house all the actual automation scripts. They are the "paths" your bot can go down. The engine itself is passed into these functions so you can access all the resources tied to the engine.

Config - All of your configuration settings go here. Things like useful coordinates or colors. My most common usage has been to stash any element ids which will need to be accessed on the routes.

FUTURE INTENTIONS
==========

My vision is to wrap the most useful parts of pyautogui and selenium in their own seperate classes and tie these classes to the engine itself. Some pdf scraping is implemented in the project, but it is a bit messy and I would like to find a more 'elegant' way to scrape useful data from pdfs other than word searching and skipping a given number of words to find data points.
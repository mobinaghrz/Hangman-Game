import requests
word = input("Choose a word or Press DR for system to choose a random word from dictionary: ")
if word == 'DR' or word == 'dr' or word == 'Dr' or word == 'dR':
    response = requests.get("https://www.merriam-webster.com/vocabulary/weekly-vocabulary-words-for-kids")
    print(response.status_code)

#In this file we are going to either choose a word or command python to go and choose a random word from a simple dictionary on the internet by connecting it to the html of the website and choose a random word then start the game
from urllib.request import urlopen
from bs4 import BeautifulSoup




try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# to search
query = f'does {word} have any meaning?'
counter  = 0
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
    counter+=1
    if "no meaning" in j:
        print('no meaning')


if counter <10:
    print('your word doest have any meaning')

# url = 'https://www.google.com/does '
# html_page = urlopen(url)
# soup = BeautifulSoup(html_page, 'html.parser')
# title = soup.title.string

# print(title)
import requests 
from bs4 import BeautifulSoup
# beautiful soup allows us to use HTML
# requests allows us to initially download that HTML

res = requests.get('https://news.ycombinator.com/news')
# get request to grab this page 
print(res)
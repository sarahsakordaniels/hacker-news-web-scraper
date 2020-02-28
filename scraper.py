import requests 
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hackernewslist):
    return sorted(hackernewslist, key=lambda k:k['votes'])

def create_custom_hacker_news(links, subtext):
    hackernews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href=item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hackernews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackernews)

pprint.pprint(create_custom_hacker_news(links, subtext))
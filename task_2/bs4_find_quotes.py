# /home/evemode/.cache/pypoetry/virtualenvs/task-2-v56Crasd-py3.13 --env
import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://quotes.toscrape.com/'

def main():
    html_doc = requests.get(BASE_URL)
    soup = BeautifulSoup(html_doc.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    data = []
    for i in range(0, len(quotes)):
        a_tags = []
        quote = quotes[i].text
        author = authors[i].text
        #print('--' + authors[i].text)
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            
            a_tags.append(tagforquote.text)
        data.append(
            {
            'tags': a_tags,
            'author': author,
            'quote': quote
        },
            )
    with open('quotes_find_method.json', 'w') as q:
        json.dump(data, q, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
"""У тебя сейчас всё построено через find_all, и это работает. Но если хочешь переделать на select, то логика остаётся та же, просто селекторы будут CSS-стилями.

Подсказки, как переписать на select

Вместо трёх отдельных списков (quotes, authors, tags) можно брать родительский контейнер — например, div.quote.
Тогда в каждом block сразу есть и текст цитаты, и автор, и теги. Это избавит тебя от путаницы с индексами.

Из каждого блока:

Цитата: block.select_one("span.text").get_text(strip=True)

Автор: block.select_one("small.author").get_text(strip=True)

Теги: [t.get_text(strip=True) for t in block.select("div.tags a.tag")]

В data.append(...) уже кладёшь словарь с тремя ключами.

👉 Т.е. в голове у тебя структура такая:

Найти все контейнеры: soup.select("div.quote")

Для каждого контейнера достать span.text, small.author, div.tags a.tag

Собрать словарь, добавить в список
"""


import json
from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://quotes.toscrape.com/'
data = []
html_doc = requests.get(BASE_URL)
soup = BeautifulSoup(html_doc.text, 'lxml')

base = soup.select('div.quote')
for el in base:
    quote = el.select_one('span.text').get_text(strip=True)
    author = el.select_one('small.author').get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in el.select('div.tags a.tag')]
    data.append({'tags': tags, 'author': author, 'quote': quote})
    # data.append({'tags': tags})
    # data.append({'author': author})
    # data.append({'quote': quote})
    


with open('quotes_select_method.json', 'w')as q:
    json.dump(data, q, indent=4, ensure_ascii=False)
    

import requests
import sys

from bs4 import BeautifulSoup as bs

site = 'https://m.amway.ua'

proxies = {}
if len(sys.argv) > 1:
    proxies = {'http':  sys.argv[1], 'https': sys.argv[1]}

session = requests.Session()


def parse_index(url):
    ret = []
    print(f'Parsing {url}')
    request = session.get(url, proxies=proxies)
    print(f'Status code {request.status_code}')
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        tags = soup.find_all('a', attrs={'class': 'menu_l1'})
        if not tags:
            print("not found")
        else:
            for tag in tags:
                ret.append(tag["href"])
    print('\n')
    return ret


def parse_category(url):
    ret = []
    print(f'Parsing {url}')
    request = session.get(url, proxies=proxies)
    print(f'Status code {request.status_code}')
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        tag_ul = soup.find('ul', attrs={'class': 'menu_ul'})
        if tag_ul is None:
            print('not found')
        else:
            tags = tag_ul.find_all('a')
            if not tags:
                print("not found")
            else:
                for tag in tags:
                    # print(tag["href"])
                    # print(tag.find('span', attrs={'class': 'count'}).text)
                    # print(tag.find('span', attrs={'class': 'inner'}).text)
                    ret.append(tag["href"])

    print('\n')
    return ret
    # print(soup.prettify())


def parse_subcategory(url):
    ret = []
    return ret


categories = parse_index(f'{site}/ru/')
for category in categories:
    subcategories = parse_category(f'{site}{category}')
    for subcategory in subcategories:
        products = parse_subcategory(f'{site}{subcategory}')
        print(products)
        break
    break

# parser of https://avmim.com/

import requests as re
from bs4 import BeautifulSoup

def firs():

    url = "https://avmim.com/category/other/other_books/page/"

    urls = []
    for i in range(1, 29):
        page = re.get(url + str(i))
        soup = BeautifulSoup(page.text, 'lxml')
        findd = soup.find_all(class_="entry-title")
        for j in findd:
            urls.append(j.find('a').get('href'))


    with open('urls.txt', 'w') as f:
        for i in urls:
            f.write(i + '\n')
            print(i)

def two():

    file = 'urls.txt'
    urls_books = []
    with open(file, 'r') as f:
        lst = f.read().split('\n')
        print('Количество ссылок:', len(lst))
        n = 1
        for i in lst:
            try:
                page = re.get(i).text
                soup = BeautifulSoup(page, 'lxml')
                findd = soup.find('div', class_="entry-content").find('a').get('href')
            except:
                print('error')

            urls_books.append(findd)
            print(f'{n} of {len(lst)}: {findd}')
            n += 1

    print(len(urls_books), 'ссылок на книги сформировано')
    with open('urls_books.txt', 'w') as f:
        for i in urls_books:
            f.write(i + '\n')

def tree():
    path = 'download/'
    file = 'urls_books.txt'
    with open(file, 'r') as f:
        lst = f.read().split('\n')
        print('Количество ссылок:', len(lst))
        n = 1
        for i in lst:
            try:
                content = re.get(i).content
                file_name = i[i.rfind('/')+1:]
                with open(f'{path}{file_name}', 'wb') as f:
                    f.write(content)
                    print(f'{n} of {len(lst)}: {file_name}')
            except:
                print('error')
            n += 1

tree()

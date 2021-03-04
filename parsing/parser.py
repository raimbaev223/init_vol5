# импортируем библиотеки
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

start = datetime.now() # записываем время начала работы

url = 'http://kenesh.kg/ru/deputy/list/35'


# получаем основную страницу
def get_html(url):
    response = requests.get(url)
    return response.text


def get_links():
    html = get_html(url) # вызываем функцию для получения главной страницы
    soup = BeautifulSoup(html, 'html.parser') # готовим суп
    tds = soup.find('table').find_all('td') # получаем элементы таблицы
    links = []

    for td in tds: # проходимся циклом по каждому элементу и сохраняем в список
        try:
            a = td.find('a').get('href')
            if "deputy" in a:
                links.append('http://kenesh.kg' + a)
        except Exception as ex:
            print(ex)
    links = set(links) # оставляем только уникальные ссылки
    return links


def get_page_data(): # вызываем функцию для получения данных с каждой страницы
    links = get_links()
    for link in links: # зарускаем цикл
        response = requests.get(link).text
        try:
            soup = BeautifulSoup(response, 'html.parser') # готовим суп для обработки страницы

            try:
                name = soup.find('h3', class_='deputy-name').text.strip() # пробуем получить имя
                # print(name)
            except Exception as ex:
                print(ex)

            try:
                phone = soup.find('p', class_='mb-10').text.strip() # пробуем получить номер телефона
                # print(phone)
            except Exception as ex:
                print(ex)
                phone = 'Нет данных'

            try:
                bio = soup.find('div', id='biography').text.strip().replace(' ', '') # пробуем получить биографию
                # print(len(bio))
            except Exception as ex:
                print(ex)

            with open('data.csv', 'a') as file: # записываем данные в файл
                data = (name, phone, bio)
                writer = csv.writer(file)
                writer.writerow(data)
                print(f'{name} записан в файл')

        except Exception as ex:
            print(ex)
    print('finish')

#
# get_page_data()
#
# # высчитываем время работы
# stop = datetime.now()
# print(stop - start)
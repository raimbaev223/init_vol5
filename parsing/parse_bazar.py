import requests
from bs4 import BeautifulSoup


#
url = input("Какую страницу спарсить? ")
page = '?page='
pagination = input()
i = 0
while i < 25:

    i += 1
    response = requests.get(f"{url}{page}{i}").text
    # print(response)

    soup = BeautifulSoup(response, 'html.parser')
    data = soup.find_all('div', class_="listing")
    print(f"{url}{page}{i} Спарсил удачно")
    for block in data:

        title = block.find('div', class_="left-side").text.strip()
        price = block.find('p', class_="price").text
        # print(title)
        # print(price)

        with open("../bazar2.txt", 'a') as file:
            file.write(title + price + "\n")

import requests
from bs4 import BeautifulSoup

def func_valuta():
    link = "https://nbu.uz/ru/fizicheskim-litsam-kursy-valyut"
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find_all('div', class_='currency_03_currency-item')

    result = ""

    for i in range(min(7, len(block))):  # защита от IndexError
        test_block = block[i]

        block_value = test_block.find('div', class_='currency_03_currency-item-curerncies-wrapper')
        name_value = block_value.find_all('div')[1].text.strip()

        value_deneg = test_block.find_all('div', class_='currency_03_currency-item-price')
        value_deneg_pokupka = value_deneg[0].text
        value_deneg_prodaja = value_deneg[1].text

        result+=f'{name_value}\nЦена покупки - {value_deneg_pokupka} | Цена продажи - {value_deneg_prodaja}\n'

    return result.strip()

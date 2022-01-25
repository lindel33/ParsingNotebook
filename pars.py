# Парсинг сайта
import datetime
from ast import literal_eval
import datetime
import time
from pprint import pprint

from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException
from selenium.webdriver.common.by import By

from data_new import add_new_model
from get_browser import get_browser

browser = get_browser('https://www.notebook-center.ru/catalog_acer.html')


def get_characters_notebook(link) -> list[str, str]:
    """
    Получаем харатеристики ноутбука и его модель
    :param link:
    :return:
    """

    browser.get(link)
    time.sleep(4)
    characters_xpath = '/html/body/div[2]/div[3]/div[2]/div/table/tbody/' \
                       'tr/td/div[2]/div/div[1]/div[2]/div[1]/div[2]'

    name_xpath = '/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr/' \
                 'td/div[2]/div/div[1]/div[2]/div[1]/div[1]/h3'
    characters_block = browser.find_element(By.XPATH, characters_xpath).text
    name_model = browser.find_element(By.XPATH, name_xpath).text
    characters_block = characters_block.split('\n')

    return [name_model, characters_block]


def get_tables():
    """
    Получение всех таблиц с ссылками на модели
    1 Таблица исключается - Это описание
    :return:
    """
    tb_xpath = '/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr/td'
    head_table = browser.find_element(By.XPATH, tb_xpath)
    block_table = head_table.find_elements(By.CLASS_NAME, 'block')
    list_links = []
    for table in block_table:
        try:
            next_table = table.find_element(By.CLASS_NAME, 'head')
            table_name = next_table.find_element(By.TAG_NAME, 'h3').text
            td = table.find_elements(By.TAG_NAME, 'li')
            links = []
            for link in td:
                post_links = link.find_element(By.TAG_NAME, 'a')
                next_link = post_links.get_attribute('href')
                links.append(next_link)
            list_links.append([str(table_name), links])
        except:
            pass
    return list_links


def create_dict():
    """
    Создает словарь для записи в БД
    """
    links = get_tables()
    for link_list in links:
        model = link_list[0]
        list_links = link_list[1]
        for link in list_links:
            data = get_characters_notebook(link)
            data = {
                'name': model,
                'number_series': data[0],
                'text': data[1],
            }
            pprint(data)

create_dict()

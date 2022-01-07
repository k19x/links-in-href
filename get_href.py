from time import sleep
import requests, os
from bs4 import BeautifulSoup

file = input("Projeto: ")
site = input("Insert: ")
data = requests.get(site)
parse = BeautifulSoup(data.text, 'html.parser')

# Abrir atual diretório
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(f'{file}'+'.txt', 'w') as file_site:
    for link in parse.find_all('a'):
        if link.get('href'):
            if site is not link.get('href'):
                print(link.get('href'))
            elif 'https://' in link.get('href') and 'http://' in link.get('href'):
                print(site+link.get('href'))
                file_site.write(str(link.get('href')))
                file_site.write(str('\n'))
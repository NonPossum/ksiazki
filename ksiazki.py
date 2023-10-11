# -*- coding: utf-8 -*-




#sprawdza czy ksiazki co chce kupic są 


# pobiera strone z adresem szukanie ksiazki
# parsuje czy jest ksiazka
# i wyswietla jesli jakies są komunikaty w konsoli

from colorama import Fore, Back, Style, init

import json
from os import link
import unicodedata

import sys
from cgitb import text
import requests
from bs4 import BeautifulSoup
import re

init(autoreset=True)

# Lista adresów URL do analizy
sklepy = [
    'https://tezeusz.pl/',
    'https://www.ceneo.pl/',
    #'https://www.amazon.pl/', i cos tam innego 
]


def usun_polskie_znaki_i_male_litery(lista_text):
    przeksztalcone_lista = []
    
    for text in lista_text:
        # Usuń polskie znaki diakrytyczne
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
        # Zamień na małe litery
        text = text.lower()
        przeksztalcone_lista.append(text)
    
    return przeksztalcone_lista


def sprawdz_link(link, slowa):

    slowa = slowa.split()

    # Rozdziel link na słowa za pomocą znaków "-" i "="
    slowa_w_linku = re.split(r'[-]', link)
    
    slowa = usun_polskie_znaki_i_male_litery(slowa)
    # Usuń znaki specjalne, spacje i puste słowa
    #slowa_w_linku = [s.strip() for s in slowa_w_linku if s.strip()]
    
    # Sprawdź, czy określone słowa występują w linku
    for slowo in slowa:
        if slowo in slowa_w_linku:
            None
        else:
            return False
        
    
    return True



# Pętla po wszystkich adresach URL
def tezeusz(nazwa):
    # Wysłanie żądania GET
    links = []
    response = requests.get(sklepy[0] + f'szukaj?szukaj={nazwa}&nowa=1&uzywana=1&tylko_dostepne=1')

    # Sprawdzenie, czy strona została pomyślnie pobrana
    if response.status_code == 200:
        # Parsowanie zawartości strony przy użyciu BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Przykład: Wyświetlenie tytułu strony
        elements = soup.find_all(class_='books-grid-container c-2 books-grid-container')
        
        for element in elements:
            a = element.find_all(class_='book-title book-title-all')

            for i in a:
                href = i.a.get('href') #link
                if sprawdz_link(href[1:],nazwa) == True:
                    links.append(sklepy[0] + href)
        
        return links

        # Tutaj możesz dodać kod do dalszej analizy strony
    else:
        print(f'Nie można pobrać strony ({sklepy[0]}). Kod odpowiedzi HTTP: {response.status_code}')


def ceneo(nazwa):
    # Wysłanie żądania GET
    links = []

    #print((sklepy[1] + f';szukaj-{nazwa}').replace(" ", "+"))
    #return links
    response = requests.get(sklepy[1] + f'Partials/GetMarketplacesOffers?searchPhrase={nazwa}&isSearchTextByUserDefined=True&categoryId=&_=1697027062986')

    

    # Sprawdzenie, czy strona została pomyślnie pobrana
    if response.status_code == 200:
        # Parsowanie zawartości strony przy użyciu BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')


        # Przykład: Wyświetlenie tytułu strony
        elements = soup.find_all(class_="cat-prod-row js_category-list-item")
        

        for element in elements:
            a = element.find_all(class_='cat-prod-row__body')

            for i in a:
                href = i.a.get('href') #link
                links.append(sklepy[1] + href)

                
        return links
        

        # Tutaj możesz dodać kod do dalszej analizy strony
    else:
        print(f'Nie można pobrać strony ({sklepy[1]}). Kod odpowiedzi HTTP: {response.status_code}')




def display_list_with_decorations(my_list, decoration='-', width=40):
    color = Fore.GREEN
    print(decoration * width)
    for item in my_list:
        print(f"{decoration}{color}{item}")
        print()
    print(decoration * width)
    print(Style.RESET_ALL)


if __name__ == "__main__":
    # Otwórz plik JSON z danymi
    with open('ksiazki.json', 'r', encoding='utf-8') as plik_json:
        dane = json.load(plik_json)

    # Wyświetl dane z funkcji ceneo
    for i in dane:
        print("WYNIKI Z FUNKCJI CENEO DLA DANYCH:", dane[i])
        display_list_with_decorations(ceneo(dane[i]))
    
    print("----------------------------")

    # Wyświetl dane z funkcji tezeusz
    for i in dane:
        print("WYNIKI Z FUNKCJI TEZEUSZ DLA DANYCH:", dane[i])
        display_list_with_decorations(tezeusz(dane[i]))

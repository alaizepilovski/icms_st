from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import re

load_dotenv()

class Portaria:

    def __init__(self) -> None:
        self.url_portaria = os.environ.get('URL_PORTARIA')
        self.status, self.html_portaria = self.check_status_portaria()
        self.status_code = ''

    def check_status_portaria(self):
        try:
            response = requests.get(self.url_portaria)
            self.status_code = response.status_code
            if response.status_code == 200:
                return True, response.content
            return False, ''
        except Exception as e:
            return False, ''

    def tratar_dados_portaria(self):

        def _sub_digits(text: str):
            """ remove os não digitos de uma string """
            try:
                return re.sub('\D',"", text)
            except TypeError:
                return text

        def _text(element, without_digits=False, replace=False, elem_replace="", replace_to=""):
            try:
                clean_element = str(element.text).strip()
                if  without_digits:
                    clean_element = _sub_digits(clean_element)
                if clean_element:
                    if replace:
                        clean_element = clean_element.replace(elem_replace, replace_to)
                    return clean_element
                return None
            except Exception as e:
                return None
            
        def _check_multiples_ncms(cols):
            """ analisa se existe mais de um ncm por meio de separado"""
            
            ncms_text = _text(cols[2])
            try:
                ncms = ncms_text.split("\n") if "\n" in ncms_text else ncms_text.split(" ")
                # Log
                # if '23.0' in _text(cols[0]):
                #     print(ncms)
                qtd_ncms = len(ncms)
                if qtd_ncms > 1:
                    items = []
                    for ncm in ncms:
                        if _sub_digits(ncm) != "":
                            items.append({'item': _text(cols[0]), 'cest': _text(cols[1], True), 'ncm': _sub_digits(ncm), 'descricao': _text(cols[3]), 'mva': _text(cols[4], replace=True, elem_replace="%", replace_to="")})
                    return items
                if _sub_digits(ncms_text) != "":
                    return [{'item': _text(cols[0]), 'cest': _text(cols[1], True), 'ncm': _sub_digits(ncms_text), 'descricao': _text(cols[3]), 'mva': _text(cols[4], replace=True, elem_replace="%", replace_to="")}]
                return False
            
            except Exception as e:
                if _sub_digits(ncms_text) != "":
                    return [{'item': _text(cols[0]), 'cest': _text(cols[1], True), 'ncm': _sub_digits(ncms_text), 'descricao': _text(cols[3]), 'mva': _text(cols[4], replace=True, elem_replace="%", replace_to="")}]
                return False
            
        def _valid(cols):
            """ verifica se o item da tabela é valido com base nas regras"""
            try:
                item = cols[0].find(size=2)

                if item or _text(cols[1]) is None or "revogado" in _text(cols[3]).lower() or "item" in _text(cols[0]).lower():
                    return False
                return True
            except Exception as e:
                return False
            
        items = []
        if self.status:
        
            soup = BeautifulSoup(self.html_portaria, 'html.parser')

            tables = soup.find_all("table", attrs={"border": 1})
            for table in tables:
                rows = table.find_all('tr')

                for row in rows:
                    cols = row.find_all('td')

                    if _valid(cols):
                        rows_list = _check_multiples_ncms(cols)
                        if rows_list:
                            items.extend(rows_list)
        else:
            print(f"erro {self.status_code}")

        return items


if __name__ == '__main__':
    teste = Portaria()
    dados = teste.tratar_dados_portaria()

    df = pd.DataFrame(dados)

    print(df.to_excel("portaria195.xlsx"))
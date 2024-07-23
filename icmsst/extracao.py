from bs4 import BeautifulSoup
import requests
import os
import re

class Portaria:

    def __init__(self) -> None:
        self.url_portaria = os.environ.get('URL_PORTARIA')
        self.status, self.html_portaria = self.check_status_portaria()

    def check_status_portaria(self):
        try:
            response = requests.get(self.url_portaria)
            if response.status_code == 200:
                return True, response.content
            return False
        except Exception as e:
            return False
        
    def tratar_dados_portaria(self):

        def text(element, without_digits=False):
            try:
                clean_element = str(element.text).strip()
                if  without_digits:
                    clean_element = re.sub('\D','', clean_element)
                if clean_element:
                    return clean_element
                return None
            except Exception as e:
                return None
            
        def valid(cols):
            try:
                item = cols[0].find(size=2)

                if item or text(cols[1]) is None or "revogado" in text(cols[3]).lower() or "item" in text(cols[0]).lower():
                    print(f"<<=== Redação pula [{item}] ===>>")
                    return False
                return True
            except Exception as e:
                return False


        soup = BeautifulSoup(self.html_portaria, 'html.parser')

        tables = soup.find_all("table", attrs={"border": 1})
        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cols = row.find_all('td')

                if valid(cols):
                    ...
                
                    print(text(cols[0]), text(cols[1], True), text(cols[2], True), text(cols[3]), text(cols[4]), sep=" | ")


if __name__ == '__main__':
    teste = Portaria()
    print(teste.tratar_dados_portaria())

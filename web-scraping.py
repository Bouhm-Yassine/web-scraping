from bs4 import BeautifulSoup
import requests

url = "https://www.societe.com/cgi-bin/search?champs=cartan"


def scrap():
    response = requests.get(url, headers={'User-agent': 'Super Bot Power Level Over 9000'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        result_search = soup.find('div', id='search')

        if result_search is None:
            return 'Aucun résultat trouvé'

        soup.find('div', id="result_doc").decompose()
        companies = soup.find_all('div', class_='ResultBloc__link')

        for company in companies[:3]:
            # print(company.prettify())
            name = company.find('p', class_='deno')
            infos = company.find_all('p', class_="txt")
            print('NAME:', name.text.strip())
            print('COMPANY STATUS: ACTIVE')
            print('REGISTRED AS:', infos[1].text.strip().split(':')[1])
            adress_line = infos[2].text.strip()
            print('LEGAL ADDRESS LINE:', adress_line)
            print('LEGAL ADDRESS POSTAL CODE:', adress_line.split(' ')[0])
            print('LEGAL ADDRESS CITY:', adress_line.split(' ')[1])

            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


if __name__ == '__main__':
    print(scrap())

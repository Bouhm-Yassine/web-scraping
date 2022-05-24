from bs4 import BeautifulSoup
import requests

url_1 = "https://www.societe.com/cgi-bin/search?champs=cartan"
url_2 = "https://find-and-update.company-information.service.gov.uk/search/companies?q=cartan"


def scrap_1():
    response = requests.get(url_1, headers={'User-agent': 'Super Bot Power Level Over 9000'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        result_search = soup.find('div', id='search')

        if result_search is None:
            return 'Aucun résultat trouvé'

        soup.find('div', id="result_doc").decompose()
        companies = soup.find_all('div', class_='ResultBloc__link')

        for company in companies[:3]:
            # print(company.prettify())
            name = company.find('p', class_='deno').text.strip()
            infos = company.find_all('p', class_="txt")
            registred_as = infos[1].text.split(':')[-1].strip()
            adress_line = infos[2].text.strip()
            adr_arr = adress_line.split(' ')
            postal_code = adr_arr[0]
            city = " ".join(adr_arr[1:])

            json = {"name": name, "status": "active", "registred_as": registred_as, "adress_line": adress_line,
                    "postal_code": postal_code, "city": city}
            print(json)
            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


def scrap_2():
    response = requests.get(url_2, headers={'User-agent': 'Super Bot Power Level Over 9000'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        result_search = soup.find('article', id="services-information-results")

        if result_search is None:
            return 'Aucun résultat trouvé'

        result = soup.find('ul', id='results')
        companies = result.findChildren("li", recursive=False)
        for company in companies[:3]:
            name = company.a.text.strip()

            national_date = company.find('p', class_='meta').text
            registred_as = national_date.split('-')[0].strip()

            full_date = national_date.split('-')[-1]
            date = full_date.replace('Incorporated on', '').replace('Dissolved on', '').strip()

            adress_line = company.find_all('p')[-1].text.strip()
            postal_code = adress_line.split(',')[-1].strip()
            json = {"name": name, "status": "active", "registred_as": registred_as, 'created_at': date,
                    "adress_line": adress_line, "postal_code": postal_code}
            print(json)
            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


if __name__ == '__main__':
    # scrap_1()
    scrap_2()

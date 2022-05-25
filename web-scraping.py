from bs4 import BeautifulSoup
import requests

url_1 = "https://www.societe.com/cgi-bin/search?champs=cartan"
# url_2 = "https://find-and-update.company-information.service.gov.uk/search/companies?q=cartan"
url_2 = "https://find-and-update.company-information.service.gov.uk/search?q=CARPANINI+INTERNATIONALE+ART+DEALERSHIP+LIMITED"
url_3 = "https://italy.globaldatabase.com/filter/company?name=cisco"

url_4 = "https://data.gov.sg/api/action/datastore_search?resource_id=5ab68aac-91f6-4f39-9b21-698610bdf3f7&q=ARKEMA"


# France
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


# UK
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
            # print(company.prettify())
            national_date = company.find('p', class_="meta crumbtrail").text
            # print(national_date)
            registred_as = national_date.split('-')[0].strip()

            full_date = national_date.split('-')[-1]
            date = ''
            status = ''
            if 'Dissolved on' in full_date:
                status = 'Inactive'
            elif 'Incorporated on' in full_date:
                status = 'Active'
                date = full_date.replace('Incorporated on', '').strip()

            adress_line = company.find('p', class_ = None).text.strip()

            postal_code = adress_line.split(',')[-1].strip()
            json = {"name": name, "status": status, "registred_as": registred_as, 'created_at': date,
                    "adress_line": adress_line, "postal_code": postal_code}

            print(json)
            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


# Italy
def scrap_3():
    response = requests.get(url_3, headers={'User-agent': 'Super Bot Power Level Over 9000'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        result_search = soup.find('ul', id="results-list-companies")

        if result_search is None:
            return 'Aucun résultat trouvé'

        companies = result_search.findChildren("li", recursive=False)

        for company in companies[:3]:
            title = company.find('div', class_='title')
            name = title.h1.a.text.strip()
            status = title.span.text.strip()

            tables = company.find('div', class_="company-info-block").findChildren('table')
            registred_as = tables[0].find_all('tr')[1].text.strip()

            city = tables[3].find_all('tr')[3].text.strip()

            json = {"name": name, "status": status, "registred_as": registred_as, "city": city}
            print(json)
            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


# Singapore
def scrap_4():
    response = requests.get(url_4)
    if response.status_code == 200:
        companies = response.json()['result']['records']

        if len(companies) == 0:
            return 'Aucun résultat trouvé'

        for company in companies[:3]:
            status = "Active" if company['uen_status'] == "R" else ("Inactive" if company['uen_status'] == "D" else "Not available")
            json = {"name": company['entity_name'], "status": status, "registred_as": company['uen'],
                    "adress_line": company['reg_street_name'], "postal_code": company['reg_postal_code'],
                    "city": 'Singapore', "created_at": company['uen_issue_date']}
            print(json)
            print('===============================')

    else:
        return 'THROW EXCPETION HERE'


if __name__ == '__main__':
    # scrap_1()
    # scrap_2()
    # scrap_3()
    scrap_4()

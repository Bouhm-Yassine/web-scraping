from flatten_json import flatten
import requests
import pandas as pd
import openpyxl as pxl
import json
from pandas.io.json import json_normalize
from pymongo import MongoClient
import uuid
import csv

# db_url = "mongodb://localhost:27017/cartan?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
client = MongoClient(host="localhost", port=27017)

credentials = {
    "username": "VPERES@scor.com",
    "password": "Wy05!UQKPkE'*HVN%Gh("
}
auth_url = "https://connect.creditsafe.com/v1/authenticate"
detail_url = "https://connect.creditsafe.com/v1/companies/{}"

url_1 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=46.23Z,46.73B,46.43Z,46.48Z,46.49Z,46.66Z,46.76Z,46.38B,46.39B&chiffre_affaires_min=2000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"
url_2 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=10.11Z,10.12Z,10.13A,10.13B,10.20Z,10.31Z,10.32Z,10.39A,10.39B,10.41A,10.41B,10.42Z,10.51A,10.51B,10.51C,10.51D,10.52Z,10.61A,10.61B,10.62Z,10.71A,10.71B,10.71C,10.71D,10.72Z,10.73Z,10.81Z,10.82Z,10.83Z,10.84Z,10.85Z,10.86Z,10.89Z,10.91Z,10.92Z,11.01Z,11.02A,11.02B,11.03Z,11.04Z,11.05Z,11.06Z,11.07A,11.07B,12.00Z,13.10Z,13.20Z,13.30Z,13.91Z,13.92Z,13.93Z,13.94Z,13.95Z,13.96Z,13.99Z,14.11Z,14.12Z,14.13Z,14.14Z,14.19Z,14.20Z,14.31Z,14.39Z,15.11Z,15.12Z,15.20Z,16.10A,16.10B,16.21Z,16.22Z,16.23Z,16.24Z,16.29Z,17.11Z,17.12Z,17.21A,17.21B,17.21C,17.22Z,17.23Z,17.24Z,17.29Z,18.11Z,18.12Z,18.13Z,18.14Z,18.20Z,19.10Z,19.20Z,20.11Z,20.12Z,20.13A,20.13B,20.14Z,20.15Z,20.16Z,20.17Z,20.20Z,20.30Z,20.41Z,20.42Z,20.51Z,20.52Z,20.53Z,20.59Z,20.60Z,21.10Z,21.20Z,22.11Z,22.19Z,22.21Z,22.22Z,22.23Z,22.29A,22.29B,23.11Z,23.12Z,23.13Z,23.14Z,23.19Z,23.20Z,23.31Z,23.32Z,23.41Z,23.42Z,23.43Z,23.44Z,23.49Z,23.51Z,23.52Z,23.61Z,23.62Z,23.63Z,23.64Z,23.65Z,23.69Z,23.70Z,23.91Z,23.99Z,24.10Z,24.20Z,24.31Z,24.32Z,24.33Z,24.34Z,24.41Z,24.42Z,24.43Z,24.44Z,24.45Z,24.46Z,24.51Z,24.52Z,24.53Z,24.54Z,25.11Z,25.12Z,25.21Z,25.29Z,25.30Z,25.40Z,25.50A,25.50B,25.61Z,25.62A,25.62B,25.71Z,25.72Z,25.73A,25.73B,25.91Z,25.92Z,25.93Z,25.94Z,25.99A,25.99B,26.11Z,26.12Z,26.20Z,26.30Z,26.40Z,26.51A,26.51B,26.52Z,26.60Z,26.70Z,26.80Z,27.11Z,27.12Z,27.20Z,27.31Z,27.32Z,27.33Z,27.40Z,27.51Z,27.52Z,27.90Z,28.11Z,28.12Z,28.13Z,28.14Z,28.15Z,28.21Z,28.22Z,28.23Z,28.24Z,28.25Z,28.29A,28.29B,28.30Z,28.41Z,28.49Z,28.91Z,28.92Z,28.93Z,28.94Z,28.95Z,28.96Z,28.99A,28.99B,29.10Z,29.20Z,29.31Z,29.32Z,30.11Z,30.12Z,30.20Z,30.30Z,30.40Z,30.91Z,30.92Z,30.99Z,31.01Z,31.02Z,31.03Z,31.09A,31.09B,32.11Z,32.12Z,32.13Z,32.20Z,32.30Z,32.40Z,32.50A,32.50B,32.91Z,32.99Z,33.11Z,33.12Z,33.13Z,33.14Z,33.15Z,33.16Z,33.17Z,33.19Z,33.20A,33.20B,33.20C,33.20D&chiffre_affaires_min=2000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"
url_3 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=49.10Z,49.20Z,49.31Z,49.32Z,49.39A,49.39B,49.39C,49.41A,49.41B,49.41C,49.42Z,49.50Z,50.10Z,50.20Z,50.30Z,50.40Z,51.10Z,51.21Z,51.22Z,52.10A,52.10B,52.21Z,52.22Z,52.23Z,52.24A,52.24B,52.29A,52.29B,53.10Z,53.20Z&chiffre_affaires_min=2000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"
url_4 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=01.11Z,01.12Z,01.13Z,01.14Z,01.15Z,01.16Z,01.19Z,01.21Z,01.22Z,01.23Z,01.24Z,01.25Z,01.26Z,01.27Z,01.28Z,01.29Z,01.30Z,01.41Z,01.42Z,01.43Z,01.44Z,01.45Z,01.46Z,01.47Z,01.49Z,01.50Z,01.61Z,01.62Z,01.63Z,01.64Z,01.70Z,02.10Z,02.20Z,02.30Z,02.40Z,03.11Z,03.12Z,03.21Z,03.22Z&chiffre_affaires_min=2000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"
url_5 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=13.99Z,13.92Z,46.41Z,13.30Z,47.51Z,47.82Z&chiffre_affaires_min=1000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"
url_6 = "https://api.pappers.fr/v2/recherche?entreprise_cessee=false&code_naf=41.10A,41.10B,41.10C,41.10D,41.20A,41.20B,42.11Z,42.12Z,42.13A,42.13B,42.21Z,42.22Z,42.91Z,42.99Z,43.11Z,43.12A,43.12B,43.13Z,43.21A,43.21B,43.22A,43.22B,43.29A,43.29B,43.31Z,43.32A,43.32B,43.32C,43.33Z,43.34Z,43.39Z,43.91A,43.91B,43.99A,43.99B,43.99C,43.99D,43.99E&chiffre_affaires_min=2000000&chiffre_affaires_max=10000000&api_token=97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575&page=1&par_page=20"

urls = [url_1, url_2, url_3, url_4, url_5, url_6]


def pappers():
    res = []
    for url in urls:
        response = requests.get(url, headers={'User-agent': 'Super Bot Power Level Over 9000'})
        print(len(response.json()['resultats']))
        res.extend(response.json()['resultats'])
    df = pd.json_normalize(res)
    df['credit_safe_id'] = 'FR-X-' + df['siege.siret']
    # df_final = df[['siren', 'siege.siret', 'credit_safe_id']]
    df.to_excel('pappers.xlsx', index=False)
    # print(df_final)


def json_pappers():
    names = ['Extract Agro 726', 'Extract CommerGros 1688', 'Extract Construction 1000', 'Extract Industrie 2000',
             'Extract Textile 416', 'Extract Transport 2000']
    df_globale = pd.DataFrame([])
    df_globale.to_excel('resultat.xlsx', index=False)

    for name in names:
        filename = './json/import/{}.json'.format(name)
        print(filename)
        file = open(filename, encoding="utf8")
        data = json.load(file)
        df_papers = pd.json_normalize(data)
        df_papers['credit_safe_id'] = 'FR-X-' + df_papers['siege.siret']
        # df_papers.to_excel('res_final.xlsx', index=""false"")
        add_new_sheet('../resultat.xlsx', df_papers, name)
        del df_papers


def add_new_sheet(path, df, sheet_name):
    excel_book = pxl.load_workbook(path)
    with pd.ExcelWriter(path, engine='openpyxl') as writer:
        writer.book = excel_book
        writer.sheets = {
            worksheet.title: worksheet
            for worksheet in excel_book.worksheets
        }

        df.to_excel(writer, sheet_name, index=False)
        writer.save()


def flatt_credit_safe():
    file = open("../credit_safe.json", encoding="utf8")
    data = json.load(file)
    df = pd.json_normalize(data, record_path="activityClassifications")
    df.to_excel('credit_safe_flatten.xlsx', index=False)
    # print(data)
    # report.companyIdentification.activityClassifications


def get_credit_safe_data():
    found = []
    not_found = []
    df = pd.read_excel('input_credit_safe_3.xlsx', index=False)
    df.apply(lambda row: credit_safe_processing_detail(row, found, not_found), axis=1)

    store_json_file("../found.json", found)
    store_json_file("../not_found.json", not_found)


def credit_safe_processing_detail(row, found, not_found):
    print(row['credit_safe_id'])
    token = authenticate()
    get_company_detail_from_provider(token, row['credit_safe_id'], found, not_found)
    print('---------------------')


def authenticate():
    response = requests.post(auth_url, credentials)
    if response.status_code == 200:
        return response.json()['token']
    else:
        print('Auth Failed')


def get_company_detail_from_provider(token, credit_safe_id, found, not_found):
    req_url = detail_url.format(credit_safe_id)
    response = requests.get(req_url, headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(token)})
    if response.status_code == 200:
        company_report = response.json()
        found.append(company_report)
        store_to_mongo(company_report)
        print('FOUND')
        # save json

    else:
        not_found.append({'credit_safe_id': credit_safe_id})
        print('THROW EXCPETION HERE', credit_safe_id)
        return 'THROW EXCPETION HERE'


def store_json_file(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


# def get_excel():
#     df = pd.DataFrame(flatten_data)
#     df.to_excel('flatten_output.xlsx')

def generate_id():
    return uuid.uuid4().hex.upper()


def store_to_mongo(data):
    data['_id'] = generate_id()
    db = client.cartan
    one_shot_coll = db.one_shot_flatten
    one_shot_coll.insert_one(data)


def new_flatten():
    print('--------------- START')
    # unflat_json = {"name": "yassine", "hobbies": ["AA", "BB", "CC"], "adresse": {"code": 12345, "villes": ['MPMP', 'LOLOO', 'BBB']}}
    file = open("C://Users//Yassine//Desktop//Extraction Credit Safe//one_shot.json", encoding="utf8")
    unflat_jsons = json.load(file)
    print('--------------- FILE LOADED')
    res = []
    for index, u in enumerate(unflat_jsons):
        flat_json = flatten(u)
        store_to_mongo(flat_json)
        res.append(flat_json)
        print(index + 1)
        print('-----------------')
    df = pd.DataFrame(res)
    df.to_excel('new_flatten.csv', index=False)


# ----------------- Agro 726
# 726
# FR-X-06180023100054
# FR-X-31514467500032
# Columns:  62919
# ----------------- CommerceGros 1375
# 1373
# FR-X-02658029000067
# FR-X-99813501600033
# Columns:  49497
# ----------------- Transport 1736
# 1733
# FR-X-02403898600014
# FR-X-97572011100015
# Columns:  66674
# ----------------- Industrie 1435
# 1432
# FR-X-00648020600017
# FR-X-97725032300010
# Columns:  51544
# ----------------- Textile 416
# 415
# FR-X-43405602400012
# FR-X-45283336100010
# Columns:  18209
# =COLONNE(INDIRECT("XFD" & "1"))
# ----------------- Construction 845
# 843
# FR-X-01645021500021
# FR-X-99773952900037
# Columns:  48202
#

def find_all():
    # rows: 1048576
    # columns: 16384
    extractions = [
        {"start": 0, "end": 726, "name": "Agro 726"},
        {"start": 727, "end": 2100, "name": "CommerceGros 1375"},
        {"start": 2101, "end": 3834, "name": "Transport 1736"},
        {"start": 3835, "end": 5267, "name": "Industrie 1435"},
        {"start": 5268, "end": 5683, "name": "Textile 416"},
        {"start": 5684, "end": 6527, "name": "Construction 845"},
    ]
    db = client.cartan
    one_shot_coll = db.one_shot_flatten
    all = list(one_shot_coll.find())

    for ex in extractions:
        print('-----------------', ex['name'])
        temp = all[ex['start']:ex['end']]
        print(len(temp))
        print(temp[0]['companyId'])
        print(temp[-1]['companyId'])
        # df = pd.DataFrame(temp)
        # columns = list(df.columns)
        # print("Columns: ", len(columns))

        # list_df = df.values.tolist()
        # with open("./extractions/" + ex['name'] + ".json", "w", newline='', encoding='utf-8') as f:
        #     writer = csv.DictWriter(f, fieldnames=list(columns), delimiter=";")
        #     writer.writeheader()
        #     writer.writerows(temp)

        with open("./extractions/" + ex['name'] + ".json", "w") as final:
           json.dump(temp, final)

        # df.to_excel("/extractions/"+ex['name']+".xlsx", index=False)
        # df.to_csv("./extractions/"+ex['name']+".csv", index=False, encoding="utf-8", sep=";", compression=True)
        # df.to_hdf("./extractions/"+ex['name']+".csv", index=False, encoding="utf-8", key='stage', mode='w')

        del temp
        # del df
        # del columns
        # f.close()
        final.close()


if __name__ == '__main__':
    # store_to_mongo()
    # get_credit_safe_data()
    # new_flatten()
    find_all()
    # df = pd.read_csv('C://Users//Yassine//Desktop//Extraction Credit Safe//one_shot_flatten.csv')
    # print(list(df.columns))
    # print('--------------')
    # print(df.head())
    # df.to_excel('oooooooooooo.xlsx')

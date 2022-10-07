import requests

url_details = "https://services.data-access-gateway.com/1/rest/svcOnlineOrder"

xml_details_body = """"
<svcOnlineOrderRequest lang="FR" version="2.2">
	<admin>
		<client>
			<contractId>49031</contractId>
			<userPrefix>GEOCOM</userPrefix>
			<userId>NN427539</userId>
			<password>W6MN5M20CQKQ</password>
		</client>
		<context>
			<appId version="1">WSPRO</appId>
			<date>2011-12-13T17:38:15+01:00</date>
		</context>
	</admin>
	<request>
		<id type="register" idName="SIREN">300254471</id>
		<product range="101021" version="1" />
		<deliveryOptions>
			<outputMethod>raw</outputMethod>
		</deliveryOptions>
	</request>
</svcOnlineOrderRequest>"""

def detail():
    response = requests.post(url_details, data=xml_details_body, headers={'Content-Type': 'Application/xml'})
    print(response.text)


if __name__ == '__main__':
    detail()

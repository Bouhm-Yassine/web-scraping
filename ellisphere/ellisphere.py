import json
import xml.etree.ElementTree as ET
from xml.etree import ElementTree

from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

import requests
import xmltodict

url = "https://services.data-access-gateway.com/1/rest/svcSearchByName"
url_details = "https://services.data-access-gateway.com/1/rest/svcOnlineOrder"

json_body_search = {
    "@lang": "FR",
    "@version": "2.2",
    "admin": {
        "client": {
            "contractId": "49031",
            "userPrefix": "GEOCOM",
            "userId": "NN427539",
            "password": "W6MN5M20CQKQ"
        },
        "context": {
            "appId": {
                "@version": "2",
                "#text": "WSPRO "
            },
            "date": "2022-07-21T13:38:15+01:00"
        }
    },
    "request": {
        "searchCriteria": {
            "name": "",
            "address": {
                "country": {
                    "@code": ""
                }
            }
        }
    }
}
xml_details_body = """<svcOnlineOrderRequest lang="FR" version="2.2">
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
		<id type="src">441768876</id>
		<product range="101021" version="1" />
		<deliveryOptions>
			<outputMethod>raw</outputMethod>
		</deliveryOptions>
	</request>
</svcOnlineOrderRequest>"""
xml_body_search = """
<svcSearchByNameRequest lang="FR" version="2.2">
  <admin>
    <client>
      <contractId>49031</contractId>
      <userPrefix>GEOCOM</userPrefix>
      <userId>NN427539</userId>
      <password>W6MN5M20CQKQ</password>
    </client>
    <context>
      <appId version="2">WSPRO</appId>
      <date>2022-07-21T13:38:15+01:00</date>
    </context>
  </admin>
  <request>
    <searchCriteria>
        <name>CARTAN TRADE</name>
        <address>
            <country code="FRA"/>
        </address>
    </searchCriteria>
  </request>
</svcSearchByNameRequest>"""
xml_response = """<?xml version="1.0" encoding="UTF-8"?>
<svcOnlineOrderResponse lang="FR" version="2.2">
    <result code="OK"/>
    <response>
        <intlReport version="2.2">
            <header>
                <provider internalId="000" country="FRA">Ellisphere</provider>
                <report>
                    <reportId range="101021" version="1">Rapport approfondi WS</reportId>
                    <date type="delivery">2022-08-03T13:00:18</date>
                    <date type="lastupdate">2022-08-01</date>
                    <lang>fr</lang>
                    <defaultCurrency code="EUR">Euro</defaultCurrency>
                    <defaultCurrencyUnit>0</defaultCurrencyUnit>
                </report>
                <order>
                    <date>2022-08-03T13:00:18</date>
                </order>
            </header>
            <companyIdentity>
                <id type="src" idName="Identifiant interne">300254471</id>
                <id type="register" idName="SIREN">300254471</id>
                <id type="register-estb" idName="SIRET">30025447100018</id>
                <id type="iref" idName="ElliNumber">A07W62V36</id>
                <id type="vat" idName="TVA">FR85300254471</id>
                <businessName>ENTREPRISE EDOUIN ERIC</businessName>
                <legalForm origin="src" ref="CATJUR" code="5710">Société par actions simplifiée</legalForm>
                <legalForm origin="csf" ref="FJ" code="FJ22">Société Anonyme</legalForm>
                <activity>
                    <description type="primary" ref="NACE2008" code="4120">Construction de bâtiments résidentiels et non résidentiels</description>
                </activity>
                <activity>
                    <description type="primary" ref="APE2008" code="4120A">Construction de maisons individuelles</description>
                </activity>
                <commentsOnActivities emphasis="bold" lang="fr">Activité exercée</commentsOnActivities>
                <commentsOnActivities lang="fr">Société spécialisée dans la construction de maison individuelle. Elle élabore le projet de construction depuis la conception jusqu'à la remise des clef et réalise des travaux sur mesure, personnalisés, selon les spécifications des clients qui sont des particuliers principalement.</commentsOnActivities>
                <status>
                    <currentStatus type="active" ref="STATUS" code="ACT">Active</currentStatus>
                </status>
                <address type="registered">
                    <country code="FRA">France</country>
                    <countrySubdivision type="department" code="27">Eure</countrySubdivision>
                    <countrySubdivision type="region" code="28">Normandie</countrySubdivision>
                    <cityName>LE BOSC-DU-THEIL</cityName>
                    <cityCode type="postalcode">27370</cityCode>
                    <cityCode type="citycode">27302</cityCode>
                    <locationDetails>
                        <locationName>Hm de la Grosse Londe</locationName>
                    </locationDetails>
                    <addressLine>Hm de la Grosse Londe</addressLine>
                </address>
                <communication type="phone">0232296600</communication>
                <communication type="fax">0232296609</communication>
                <communication type="url">www.edouin.fr</communication>
                <communication type="mail">entreprise-edouin@wanadoo.fr</communication>
            </companyIdentity>
            <companyDetails>
                <foundation>
                    <date type="creation">1974-01-01</date>
                    <registration>
                        <authority>
                            <id type="national" idName="Numéro de greffe">2702</id>
                            <name>Evreux</name>
                        </authority>
                        <date type="registration">1974-01-01</date>
                        <reference>2000B00582</reference>
                    </registration>
                    <ISCA>Convention collective nationale concernant les ouvriers employés par les entreprises du bâtiment non visées par le décret 1er mars 1962 -c'est-à-dire occupant plus de 10 salariés-</ISCA>
                </foundation>
                <workForce>
                    <numberOfEmployees format="number">14</numberOfEmployees>
                </workForce>
                <capitalInformation>
                    <capital format="currency" currencyCode="EUR" currencyUnit="0">800000.00</capital>
                    <capitalDetail ref="CPTLCAT" code="NOMINAL">
                        <name>Capital social</name>
                        <value format="currency" currencyCode="EUR" currencyUnit="0">800000.00</value>
                    </capitalDetail>
                </capitalInformation>
                <stockExchange listed="no"/>
                <premises>Propriétaire des Locaux</premises>
                <companyType ref="CATENT" code="PME">Petite ou Moyenne Entreprise</companyType>
                <corporatePurpose>-Construction et vente de maisons individuelles (en CMI et Vefa) Tous travaux de construction et d'une manière générale, toutes les activités d'entreprise générale du bâtiment éventuellement l'activité de marchand de biens l'achat et la location d'immeubles. Création acquisition location prise à bail installation exploitation de tous établissements fonds de commerce.</corporatePurpose>
            </companyDetails>
            <establishment type="main">
                <name type="businessname">ENTREPRISE EDOUIN ERIC</name>
                <id type="register-estb" idName="SIRET">30025447100018</id>
                <id type="iref-estb" idName="ElliEstab">A07W62V3600001</id>
                <registration>
                    <authority>
                        <id type="national" idName="Numéro de greffe">2702</id>
                        <name>Evreux</name>
                    </authority>
                    <date type="registration">1974-01-01</date>
                </registration>
                <address type="registered">
                    <country code="FRA">France</country>
                    <countrySubdivision type="department" code="27">Eure</countrySubdivision>
                    <countrySubdivision type="region" code="28">Normandie</countrySubdivision>
                    <cityName>LE BOSC-DU-THEIL</cityName>
                    <cityCode type="postalcode">27370</cityCode>
                    <cityCode type="citycode">27302</cityCode>
                    <locationDetails>
                        <locationName>Hm de la Grosse Londe</locationName>
                    </locationDetails>
                    <addressLine>Hm de la Grosse Londe</addressLine>
                </address>
                <activity type="primary" ref="APE2008" code="4120A">Construction de maisons individuelles</activity>
                <communication type="phone">0232296600</communication>
                <communication type="fax">0232296609</communication>
                <workForce>
                    <numberOfEmployees format="number">14</numberOfEmployees>
                </workForce>
            </establishment>
            <establishmentsBreakDown>
                <category ref="DEPT" code="27">
                    <name>EURE</name>
                    <value format="number">1</value>
                </category>
            </establishmentsBreakDown>
            <characteristics>
                <market scope="national">
                    <comment lang="fr">L'entreprise n'exporte pas</comment>
                </market>
            </characteristics>
            <companyAppointments type="statutory">
                <boardName>Directeurs</boardName>
                <manager>
                    <party>
                        <company>
                            <id type="src" idName="Identifiant interne">398773242</id>
                            <id type="register" idName="SIREN">398773242</id>
                            <businessName>DUDAS DEVELOPPEMENT ET PARTICIPATIONS</businessName>
                            <address>
                                <country code="FRA">France</country>
                            </address>
                        </company>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="100">Président</role>
                        <role origin="csf" ref="MGMT" code="MG43">Président</role>
                        <date type="nomination">2021-02-16</date>
                        <date type="since">2022-02-01</date>
                    </position>
                </manager>
                <manager>
                    <party>
                        <company>
                            <id type="src" idName="Identifiant interne">848733705</id>
                            <id type="register" idName="SIREN">848733705</id>
                            <businessName>GROUPE NORMANDIE MAISONS INDIVIDUELLES</businessName>
                            <address>
                                <country code="FRA">France</country>
                            </address>
                        </company>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="400">Directeur général</role>
                        <role origin="csf" ref="MGMT" code="MG27">Directeur General</role>
                        <date type="nomination">2020-09-12</date>
                        <date type="since">2022-02-01</date>
                    </position>
                </manager>
            </companyAppointments>
            <companyAppointments type="auditors">
                <boardName>Auditeurs</boardName>
                <manager>
                    <party>
                        <company>
                            <id type="src" idName="Identifiant interne">521599688</id>
                            <id type="register" idName="SIREN">521599688</id>
                            <businessName>ASSISTECO AUDIT</businessName>
                            <address>
                                <country code="FRA">France</country>
                            </address>
                        </company>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="9300">Commissaire aux comptes titulaire</role>
                        <role origin="csf" ref="MGMT" code="MG10">Commissaire aux Comptes</role>
                        <date type="nomination">2021-05-15</date>
                    </position>
                </manager>
                <manager>
                    <party>
                        <person>
                            <salutation>M</salutation>
                            <firstName>Francois</firstName>
                            <lastName>DOLIGE</lastName>
                            <fullName>Francois DOLIGE</fullName>
                        </person>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="9400">Commissaire aux comptes suppléant</role>
                        <role origin="csf" ref="MGMT" code="MG10">Commissaire aux Comptes</role>
                        <date type="nomination">1997-04-30</date>
                    </position>
                </manager>
            </companyAppointments>
            <companyAppointments type="managers">
                <boardName>Dirigeants opérationnels</boardName>
                <manager>
                    <party>
                        <person>
                            <salutation>M</salutation>
                            <firstName>Cedric</firstName>
                            <lastName>LEPORGNE</lastName>
                            <fullName>Cedric LEPORGNE</fullName>
                        </person>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="607170">Dir/Resp des Travaux</role>
                        <role origin="csf" ref="MGMT" code="MG13">Directeur</role>
                    </position>
                </manager>
                <manager>
                    <party>
                        <person>
                            <salutation>MME</salutation>
                            <firstName>Maria</firstName>
                            <lastName>PEREZ</lastName>
                            <fullName>Maria PEREZ</fullName>
                        </person>
                    </party>
                    <position>
                        <role origin="src" ref="FCTORG" code="612080">Dir/Resp Comptabilité Gestion</role>
                        <role origin="csf" ref="MGMT" code="MG26">Directeur Financier</role>
                    </position>
                </manager>
            </companyAppointments>
            <shareHolder ultimate="false" level="1">
                <typeOfLink>Actionnaire</typeOfLink>
                <party>
                    <person>
                        <salutation>M</salutation>
                        <firstName>ERIC</firstName>
                        <lastName>EDOUIN</lastName>
                        <fullName>ERIC EDOUIN</fullName>
                        <birthPlace>MAROMME</birthPlace>
                        <birthCountry>FRANCE (FRA)</birthCountry>
                    </person>
                </party>
                <shareDetails>
                    <date type="publication">2019-07-01</date>
                    <quote ref="QUOTE" code="SUB">Filiale</quote>
                    <comment>Pourcentage fusionné: 50.01%</comment>
                </shareDetails>
                <informationSource ref="INFSRC" code="COMPANY">
                    <name>Interrogation auprès de l'entreprise</name>
                </informationSource>
            </shareHolder>
            <shareHolding level="1">
                <typeOfLink>Participation</typeOfLink>
                <party>
                    <company>
                        <id type="src" idName="Identifiant interne">345214654</id>
                        <id type="register" idName="SIREN">345214654</id>
                        <id type="register-estb" idName="SIRET">A08S61B89</id>
                        <businessName>S.C.I PIERIC</businessName>
                        <address>
                            <country code="FRA">FRANCE</country>
                            <countrySubdivision type="department" code="27">Eure</countrySubdivision>
                            <countrySubdivision type="region" code="28">Normandie</countrySubdivision>
                            <cityName>LE BOSC DU THEIL</cityName>
                            <cityCode type="postalcode">27370</cityCode>
                        </address>
                    </company>
                </party>
                <shareDetails>
                    <date type="publication">2020-09-16</date>
                    <quote format="percent">99.00</quote>
                </shareDetails>
                <score origin="csf" name="Ellisphere" meaning="companydefault" type="standard" duration="P12M">
                    <value type="riskclass" scale="A - D" format="text">A</value>
                    <comment type="riskclass" lang="fr">Risque faible</comment>
                </score>
                <informationSource ref="INFSRC" code="COMPANY">
                    <name>Interrogation auprès de l'entreprise</name>
                </informationSource>
            </shareHolding>
            <shareHolding level="1">
                <typeOfLink>Participation</typeOfLink>
                <party>
                    <company>
                        <id type="src" idName="Identifiant interne">424846624</id>
                        <id type="register" idName="SIREN">424846624</id>
                        <id type="register-estb" idName="SIRET">A10W44I95</id>
                        <businessName>PIERRE 3000</businessName>
                        <address>
                            <country code="FRA">FRANCE</country>
                            <countrySubdivision type="department" code="76">Seine-Maritime</countrySubdivision>
                            <countrySubdivision type="region" code="28">Normandie</countrySubdivision>
                            <cityName>LE HAVRE</cityName>
                            <cityCode type="postalcode">76600</cityCode>
                        </address>
                    </company>
                </party>
                <shareDetails>
                    <date type="publication">2013-09-13</date>
                    <quote format="percent">78.20</quote>
                </shareDetails>
                <score origin="csf" name="Ellisphere" meaning="companydefault" type="standard" duration="P12M">
                    <value type="riskclass" scale="A - D" format="text">A</value>
                    <comment type="riskclass" lang="fr">Risque faible</comment>
                </score>
                <keyFigures origin="csf" consolidated="false">
                    <element code="CA00">
                        <elementName>Chiffre d'affaires</elementName>
                        <value format="currency" currencyCode="EUR" currencyUnit="0">40833.00</value>
                    </element>
                    <element code="RN00">
                        <elementName>Résultat net</elementName>
                        <value format="currency" currencyCode="EUR" currencyUnit="0">8712.00</value>
                    </element>
                </keyFigures>
                <informationSource ref="INFSRC" code="COMPANY">
                    <name>Interrogation auprès de l'entreprise</name>
                </informationSource>
            </shareHolding>
            <bankReference>
                <party>
                    <company>
                        <id type="bankid" idName="BIC">30027</id>
                        <id type="bankid-estb" idName="Code agence">16079</id>
                        <businessName>BSDCIN EVREUX EURE ENTRE</businessName>
                        <address>
                            <country code="FRA">France</country>
                            <addressLine>49 R GEORGES BERNARD</addressLine>
                            <addressLine>27000 EVREUX</addressLine>
                        </address>
                    </company>
                </party>
            </bankReference>
            <event type="legalchange">
                <description ref="LEGEVE" code="153">Modification sur les représentants</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2022-01-16</date>
                    <date type="publication">2022-01-16</date>
                    <reference>22011B0495</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B011  0495  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Activité : -Construction et vente de maisons individuelles (en CMI et Vefa) Tous travaux de construction et d'une manière générale, toutes les activités d'entreprise générale du bâtiment éventuellement l'activité de marchand de biens l'achat et la location d'immeubles. Création acquisition location prise à bail installation exploitation de tous établissements fonds de commerce.  Administration : Président : DUDAS DEVELOPPEMENT ET PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : ASSISTECO AUDIT ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration.</comment>
            </event>
            <event type="legalchange" initby="subject">
                <description ref="LEGEVE" code="194">Reconstitution de l'Actif Net</description>
                <severity>GREEN</severity>
                <registration>
                    <authority>
                        <name>RNCS</name>
                    </authority>
                    <date type="effective">2022-01-13</date>
                    <date type="publication">2022-01-13</date>
                </registration>
            </event>
            <event type="other">
                <description ref="LEGEVE" code="265">Avis de dépôt des comptes annuels</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2022-01-13</date>
                    <date type="publication">2022-01-13</date>
                    <reference>2200900565</reference>
                </registration>
                <comment lang="fr">GREFFE DU TRIBUNAL DE COMMERCE D'EVREUX. Comptes annuels et rapports. C009 00565 RCS Evreux 300254471. ENTREPRISE ERIC EDOUIN. Forme : Société par actions simplifiée. Adresse : Hameau la Grosse Londe, Saint-Nicolas-du-Bosc, 27370 le bosc du theil. Comptes annuels et rapports. Date de cloture : 30 juin 2021.</comment>
            </event>
            <event type="legalchange">
                <description ref="LEGEVE" code="153">Modification sur les représentants</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2021-05-16</date>
                    <date type="publication">2021-05-16</date>
                    <reference>21095B0957</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B095  0957  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Activité : -Construction et vente de maisons individuelles (en CMI et Vefa) Tous travaux de construction et d'une manière générale, toutes les activités d'entreprise générale du bâtiment éventuellement l'activité de marchand de biens l'achat et la location d'immeubles. Création acquisition location prise à bail installation exploitation de tous établissements fonds de commerce.  Administration : Président : DUDAS DEVELOPPEMENT ET PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : COGEDIAC ET ASSOCIES ; Commissaire aux comptes titulaire : ASSISTECO AUDIT ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration.</comment>
            </event>
            <event type="legalchange">
                <description ref="LEGEVE" code="147">Modification du capital social</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2021-02-16</date>
                    <date type="publication">2021-02-16</date>
                    <reference>21032B0670</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B032  0670  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Capital :  800000 euros.  Activité : Construction et vente de maisons individuelles (en CMI et Vefa) - Tous travaux de construction et d'une maniere générale, toutes les activités d'entreprise générale du bâtiment eventuellement l'activité de marchand de biens l'achat et la location d'immeubles - Création acquisition location prise à bail installation exploitation de tous etablissements fonds de commerce.  Administration : Président : DUDAS DEVELOPPEMENT ET PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : COGEDIAC ET ASSOCIES ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration, l'activité, le capital.</comment>
            </event>
            <event type="legalchange">
                <description ref="LEGEVE" code="153">Modification sur les représentants</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2021-02-16</date>
                    <date type="publication">2021-02-16</date>
                    <reference>21032B0670</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B032  0670  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Capital :  800000 euros.  Activité : Construction et vente de maisons individuelles (en CMI et Vefa) - Tous travaux de construction et d'une maniere générale, toutes les activités d'entreprise générale du bâtiment eventuellement l'activité de marchand de biens l'achat et la location d'immeubles - Création acquisition location prise à bail installation exploitation de tous etablissements fonds de commerce.  Administration : Président : DUDAS DEVELOPPEMENT ET PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : COGEDIAC ET ASSOCIES ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration, l'activité, le capital.</comment>
            </event>
            <event type="legalchange">
                <description ref="LEGEVE" code="144">Modification de l'activité</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2021-02-16</date>
                    <date type="publication">2021-02-16</date>
                    <reference>21032B0670</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B032  0670  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Capital :  800000 euros.  Activité : Construction et vente de maisons individuelles (en CMI et Vefa) - Tous travaux de construction et d'une maniere générale, toutes les activités d'entreprise générale du bâtiment eventuellement l'activité de marchand de biens l'achat et la location d'immeubles - Création acquisition location prise à bail installation exploitation de tous etablissements fonds de commerce.  Administration : Président : DUDAS DEVELOPPEMENT ET PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : COGEDIAC ET ASSOCIES ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration, l'activité, le capital.</comment>
            </event>
            <event type="legalchange">
                <description ref="LEGEVE" code="153">Modification sur les représentants</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2020-09-15</date>
                    <date type="publication">2020-09-15</date>
                    <reference>20179B0472</reference>
                </registration>
                <comment lang="fr">Tribunal de commerce de EVREUX. Mutations et modifications diverses. B179  0472  RCS Evreux 300 254 471.  ENTREPRISE ERIC EDOUIN.  Forme : Société par actions simplifiée.  Activité : Tous travaux de construction et d'une maniere générale, toutes les activités d'entreprise générale du batiment eventuellement l'activité de marchand de biens l'achat et la location d'immeubles ... Création acquisition location prise à bail installation exploitation de tous etablissements fonds de commerce. Administration : Président : DUDAS DEFFONTAINE PARTICIPATIONS ; Directeur général : GROUPE NORMANDIE MAISONS INDIVIDUELLES ; Commissaire aux comptes titulaire : COGEDIAC ET ASSOCIES ; Commissaire aux comptes suppléant : DOLIGE François.  Adresse du siège social : Hameau la Grosse Londe,   Saint-Nicolas-du-Bosc,  27370  le bosc du theil.  Commentaires : Modification survenue sur l'administration.</comment>
            </event>
            <event type="other">
                <description ref="LEGEVE" code="286">Avis de dépôt des comptes annuels confidentiel</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2020-07-19</date>
                    <date type="publication">2020-07-19</date>
                    <reference>2013801380</reference>
                </registration>
                <comment lang="fr">GREFFE DU TRIBUNAL DE COMMERCE D'EVREUX. Comptes annuels et rapports. C138 01380 RCS Evreux 300254471. ENTREPRISE ERIC EDOUIN. Forme : Société par actions simplifiée. Adresse : Hameau la Grosse Londe, Saint-Nicolas-du-Bosc, 27370 le bosc du theil. Comptes annuels et rapports. Les comptes annuels sont accompagnés d'une déclaration de confidentialité en application du premier ou deuxième alinéa de l'article L. 232-25. Date de cloture : 31 decembre 2019.</comment>
            </event>
            <event type="other">
                <description ref="LEGEVE" code="286">Avis de dépôt des comptes annuels confidentiel</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2019-04-24</date>
                    <date type="publication">2019-04-24</date>
                    <reference>1908001733</reference>
                </registration>
                <comment lang="fr">GREFFE DU TRIBUNAL DE COMMERCE D'EVREUX. Comptes annuels et rapports. C080 01733 RCS Evreux 300254471. ENTREPRISE ERIC EDOUIN. Forme : Société par actions simplifiée. Adresse : hameau la Grosse Londe, Saint-Nicolas-Du-Bosc, 27370 Le Bosc-du-Theil. Comptes annuels et rapports. Les comptes annuels sont accompagnés d'une déclaration de confidentialité en application du premier ou deuxième alinéa de l'article L. 232-25. Date de cloture : 30 juin 2018.</comment>
            </event>
            <event type="legalchange" initby="subject">
                <description ref="LEGEVE" code="44">Continuation malgré perte du Capital</description>
                <severity>ORANGE</severity>
                <registration>
                    <authority>
                        <name>RNCS</name>
                    </authority>
                    <date type="effective">2019-03-21</date>
                    <date type="publication">2019-03-21</date>
                </registration>
            </event>
            <event type="other">
                <description ref="LEGEVE" code="286">Avis de dépôt des comptes annuels confidentiel</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>BODACC</name>
                    </authority>
                    <date type="effective">2018-04-10</date>
                    <date type="publication">2018-04-10</date>
                    <reference>1806501946</reference>
                </registration>
                <comment lang="fr">GREFFE DU TRIBUNAL DE COMMERCE D'EVREUX. Comptes annuels et rapports. C065 01946 RCS Evreux 300254471. ENTREPRISE ERIC EDOUIN. Forme : Société par actions simplifiée. Adresse : hameau la Grosse Londe, Saint-Nicolas-Du-Bosc, 27370 Le Bosc-du-Theil. Comptes annuels et rapports. Les comptes annuels sont accompagnés d'une déclaration de confidentialité en application du premier ou deuxième alinéa de l'article L. 232-25. Date de cloture : 30 juin 2017.</comment>
            </event>
            <event type="legalchange" initby="subject">
                <description ref="LEGEVE" code="4">Achat d'un fonds</description>
                <severity>GREEN</severity>
                <registration>
                    <authority>
                        <name>Bodacc</name>
                    </authority>
                    <date type="effective">1994-12-30</date>
                    <date type="publication">1995-04-05</date>
                </registration>
            </event>
            <event type="legalchange" initby="subject">
                <description ref="LEGEVE" code="27">Cession de parts</description>
                <severity>UNDEFINED</severity>
                <registration>
                    <authority>
                        <name>RNCS</name>
                    </authority>
                    <date type="effective">1993-02-18</date>
                    <date type="publication">1993-02-18</date>
                </registration>
            </event>
            <event type="legalchange" initby="subject">
                <description ref="LEGEVE" code="4">Achat d'un fonds</description>
                <severity>GREEN</severity>
                <registration>
                    <authority>
                        <name>Bodacc</name>
                    </authority>
                    <date type="effective">1974-01-01</date>
                    <date type="publication">1995-05-31</date>
                </registration>
            </event>
            <paymentDefaults type="sslien">
                <description>Privilèges sécurité sociale</description>
                <totalNumber format="number">0</totalNumber>
                <totalAmount format="currency" currencyCode="EUR" currencyUnit="0">0.00</totalAmount>
                <detail>
                    <date type="event">2021-08-23</date>
                    <amount type="due" format="currency" currencyCode="EUR" currencyUnit="0">0.00</amount>
                </detail>
                <comment lang="fr">Aucune inscription</comment>
            </paymentDefaults>
            <paymentDefaults type="taxlien">
                <description>Privilèges trésor</description>
                <totalNumber format="number">0</totalNumber>
                <totalAmount format="currency" currencyCode="EUR" currencyUnit="0">0.00</totalAmount>
                <detail>
                    <date type="event">2021-08-23</date>
                    <amount type="due" format="currency" currencyCode="EUR" currencyUnit="0">0.00</amount>
                </detail>
                <comment lang="fr">Aucune inscription</comment>
            </paymentDefaults>
            <paymentsAnalysis>
                <paymentBehaviour>
                    <rank ref="PYR_INDICTR" code="3">L'entreprise présente un crédit fournisseur dans la moyenne de son secteur.</rank>
                    <date>2022-04-14</date>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">L'entreprise présente un crédit fournisseur dans la moyenne de son secteur.</rank>
                        <date>2022-08-03</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">L'entreprise présente un crédit fournisseur dans la moyenne de son secteur.</rank>
                        <date>2022-06-30</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">L'entreprise présente un crédit fournisseur dans la moyenne de son secteur.</rank>
                        <date>2022-03-31</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2021-12-31</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2021-09-30</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2021-06-30</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2021-03-31</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2020-12-31</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="3">Le PayRank de cette entreprise est correct.</rank>
                        <date>2020-09-30</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="2">Le PayRank de cette entreprise est insatisfaisant.</rank>
                        <date>2020-06-30</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="2">Le PayRank de cette entreprise est insatisfaisant.</rank>
                        <date>2020-03-31</date>
                    </history>
                    <history>
                        <rank ref="PYR_INDICTR" code="2">Le PayRank de cette entreprise est insatisfaisant.</rank>
                        <date>2019-12-31</date>
                    </history>
                    <DPO year="2021">
                        <company>39.22</company>
                        <sector>35.97</sector>
                    </DPO>
                </paymentBehaviour>
                <paymentIncidents>
                    <indicator ref="PYR_INCIDENT" code="NA">Non déterminé</indicator>
                    <summary type="due" since="36" unit="month">false</summary>
                    <summary type="settled" since="36" unit="month">false</summary>
                    <incidentsByPeriod type="due" from="0" to="1" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                    <incidentsByPeriod type="due" from="1" to="3" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                    <incidentsByPeriod type="due" from="3" to="6" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                    <incidentsByPeriod type="due" from="6" to="12" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                    <incidentsByPeriod type="due" from="12" to="24" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                    <incidentsByPeriod type="due" from="24" to="36" unit="month">
                        <amountRange from="0" to="1000">false</amountRange>
                        <amountRange from="1000" to="2000">false</amountRange>
                        <amountRange from="2000" to="5000">false</amountRange>
                        <amountRange from="5000" to="10000">false</amountRange>
                        <amountRange from="10000">false</amountRange>
                    </incidentsByPeriod>
                </paymentIncidents>
            </paymentsAnalysis>
            <commentsOnPayments lang="fr">Aucun incident de moins de 12 mois n'a été porté à notre connaissance.</commentsOnPayments>
            <assessmentData>
                <score origin="csf" name="Ellisphere" meaning="companydefault" type="standard" duration="P12M">
                    <date>2022-04-14</date>
                    <value type="score" format="text" scale="0 - 10">5</value>
                    <value type="riskclass" scale="A - E" format="text">B</value>
                    <comment type="riskclass" lang="fr">Risque moyen à faible</comment>
                    <comment type="score" lang="fr">Structure qui évolue dans un secteur jugé sensible, néanmoins des relations restent envisageables.</comment>
                </score>
                <score origin="src" name="Ellisphere" meaning="companydefault" type="standard" duration="P12M">
                    <date>2022-04-14</date>
                    <value type="score" format="text" scale="1 - 10">5</value>
                    <value type="riskclass" scale="A - E" format="text">B</value>
                    <comment type="riskclass" lang="fr">Risque moyen à faible</comment>
                    <comment type="score" lang="fr">Structure qui évolue dans un secteur jugé sensible, néanmoins des relations restent envisageables.</comment>
                </score>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2022-06-30</date>
                    <value type="score" format="text" scale="0 - 10">5</value>
                </scoreHistory>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2021-12-31</date>
                    <value type="score" format="text" scale="0 - 10">5</value>
                </scoreHistory>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2021-06-30</date>
                    <value type="score" format="text" scale="0 - 10">3</value>
                </scoreHistory>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2020-12-31</date>
                    <value type="score" format="text" scale="0 - 10">3</value>
                </scoreHistory>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2020-06-30</date>
                    <value type="score" format="text" scale="0 - 10">3</value>
                </scoreHistory>
                <scoreHistory origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <date>2019-12-31</date>
                    <value type="score" format="text" scale="0 - 10">2</value>
                </scoreHistory>
                <sectorScore origin="csf" name="Ellisphere" meaning="companydefault" type="standard">
                    <value type="score" scale="0 - 10" format="text">3</value>
                    <value type="riskclass" scale="A - E" format="text">C</value>
                    <comment type="riskclass" lang="fr">Risque moyen à élevé</comment>
                </sectorScore>
                <creditOpinion origin="csf" name="Ellisphere" type="standard">
                    <date>2021-12-06</date>
                    <upTo format="currency" currencyCode="EUR" currencyUnit="0">15000.00</upTo>
                </creditOpinion>
                <keyFigures origin="csf" consolidated="false">
                    <period type="actual" number="1">
                        <date type="end">2021-06-30</date>
                        <sector>CIS</sector>
                        <duration unit="month">18</duration>
                        <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                        <currencyCode>EUR</currencyCode>
                        <currencyUnit>0</currencyUnit>
                    </period>
                    <period type="actual" number="2">
                        <date type="end">2019-12-31</date>
                        <sector>CIS</sector>
                        <duration unit="month">18</duration>
                        <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                        <currencyCode>EUR</currencyCode>
                        <currencyUnit>0</currencyUnit>
                    </period>
                    <period type="actual" number="3">
                        <date type="end">2018-06-30</date>
                        <sector>CIS</sector>
                        <duration unit="month">12</duration>
                        <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                        <currencyCode>EUR</currencyCode>
                        <currencyUnit>0</currencyUnit>
                    </period>
                    <element code="CA00">
                        <elementName>Chiffre d'affaires</elementName>
                        <value period="1" type="actual" percent="100.00" format="currency">2318505.00</value>
                        <value period="3" type="actual" percent="100.00" format="currency">1766000.00</value>
                    </element>
                </keyFigures>
                <statistics ref="ST" code="ST01">
                    <name>Nombre etablissements actifs</name>
                    <value format="number">1</value>
                </statistics>
                <statistics ref="ST" code="ST02">
                    <name>Nombre de dirigeants (hors CAC)</name>
                    <value format="number">2</value>
                </statistics>
                <statistics ref="ST" code="ST03">
                    <name>Nombre de dirigeants opérationnels</name>
                    <value format="number">2</value>
                </statistics>
                <statistics ref="ST" code="ST04">
                    <name>Nombre d'actionnaires recensés</name>
                    <value format="number">1</value>
                </statistics>
                <statistics ref="ST" code="ST05">
                    <name>Nombre de participations recensées (entreprise)</name>
                    <value format="number">2</value>
                </statistics>
                <statistics ref="ST" code="ST07">
                    <name>Nombre de jugements</name>
                    <value format="number">0</value>
                </statistics>
                <statistics ref="ST" code="ST08">
                    <name>Nombre de résumés de presse</name>
                    <value format="number">0</value>
                </statistics>
                <statistics ref="ST" code="ST09">
                    <name>Nombre d'actionnaires indirects recensés</name>
                    <value format="number">0</value>
                </statistics>
                <statistics ref="ST" code="ST10">
                    <name>Nombre de participations indirectes recensées</name>
                    <value format="number">0</value>
                </statistics>
                <statistics ref="ST" code="ST11">
                    <name>Nombre de commissaires aux comptes</name>
                    <value format="number">2</value>
                </statistics>
                <statistics ref="ST" code="ST12">
                    <name>Nombre d'évènements BODACC</name>
                    <value format="number">26</value>
                </statistics>
                <statistics ref="ST" code="ST15">
                    <name>Classe de risque maximale des participations</name>
                    <value format="text">A</value>
                    <comment lang="fr">Risque faible</comment>
                </statistics>
                <audience>
                    <queries>
                        <date>2022-08</date>
                        <number>0</number>
                    </queries>
                    <queries>
                        <date>2022-07</date>
                        <number>1</number>
                    </queries>
                    <queries>
                        <date>2022-06</date>
                        <number>0</number>
                    </queries>
                    <queries>
                        <date>2022-05</date>
                        <number>1</number>
                    </queries>
                    <queries>
                        <date>2022-04</date>
                        <number>4</number>
                    </queries>
                    <queries>
                        <date>2022-03</date>
                        <number>0</number>
                    </queries>
                    <queries>
                        <date>2022-02</date>
                        <number>5</number>
                    </queries>
                    <queries>
                        <date>2022-01</date>
                        <number>9</number>
                    </queries>
                    <queries>
                        <date>2021-12</date>
                        <number>7</number>
                    </queries>
                    <queries>
                        <date>2021-11</date>
                        <number>0</number>
                    </queries>
                    <queries>
                        <date>2021-10</date>
                        <number>2</number>
                    </queries>
                    <queries>
                        <date>2021-09</date>
                        <number>1</number>
                    </queries>
                    <monitoring>
                        <date>2022-08</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-07</date>
                        <number>24</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-06</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-05</date>
                        <number>24</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-04</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-03</date>
                        <number>21</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-02</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2022-01</date>
                        <number>22</number>
                    </monitoring>
                    <monitoring>
                        <date>2021-12</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2021-11</date>
                        <number>23</number>
                    </monitoring>
                    <monitoring>
                        <date>2021-10</date>
                        <number>25</number>
                    </monitoring>
                    <monitoring>
                        <date>2021-09</date>
                        <number>23</number>
                    </monitoring>
                </audience>
            </assessmentData>
            <financialsDisclaimer ref="FINDISC" code="PUBLIC">
                <date type="end">2021-06-30</date>
                <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                <comment>Les comptes sont publics</comment>
            </financialsDisclaimer>
            <financialsDisclaimer ref="FINDISC" code="PCONF">
                <date type="end">2019-12-31</date>
                <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                <comment>Le compte de résultats est publié avec confidentialité (source légale)</comment>
            </financialsDisclaimer>
            <financialsDisclaimer ref="FINDISC" code="PCONF">
                <date type="end">2018-06-30</date>
                <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                <comment>Le compte de résultats est publié avec confidentialité (source légale)</comment>
            </financialsDisclaimer>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Structure et endettement</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DRA1">
                    <elementName>Indépendance financière retraitée (en %)</elementName>
                    <value period="1" type="actual" format="percent">64.39</value>
                    <value period="2" type="actual" format="percent">14.33</value>
                    <value period="3" type="actual" format="percent">15.55</value>
                </element>
                <element code="DRA2">
                    <elementName>Indépendance financière non retraitée (en %)</elementName>
                    <value period="1" type="actual" format="percent">64.39</value>
                    <value period="2" type="actual" format="percent">12.75</value>
                    <value period="3" type="actual" format="percent">4.80</value>
                </element>
                <element code="DRB1">
                    <elementName>Taux d'endettement net (gearing) retraité (en %)</elementName>
                    <value period="3" type="actual" format="percent">175.13</value>
                </element>
                <element code="DRB2">
                    <elementName>Taux d'endettement net (gearing) non retraité (en %)</elementName>
                    <value period="3" type="actual" format="percent">567.72</value>
                </element>
                <element code="DRH1">
                    <elementName>Taux d'usure des immobilisations (en %)</elementName>
                    <value period="1" type="actual" format="percent">93.03</value>
                    <value period="2" type="actual" format="percent">96.64</value>
                    <value period="3" type="actual" format="percent">73.40</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Couverture</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DRFRNG">
                    <elementName>FRNG (en jours de C.A. HT)</elementName>
                    <value period="1" type="actual" format="days">131.53</value>
                    <value period="3" type="estimated" format="days">-50.03</value>
                </element>
                <element code="DRBFR">
                    <elementName>BFR (en jours de C.A. HT)</elementName>
                    <value period="1" type="actual" format="days">6.48</value>
                    <value period="3" type="estimated" format="days">-18.44</value>
                </element>
                <element code="DRBFRE">
                    <elementName>BFRE (en jours de C.A. HT)</elementName>
                    <value period="1" type="actual" format="days">4.84</value>
                    <value period="3" type="estimated" format="days">-27.05</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Gestion du BFR</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DRF2">
                    <elementName>Crédits fournisseurs (en jours d'achat TTC)</elementName>
                    <value period="1" type="actual" format="days">42.22</value>
                </element>
                <element code="DRF3">
                    <elementName>Crédits clients (en jours d'achat TTC)</elementName>
                    <value period="1" type="actual" format="days">63.69</value>
                    <value period="3" type="estimated" format="days">63.71</value>
                </element>
                <element code="DRF4">
                    <elementName>Provisions clients (en % du poste clients)</elementName>
                    <value period="1" type="actual" format="percent">10.24</value>
                    <value period="2" type="actual" format="percent">12.00</value>
                    <value period="3" type="actual" format="percent">17.57</value>
                </element>
                <element code="DRR1">
                    <elementName>Délais de rotation des stocks de matières premières (en jours d'achat HT)</elementName>
                    <value period="1" type="actual" format="days">10.91</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Liquidité</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DRD1">
                    <elementName>Liquidité générale (en unité)</elementName>
                    <value period="1" type="actual" format="number">2.89</value>
                    <value period="2" type="actual" format="number">1.19</value>
                    <value period="3" type="actual" format="number">0.61</value>
                </element>
                <element code="DRD2">
                    <elementName>Liquidité réduite (en unité)</elementName>
                    <value period="1" type="actual" format="number">2.85</value>
                    <value period="2" type="actual" format="number">0.96</value>
                    <value period="3" type="actual" format="number">0.51</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Marges et performance économique</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DRG1">
                    <elementName>Marge brute d'exploitation (en % du C.A. HT)</elementName>
                    <value period="1" type="actual" format="percent">-2.44</value>
                    <value period="3" type="estimated" format="percent">1.25</value>
                </element>
                <element code="DRG2">
                    <elementName>Performance (en % du C.A. HT)</elementName>
                    <value period="1" type="actual" format="percent">-0.04</value>
                    <value period="3" type="estimated" format="percent">-2.66</value>
                </element>
                <element code="DRG3">
                    <elementName>Marge nette (en % du C.A. HT)</elementName>
                    <value period="1" type="actual" format="percent">0.40</value>
                    <value period="3" type="estimated" format="percent">-1.74</value>
                </element>
                <element code="DRG4">
                    <elementName>Rentabilité économique (en % du C.A. HT)</elementName>
                    <value period="1" type="actual" format="percent">-30.65</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="functionnal-accounts">
                <financialsName>Bilan fonctionnel</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DSTR1">
                    <elementName>Emplois stables</elementName>
                    <value period="1" type="actual" percent="15.67" format="currency">164498.00</value>
                </element>
                <element code="DSTR2">
                    <elementName>Actifs circulants d'exploitation</elementName>
                    <value period="1" type="actual" percent="32.52" format="currency">341399.00</value>
                </element>
                <element code="DSTR3">
                    <elementName>Actifs circulants hors exploitation</elementName>
                    <value period="1" type="actual" percent="0.67" format="currency">7058.00</value>
                </element>
                <element code="DSTR4">
                    <elementName>Actif de trésorerie</elementName>
                    <value period="1" type="actual" percent="51.14" format="currency">536872.00</value>
                </element>
                <element code="DSTR5">
                    <elementName>Total actif brut retraité</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">1049827.00</value>
                </element>
                <element code="DSTR6">
                    <elementName>Ressources stables</elementName>
                    <value period="1" type="actual" percent="69.46" format="currency">729205.00</value>
                </element>
                <element code="DSTR7">
                    <elementName>Dettes d'exploitation</elementName>
                    <value period="1" type="actual" percent="30.54" format="currency">320625.00</value>
                </element>
                <element code="DSTR8">
                    <elementName>Dettes hors exploitation</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSTR9">
                    <elementName>Passif de trésorerie</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSTR10">
                    <elementName>Total passif brut retraité</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">1049830.00</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="work-capital-variations">
                <financialsName>Évolution du FRNG et du BFR</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                    <comment lang="fr">L'analyse du besoin en fonds de roulement d'exploitation et de ses 2 composantes ne peut être effectuée.</comment>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                    <comment lang="fr">L'analyse du besoin en fonds de roulement d'exploitation et de ses 2 composantes ne peut être effectuée.</comment>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                    <comment lang="fr">L'analyse du besoin en fonds de roulement d'exploitation et de ses 2 composantes ne peut être effectuée.</comment>
                </period>
                <element code="DGM1">
                    <elementName>Chiffre d'affaires</elementName>
                    <value period="1" type="actual" format="currency">2318505.00</value>
                    <value period="3" type="estimated" format="currency">1766000.00</value>
                </element>
                <element code="DSTR1">
                    <elementName>Emplois stables</elementName>
                    <value period="1" type="actual" format="currency">164498.00</value>
                    <value period="2" type="actual" format="currency">407776.00</value>
                    <value period="3" type="actual" format="currency">1240442.00</value>
                </element>
                <element code="DSTR6">
                    <elementName>Ressources stables</elementName>
                    <value period="1" type="actual" format="currency">729205.00</value>
                    <value period="2" type="actual" format="currency">408982.00</value>
                    <value period="3" type="actual" format="currency">995019.00</value>
                </element>
                <element code="DSTR11">
                    <elementName>FRNG</elementName>
                    <value period="1" type="actual" format="currency">564707.00</value>
                    <value period="2" type="actual" format="currency">1206.00</value>
                    <value period="3" type="actual" format="currency">-245423.00</value>
                </element>
                <element code="DSTR12">
                    <elementName>BFR</elementName>
                    <value period="1" type="actual" format="currency">27832.00</value>
                    <value period="2" type="actual" format="currency">-34602.00</value>
                    <value period="3" type="actual" format="currency">-90470.00</value>
                </element>
                <element code="DSTR13">
                    <elementName>BFRE</elementName>
                    <value period="1" type="actual" percent="0.90" format="currency">20774.00</value>
                    <value period="2" type="actual" format="currency">-55312.00</value>
                    <value period="3" type="actual" percent="-7.51" format="currency">-132672.00</value>
                </element>
                <element code="DSTR131">
                    <elementName>BFRE opérationnel</elementName>
                    <value period="1" type="actual" percent="7.25" format="currency">168071.00</value>
                    <value period="2" type="actual" format="currency">143938.00</value>
                    <value period="3" type="actual" percent="7.55" format="currency">133281.00</value>
                </element>
                <element code="DSTR1311">
                    <elementName>BFRE opérationnel - Stocks</elementName>
                    <value period="1" type="actual" percent="0.59" format="currency">13737.00</value>
                    <value period="2" type="actual" format="currency">78971.00</value>
                    <value period="3" type="actual" percent="4.37" format="currency">77127.00</value>
                </element>
                <element code="DSTR1312">
                    <elementName>BFRE opérationnel - Clients</elementName>
                    <value period="1" type="actual" percent="14.08" format="currency">326339.00</value>
                    <value period="2" type="actual" format="currency">278272.00</value>
                    <value period="3" type="actual" percent="21.24" format="currency">375041.00</value>
                </element>
                <element code="DSTR1313">
                    <elementName>BFRE opérationnel - Fournisseurs</elementName>
                    <value period="1" type="actual" percent="7.42" format="currency">172005.00</value>
                    <value period="2" type="actual" format="currency">213305.00</value>
                    <value period="3" type="actual" percent="18.06" format="currency">318887.00</value>
                </element>
                <element code="DRF2">
                    <elementName>BFRE opérationnel - Crédits fournisseurs (en jours d'achat TTC)</elementName>
                    <value period="1" type="actual" format="days">42.22</value>
                </element>
                <element code="DSTR132">
                    <elementName>BFRE non opérationnel</elementName>
                    <value period="1" type="actual" percent="-6.35" format="currency">-147297.00</value>
                    <value period="2" type="actual" format="currency">-199250.00</value>
                    <value period="3" type="actual" percent="-15.06" format="currency">-265953.00</value>
                </element>
                <element code="DSTR14">
                    <elementName>BFRHE</elementName>
                    <value period="1" type="actual" format="currency">7058.00</value>
                    <value period="2" type="actual" format="currency">20710.00</value>
                    <value period="3" type="actual" format="currency">42202.00</value>
                </element>
                <element code="DSTR15">
                    <elementName>Trésorerie nette</elementName>
                    <value period="1" type="actual" format="currency">536872.00</value>
                    <value period="2" type="actual" format="currency">35811.00</value>
                    <value period="3" type="actual" format="currency">-154952.00</value>
                </element>
                <element code="DSTR16">
                    <elementName>Intensité capitalistique</elementName>
                    <value period="1" type="actual" format="percent">7.96</value>
                    <value period="3" type="estimated" format="percent">53.21</value>
                </element>
                <element code="DSTR21">
                    <elementName>Équilibre financier</elementName>
                    <value period="1" type="actual" format="number">4.43</value>
                    <value period="2" type="actual" format="number">1</value>
                    <value period="3" type="actual" format="number">0.8</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="stable-resources-distrib">
                <financialsName>Répartition des ressources stables</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DSTR17">
                    <elementName>Capitaux propres</elementName>
                    <value period="1" type="actual" format="percent">79.52</value>
                    <value period="2" type="actual" format="percent">17.23</value>
                    <value period="3" type="actual" format="percent">4.53</value>
                </element>
                <element code="DSTR18">
                    <elementName>Endettement bancaire brut</elementName>
                    <value period="1" type="actual" format="percent">0.00</value>
                    <value period="2" type="actual" format="percent">2.13</value>
                    <value period="3" type="actual" format="percent">10.16</value>
                </element>
                <element code="DSTR19">
                    <elementName>Engagements de crédit-bail</elementName>
                    <value period="1" type="actual" format="percent">0.00</value>
                </element>
                <element code="DSTR20">
                    <elementName>Amortissements et provisions</elementName>
                    <value period="1" type="actual" format="percent">20.48</value>
                    <value period="2" type="actual" format="percent">80.64</value>
                    <value period="3" type="actual" format="percent">85.31</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" consolidated="false" ref="FINCAT" code="cashflow">
                <financialsName>Flux de trésorerie</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DTRES1">
                    <elementName>Excédent brut d'exploitation</elementName>
                    <value period="1" type="actual" format="currency">-56578.00</value>
                    <value period="3" type="estimated" format="currency">22000.00</value>
                </element>
                <element code="DTRES2">
                    <elementName>Variation du BFRE</elementName>
                    <value period="1" type="actual" format="currency">76086.00</value>
                    <value period="3" type="actual" format="currency">63251.00</value>
                </element>
                <element code="DTRES3">
                    <elementName>Flux d'exploitation</elementName>
                    <value period="1" type="actual" format="currency">-132664.00</value>
                    <value period="3" type="estimated" format="currency">-41251.00</value>
                </element>
                <element code="DTRES4">
                    <elementName>Capacité d'autofinancement</elementName>
                    <value period="1" type="actual" format="currency">-12049.00</value>
                    <value period="3" type="estimated" format="currency">44000.00</value>
                </element>
                <element code="DTRES5">
                    <elementName>Variation du BFR</elementName>
                    <value period="1" type="actual" format="currency">62434.00</value>
                    <value period="3" type="actual" format="currency">154429.00</value>
                </element>
                <element code="DTRES6">
                    <elementName>Flux d'activité</elementName>
                    <value period="1" type="actual" format="currency">-74483.00</value>
                    <value period="3" type="estimated" format="currency">-110429.00</value>
                </element>
                <element code="DTRES7">
                    <elementName>Trésorerie nette de clôture au bilan</elementName>
                    <value period="1" type="actual" format="currency">536872.00</value>
                    <value period="2" type="actual" format="currency">35811.00</value>
                    <value period="3" type="actual" format="currency">-154952.00</value>
                </element>
                <element code="DTRES8">
                    <elementName>Trésorerie nette d'ouverture au bilan</elementName>
                    <value period="1" type="actual" format="currency">35811.00</value>
                    <value period="3" type="actual" format="currency">-194425.00</value>
                </element>
                <element code="DTRES9">
                    <elementName>Flux de trésorerie nette</elementName>
                    <value period="1" type="actual" format="currency">501061.00</value>
                    <value period="3" type="actual" format="currency">39473.00</value>
                </element>
                <element code="DTRES10">
                    <elementName>Cash Flow opérationnel (IFRS)</elementName>
                    <value period="1" type="actual" format="currency">-132664.00</value>
                    <value period="3" type="estimated" format="currency">-41251.00</value>
                </element>
            </financials>
            <financials origin="src" type="keyfigures" consolidated="false" ref="FINCAT" code="managerial-analyses">
                <financialsName>Soldes intermédiaires de Gestion</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DSIG1">
                    <elementName>Chiffre d'affaires</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">2318505.00</value>
                    <value period="3" type="estimated" percent="100.00" format="currency">1766000.00</value>
                </element>
                <element code="DSIG2">
                    <elementName>Ventes de marchandises</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG3">
                    <elementName>Coût d'achat des marchandises vendues</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG4">
                    <elementName>Marge commerciale</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG5">
                    <elementName>Production de l'exercice</elementName>
                    <value period="1" type="actual" percent="98.00" format="currency">2272164.00</value>
                </element>
                <element code="DSIG6">
                    <elementName>Production vendue</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">2318504.00</value>
                </element>
                <element code="DSIG7">
                    <elementName>Production stockée</elementName>
                    <value period="1" type="actual" percent="-2.00" format="currency">-46340.00</value>
                </element>
                <element code="DSIG8">
                    <elementName>Production immobilisée</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG9">
                    <elementName>Coût des matières premières et approvisionnement</elementName>
                    <value period="1" type="actual" percent="29.34" format="currency">680202.00</value>
                </element>
                <element code="DSIG10">
                    <elementName>Marge brute de production</elementName>
                    <value period="1" type="actual" percent="68.66" format="currency">1591962.00</value>
                </element>
                <element code="DSIG11">
                    <elementName>Marge globale</elementName>
                    <value period="1" type="actual" percent="68.66" format="currency">1591962.00</value>
                </element>
                <element code="DSIG12">
                    <elementName>Consommations externes hors crédit-bail, sous-traitance et personnel extérieur</elementName>
                    <value period="1" type="actual" percent="12.99" format="currency">301188.00</value>
                </element>
                <element code="DSIG13">
                    <elementName>Valeur ajoutée</elementName>
                    <value period="1" type="actual" percent="55.67" format="currency">1290775.00</value>
                </element>
                <element code="DSIG14">
                    <elementName>Charges de personnel</elementName>
                    <value period="1" type="actual" percent="57.49" format="currency">1332978.00</value>
                </element>
                <element code="DSIG15">
                    <elementName>Impôts et taxes</elementName>
                    <value period="1" type="actual" percent="0.62" format="currency">14375.00</value>
                </element>
                <element code="DSIG16">
                    <elementName>Subventions d'exploitation</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG17">
                    <elementName>Excédent brut d'exploitation</elementName>
                    <value period="1" type="actual" percent="-2.44" format="currency">-56578.00</value>
                    <value period="3" type="estimated" percent="1.25" format="currency">22000.00</value>
                </element>
                <element code="DSIG18">
                    <elementName>Autres produits, charges et reprises</elementName>
                    <value period="1" type="actual" percent="0.72" format="currency">16776.00</value>
                </element>
                <element code="DSIG19">
                    <elementName>Dotations d'exploitation, amortissements et provisions</elementName>
                    <value period="1" type="actual" percent="0.02" format="currency">498.00</value>
                </element>
                <element code="DSIG20">
                    <elementName>Résultat d'exploitation</elementName>
                    <value period="1" type="actual" percent="-1.74" format="currency">-40302.00</value>
                    <value period="3" type="estimated" percent="-1.81" format="currency">-32000.00</value>
                </element>
                <element code="DSIG21">
                    <elementName>Opérations en commun</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG22">
                    <elementName>Produits financiers</elementName>
                    <value period="1" type="actual" percent="1.86" format="currency">43170.00</value>
                </element>
                <element code="DSIG23">
                    <elementName>Charges financières retraitées</elementName>
                    <value period="1" type="actual" percent="0.16" format="currency">3813.00</value>
                </element>
                <element code="DSIG24">
                    <elementName>Intérêts et charges assimilées</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">13.00</value>
                </element>
                <element code="DSIG25">
                    <elementName>Résultat courant</elementName>
                    <value period="1" type="actual" percent="-0.04" format="currency">-945.00</value>
                    <value period="3" type="estimated" percent="-2.66" format="currency">-47000.00</value>
                </element>
                <element code="DSIG26">
                    <elementName>Produits exceptionnels</elementName>
                    <value period="1" type="actual" percent="6.45" format="currency">149614.00</value>
                </element>
                <element code="DSIG27">
                    <elementName>Charges exceptionnelles</elementName>
                    <value period="1" type="actual" percent="6.01" format="currency">139289.00</value>
                </element>
                <element code="DSIG28">
                    <elementName>Participation des salariés</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG29">
                    <elementName>Impôts sur les bénéfices</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG30">
                    <elementName>Résultat net</elementName>
                    <value period="1" type="actual" percent="0.40" format="currency">9378.00</value>
                    <value period="2" type="actual" format="currency">25362.00</value>
                    <value period="3" type="actual" percent="-1.74" format="currency">-30792.00</value>
                </element>
                <element code="DSIG31">
                    <elementName>Capacité d'autofinancement</elementName>
                    <value period="1" type="actual" percent="-0.52" format="currency">-12049.00</value>
                    <value period="3" type="estimated" percent="2.49" format="currency">44000.00</value>
                </element>
                <element code="DSIG32">
                    <elementName>Dividendes de l'exercice</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DSIG33">
                    <elementName>Autofinancement</elementName>
                    <value period="1" type="actual" percent="-0.52" format="currency">-12049.00</value>
                    <value period="3" type="estimated" percent="2.49" format="currency">44000.00</value>
                </element>
                <element code="DSIG34">
                    <elementName>Trésorerie nette</elementName>
                    <value period="1" type="actual" percent="23.16" format="currency">536872.00</value>
                    <value period="2" type="actual" format="currency">35811.00</value>
                    <value period="3" type="actual" percent="-8.77" format="currency">-154952.00</value>
                </element>
                <element code="DSIG35">
                    <elementName>Frais financiers du crédit-bail</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="DSIG36">
                    <elementName>Amortissements du crédit-bail</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="DSIG37">
                    <elementName>Personnel extérieur</elementName>
                    <value period="1" type="actual" format="currency">47613.00</value>
                </element>
                <element code="DSIG38">
                    <elementName>Sous-traitance non retraitée</elementName>
                    <value period="1" type="actual" format="currency">852783.00</value>
                </element>
                <element code="DSIG39">
                    <elementName>Part des salariés dans la valeur ajoutée</elementName>
                    <value period="1" type="actual" percent="103.27" format="currency">1332978.00</value>
                </element>
            </financials>
            <financials origin="src" type="keyfigures" consolidated="false">
                <financialsName>Chiffres clés</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="DGM1">
                    <elementName>Chiffre d'affaires</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">2318505.00</value>
                    <value period="3" type="actual" percent="100.00" format="currency">1766000.00</value>
                </element>
                <element code="DGM2">
                    <elementName>Chiffre d'affaires à l'export</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                </element>
                <element code="DGM3">
                    <elementName>Résultat d'exploitation</elementName>
                    <value period="1" type="actual" percent="-1.74" format="currency">-40302.00</value>
                    <value period="3" type="actual" percent="-1.81" format="currency">-32000.00</value>
                </element>
                <element code="DGM4">
                    <elementName>Excédent brut d'exploitation</elementName>
                    <value period="1" type="actual" percent="-2.44" format="currency">-56578.00</value>
                    <value period="3" type="actual" percent="1.25" format="currency">22000.00</value>
                </element>
                <element code="DGM5">
                    <elementName>Résultat courant</elementName>
                    <value period="1" type="actual" percent="-0.04" format="currency">-945.00</value>
                    <value period="3" type="actual" percent="-2.66" format="currency">-47000.00</value>
                </element>
                <element code="DGM6">
                    <elementName>Résultat net</elementName>
                    <value period="1" type="actual" percent="0.40" format="currency">9378.00</value>
                    <value period="2" type="actual" format="currency">25362.00</value>
                    <value period="3" type="actual" percent="-1.74" format="currency">-30792.00</value>
                </element>
                <element code="DGM7">
                    <elementName>Capacité d'autofinancement</elementName>
                    <value period="1" type="actual" percent="-0.52" format="currency">-12049.00</value>
                    <value period="3" type="actual" percent="2.49" format="currency">44000.00</value>
                </element>
                <element code="DGM8">
                    <elementName>Total bilan net retraité</elementName>
                    <value period="1" type="actual" percent="100.00" format="currency">900470.00</value>
                    <value period="2" type="actual" percent="100.00" format="currency">552486.00</value>
                    <value period="3" type="actual" percent="100.00" format="currency">940065.00</value>
                </element>
                <element code="DGM9">
                    <elementName>Capitaux propres non élargis aux CCA</elementName>
                    <value period="1" type="actual" percent="64.39" format="currency">579845.00</value>
                    <value period="2" type="actual" percent="12.75" format="currency">70466.00</value>
                    <value period="3" type="actual" percent="4.80" format="currency">45104.00</value>
                </element>
                <element code="DGM10">
                    <elementName>Capitaux propres</elementName>
                    <value period="1" type="actual" percent="64.39" format="currency">579845.00</value>
                    <value period="2" type="actual" percent="14.33" format="currency">79166.00</value>
                    <value period="3" type="actual" percent="15.55" format="currency">146215.00</value>
                </element>
                <element code="DGM11">
                    <elementName>Endettement financier brut</elementName>
                    <value period="1" type="actual" percent="0.00" format="currency">0.00</value>
                    <value period="2" type="actual" percent="1.57" format="currency">8700.00</value>
                    <value period="3" type="actual" percent="10.76" format="currency">101111.00</value>
                </element>
                <element code="DGM12">
                    <elementName>Trésorerie nette</elementName>
                    <value period="1" type="actual" percent="59.62" format="currency">536872.00</value>
                    <value period="2" type="actual" percent="6.48" format="currency">35811.00</value>
                    <value period="3" type="actual" percent="-16.48" format="currency">-154952.00</value>
                </element>
                <element code="DGM13">
                    <elementName>Endettement financier Net</elementName>
                    <value period="1" type="actual" percent="-59.62" format="currency">-536872.00</value>
                    <value period="2" type="actual" percent="-4.91" format="currency">-27111.00</value>
                    <value period="3" type="actual" percent="27.24" format="currency">256063.00</value>
                </element>
                <element code="DGM14">
                    <elementName>Effectif de l'entreprise</elementName>
                    <value period="3" type="actual" format="number">14</value>
                </element>
                <element code="DGM15">
                    <elementName>Engagement de crédit-bail</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="DGM16">
                    <elementName>Dettes groupe et associés</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">8700.00</value>
                    <value period="3" type="actual" format="currency">101111.00</value>
                </element>
                <element code="DGM17">
                    <elementName>Créances groupe et associés</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="DGM18">
                    <elementName>Effets portés à l'escompte et non échus</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="DGM19">
                    <elementName>Redevances de crédit-bail</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
            </financials>
            <financials origin="src" type="sectorcomparison">
                <financialsName>Positionnement sectoriel</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021</date>
                    <sector ref="APE2008" code="4120A">Construction de maisons individuelles</sector>
                    <turnOverRange>CA &lt; 3 ME</turnOverRange>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019</date>
                    <sector ref="APE2008" code="4120A">Construction de maisons individuelles</sector>
                    <turnOverRange>CA &lt; 3 ME</turnOverRange>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018</date>
                    <sector ref="APE2008" code="4120A">Construction de maisons individuelles</sector>
                    <turnOverRange>CA &lt; 3 ME</turnOverRange>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="RA01">
                    <elementName>Evolution du chiffre d'affaires (%)</elementName>
                    <value period="1" format="percent">-8.98</value>
                    <sector period="1" format="percent">9.00</sector>
                    <sector period="2" format="percent">3.07</sector>
                    <sector period="3" format="percent">3.83</sector>
                </element>
                <element code="RA06">
                    <elementName>E.B.E. (%)</elementName>
                    <value period="1" format="percent">-2.44</value>
                    <sector period="1" format="percent">5.54</sector>
                    <sector period="2" format="percent">4.80</sector>
                    <sector period="3" format="percent">4.56</sector>
                </element>
                <element code="RA08">
                    <elementName>Résultat d'exploitation (%)</elementName>
                    <value period="1" format="percent">-1.74</value>
                    <sector period="1" format="percent">3.77</sector>
                    <sector period="2" format="percent">3.22</sector>
                    <sector period="3" format="percent">3.07</sector>
                </element>
                <element code="RA09">
                    <elementName>Résultat courant avant impôts (%)</elementName>
                    <value period="1" format="percent">-0.04</value>
                    <sector period="1" format="percent">3.47</sector>
                    <sector period="2" format="percent">2.88</sector>
                    <sector period="3" format="percent">2.84</sector>
                </element>
                <element code="RA10">
                    <elementName>Résultat Net (%)</elementName>
                    <value period="1" format="percent">0.40</value>
                    <sector period="1" format="percent">2.99</sector>
                    <sector period="2" format="percent">2.42</sector>
                    <sector period="3" format="percent">2.53</sector>
                </element>
                <element code="RA20">
                    <elementName>Durée du Crédit Clients</elementName>
                    <value period="1" format="days">63.69</value>
                    <sector period="1" format="days">41.26</sector>
                    <sector period="2" format="days">44.09</sector>
                    <sector period="3" format="days">43.01</sector>
                </element>
                <element code="RA21">
                    <elementName>Durée du Crédit Fournisseurs</elementName>
                    <value period="1" format="days">42.22</value>
                    <sector period="1" format="days">37.83</sector>
                    <sector period="2" format="days">35.82</sector>
                    <sector period="3" format="days">39.08</sector>
                </element>
                <element code="RA32">
                    <elementName>Capacité d'Autofinancement (%)</elementName>
                    <value period="1" format="percent">-0.52</value>
                    <sector period="1" format="percent">4.64</sector>
                    <sector period="2" format="percent">3.98</sector>
                    <sector period="3" format="percent">4.07</sector>
                </element>
            </financials>
            <financials origin="csf" type="balancesheet" consolidated="false">
                <financialsName>Bilan</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="AI00" emphasis="bold" indent="1">
                    <elementName>Actif immobilisé</elementName>
                    <value period="1" type="actual" format="currency">48543.00</value>
                    <value period="2" type="actual" format="currency">112298.00</value>
                    <value period="3" type="actual" format="currency">478986.00</value>
                </element>
                <element code="AI01" emphasis="normal" indent="2">
                    <elementName>Immobilisations incorporelles</elementName>
                    <value period="1" type="actual" format="currency">35276.00</value>
                    <value period="2" type="actual" format="currency">35276.00</value>
                    <value period="3" type="actual" format="currency">43417.00</value>
                </element>
                <element code="AI02" emphasis="normal" indent="3">
                    <elementName>dont fonds commercial ou Goodwill</elementName>
                    <value period="1" type="actual" format="currency">35276.00</value>
                    <value period="2" type="actual" format="currency">35276.00</value>
                    <value period="3" type="actual" format="currency">43417.00</value>
                </element>
                <element code="AI03" emphasis="normal" indent="2">
                    <elementName>Immobilisations corporelles</elementName>
                    <value period="1" type="actual" format="currency">5520.00</value>
                    <value period="2" type="actual" format="currency">6020.00</value>
                    <value period="3" type="actual" format="currency">253413.00</value>
                </element>
                <element code="AI04" emphasis="normal" indent="3">
                    <elementName>dont terrains et locaux</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">25000.00</value>
                </element>
                <element code="AI05" emphasis="normal" indent="3">
                    <elementName>Installations techniques, matériel</elementName>
                    <value period="1" type="actual" format="currency">5271.00</value>
                    <value period="2" type="actual" format="currency">5654.00</value>
                    <value period="3" type="actual" format="currency">29398.00</value>
                </element>
                <element code="AI06" emphasis="normal" indent="2">
                    <elementName>Immobilisations financières</elementName>
                    <value period="1" type="actual" format="currency">7744.00</value>
                    <value period="2" type="actual" format="currency">71000.00</value>
                    <value period="3" type="actual" format="currency">182153.00</value>
                </element>
                <element code="AC00" emphasis="bold" indent="1">
                    <elementName>Actif circulant</elementName>
                    <value period="1" type="actual" format="currency">850604.00</value>
                    <value period="2" type="actual" format="currency">401074.00</value>
                    <value period="3" type="actual" format="currency">436705.00</value>
                </element>
                <element code="AC01" emphasis="normal" indent="2">
                    <elementName>Stocks</elementName>
                    <value period="1" type="actual" format="currency">13737.00</value>
                    <value period="2" type="actual" format="currency">78971.00</value>
                    <value period="3" type="actual" format="currency">77127.00</value>
                </element>
                <element code="AC02" emphasis="normal" indent="2">
                    <elementName>Créances</elementName>
                    <value period="1" type="actual" format="currency">299992.00</value>
                    <value period="2" type="actual" format="currency">285757.00</value>
                    <value period="3" type="actual" format="currency">359576.00</value>
                </element>
                <element code="AC03" emphasis="normal" indent="3">
                    <elementName>dont créances commerciales</elementName>
                    <value period="1" type="actual" format="currency">292934.00</value>
                    <value period="2" type="actual" format="currency">244867.00</value>
                    <value period="3" type="actual" format="currency">309142.00</value>
                </element>
                <element code="AC04" emphasis="normal" indent="3">
                    <elementName>dont créances intra groupe</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="AC05" emphasis="normal" indent="2">
                    <elementName>Valeurs mobilières de placement</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="AC06" emphasis="normal" indent="2">
                    <elementName>Disponibles</elementName>
                    <value period="1" type="actual" format="currency">536872.00</value>
                    <value period="2" type="actual" format="currency">36345.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="AC07" emphasis="normal" indent="2">
                    <elementName>Autres actifs</elementName>
                    <value period="1" type="actual" format="currency">1323.00</value>
                    <value period="2" type="actual" format="currency">39113.00</value>
                    <value period="3" type="actual" format="currency">24374.00</value>
                </element>
                <element code="CR00" emphasis="normal" indent="1">
                    <elementName>Comptes de régularisation</elementName>
                    <value period="1" type="actual" format="currency">1323.00</value>
                    <value period="2" type="actual" format="currency">39113.00</value>
                    <value period="3" type="actual" format="currency">24374.00</value>
                </element>
                <element code="TA00" emphasis="bold" indent="1">
                    <elementName>Total actif</elementName>
                    <value period="1" type="actual" format="currency">900470.00</value>
                    <value period="2" type="actual" format="currency">552488.00</value>
                    <value period="3" type="actual" format="currency">940066.00</value>
                </element>
                <element code="FP00" emphasis="bold" indent="1">
                    <elementName>Fonds propres</elementName>
                    <value period="1" type="actual" format="currency">579845.00</value>
                    <value period="2" type="actual" format="currency">70466.00</value>
                    <value period="3" type="actual" format="currency">45104.00</value>
                </element>
                <element code="FP01" emphasis="normal" indent="2">
                    <elementName>Capital social</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="FP02" emphasis="normal" indent="2">
                    <elementName>Réserves</elementName>
                    <value period="1" type="actual" format="currency">-520177.00</value>
                    <value period="2" type="actual" format="currency">-545540.00</value>
                    <value period="3" type="actual" format="currency">-514748.00</value>
                </element>
                <element code="FP03" emphasis="normal" indent="2">
                    <elementName>Report à nouveau</elementName>
                    <value period="1" type="actual" format="currency">-550177.00</value>
                    <value period="2" type="actual" format="currency">-575540.00</value>
                    <value period="3" type="actual" format="currency">-544748.00</value>
                </element>
                <element code="FP05" emphasis="bold" indent="1">
                    <elementName>Provisions</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">935.00</value>
                    <value period="3" type="actual" format="currency">21450.00</value>
                </element>
                <element code="DL00" emphasis="bold" indent="1">
                    <elementName>Dettes à long terme</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">8700.00</value>
                    <value period="3" type="actual" format="currency">101111.00</value>
                </element>
                <element code="DC00" emphasis="bold" indent="1">
                    <elementName>Dettes à court terme</elementName>
                    <value period="1" type="actual" format="currency">320625.00</value>
                    <value period="2" type="actual" format="currency">472384.00</value>
                    <value period="3" type="actual" format="currency">772400.00</value>
                </element>
                <element code="DC01" emphasis="normal" indent="2">
                    <elementName>Etablissements de crédit</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">534.00</value>
                    <value period="3" type="actual" format="currency">154952.00</value>
                </element>
                <element code="DC02" emphasis="normal" indent="2">
                    <elementName>Fournisseurs</elementName>
                    <value period="1" type="actual" format="currency">172005.00</value>
                    <value period="2" type="actual" format="currency">213305.00</value>
                    <value period="3" type="actual" format="currency">318887.00</value>
                </element>
                <element code="DC03" emphasis="normal" indent="2">
                    <elementName>Dettes intra groupe</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                    <value period="2" type="actual" format="currency">8700.00</value>
                    <value period="3" type="actual" format="currency">101111.00</value>
                </element>
                <element code="DC04" emphasis="normal" indent="2">
                    <elementName>Dettes fiscales et sociales</elementName>
                    <value period="1" type="actual" format="currency">121820.00</value>
                    <value period="2" type="actual" format="currency">102189.00</value>
                    <value period="3" type="actual" format="currency">229161.00</value>
                </element>
                <element code="TD00" emphasis="bold" indent="1">
                    <elementName>Total des dettes</elementName>
                    <value period="1" type="actual" format="currency">293825.00</value>
                    <value period="2" type="actual" format="currency">344910.00</value>
                    <value period="3" type="actual" format="currency">812345.00</value>
                </element>
                <element code="CR01" emphasis="normal" indent="1">
                    <elementName>Comptes de régularisation</elementName>
                    <value period="1" type="actual" format="currency">26800.00</value>
                    <value period="2" type="actual" format="currency">136174.00</value>
                    <value period="3" type="actual" format="currency">61166.00</value>
                </element>
                <element code="TP00" emphasis="bold" indent="1">
                    <elementName>Total passif</elementName>
                    <value period="1" type="actual" format="currency">900470.00</value>
                    <value period="2" type="actual" format="currency">552486.00</value>
                    <value period="3" type="actual" format="currency">940065.00</value>
                </element>
            </financials>
            <financials origin="csf" type="profitandloss" consolidated="false">
                <financialsName>Compte de résultat</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="CA00" emphasis="bold" indent="1">
                    <elementName>Chiffre d'affaires</elementName>
                    <value period="1" type="actual" format="currency">2318505.00</value>
                    <value period="3" type="estimated" format="currency">1766000.00</value>
                </element>
                <element code="CA01" emphasis="normal" indent="2">
                    <elementName>Chiffre d'affaires à l'export</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="AH00" emphasis="normal" indent="1">
                    <elementName>Achats</elementName>
                    <value period="1" type="actual" format="currency">1862893.00</value>
                    <value period="2" type="actual" format="currency">0.00</value>
                    <value period="3" type="actual" format="currency">0.00</value>
                </element>
                <element code="MB00" emphasis="normal" indent="1">
                    <elementName>Marge brute</elementName>
                    <value period="1" type="actual" format="currency">1591962.00</value>
                </element>
                <element code="PE00" emphasis="normal" indent="1">
                    <elementName>Produits d'exploitation</elementName>
                    <value period="1" type="actual" format="currency">2288953.00</value>
                </element>
                <element code="CE00" emphasis="normal" indent="1">
                    <elementName>Charges d'exploitation</elementName>
                    <value period="1" type="actual" format="currency">2329255.00</value>
                </element>
                <element code="CE01" emphasis="normal" indent="2">
                    <elementName>dont salaires et traitements</elementName>
                    <value period="1" type="actual" format="currency">291234.00</value>
                </element>
                <element code="CE02" emphasis="normal" indent="2">
                    <elementName>dont dotation aux amortissements</elementName>
                    <value period="1" type="actual" format="currency">498.00</value>
                </element>
                <element code="RE00" emphasis="bold" indent="1">
                    <elementName>Résultat d'exploitation</elementName>
                    <value period="1" type="actual" format="currency">-40302.00</value>
                </element>
                <element code="PF00" emphasis="normal" indent="1">
                    <elementName>Produits financiers</elementName>
                    <value period="1" type="actual" format="currency">43170.00</value>
                </element>
                <element code="CF01" emphasis="normal" indent="1">
                    <elementName>Charges financières</elementName>
                    <value period="1" type="actual" format="currency">3813.00</value>
                </element>
                <element code="RF00" emphasis="bold" indent="1">
                    <elementName>Résultat financier</elementName>
                    <value period="1" type="actual" format="currency">39356.00</value>
                </element>
                <element code="RA01" emphasis="bold" indent="1">
                    <elementName>Résultat avant impôts</elementName>
                    <value period="1" type="actual" format="currency">-945.00</value>
                    <value period="3" type="actual" format="currency">-47000.00</value>
                </element>
                <element code="PE01" emphasis="normal" indent="1">
                    <elementName>Produits exceptionnels</elementName>
                    <value period="1" type="actual" format="currency">149614.00</value>
                </element>
                <element code="CX00" emphasis="normal" indent="1">
                    <elementName>Charges exceptionnelles</elementName>
                    <value period="1" type="actual" format="currency">139289.00</value>
                </element>
                <element code="RX00" emphasis="bold" indent="1">
                    <elementName>Résultat exceptionnel</elementName>
                    <value period="1" type="actual" format="currency">10324.00</value>
                </element>
                <element code="IM00" emphasis="normal" indent="1">
                    <elementName>Impôts</elementName>
                    <value period="1" type="actual" format="currency">0.00</value>
                </element>
                <element code="RN00" emphasis="bold" indent="1">
                    <elementName>Résultat net</elementName>
                    <value period="1" type="actual" format="currency">9378.00</value>
                    <value period="2" type="actual" format="currency">25362.00</value>
                    <value period="3" type="actual" format="currency">-30792.00</value>
                </element>
            </financials>
            <financials origin="csf" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Activité</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="RE01">
                    <elementName>Evolution du CA</elementName>
                    <value period="1" type="actual" format="percent">-8.98</value>
                    <value period="3" type="actual" format="percent">-37.03</value>
                </element>
                <element code="RE02">
                    <elementName>Evolution du résultat d'exploitation</elementName>
                    <value period="1" type="actual" format="percent">-74.64</value>
                </element>
                <element code="RE12">
                    <elementName>Evolution du résultat d'exploitation retraité</elementName>
                    <value period="1" type="actual" format="percent">-74.64</value>
                    <value period="3" type="actual" format="percent">-63.58</value>
                </element>
                <element code="RE03">
                    <elementName>Evolution du résultat net</elementName>
                    <value period="1" type="actual" format="percent">-63.02</value>
                </element>
            </financials>
            <financials origin="csf" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Productivité et rentabilité</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="RR01">
                    <elementName>Rentabilité nette</elementName>
                    <value period="1" type="actual" format="percent">0.40</value>
                    <value period="3" type="estimated" format="percent">-1.74</value>
                </element>
                <element code="RR02">
                    <elementName>Rentabilité avant impôts</elementName>
                    <value period="1" type="actual" format="percent">-0.04</value>
                    <value period="3" type="estimated" format="percent">-2.66</value>
                </element>
                <element code="RR04">
                    <elementName>Rentabilité de l'actif</elementName>
                    <value period="1" type="actual" format="percent">-37.42</value>
                </element>
                <element code="RR05">
                    <elementName>Marge brute/CA</elementName>
                    <value period="1" type="actual" format="percent">68.66</value>
                    <value period="3" type="actual" format="percent">0.00</value>
                </element>
                <element code="RR06">
                    <elementName>Marge opérationnelle</elementName>
                    <value period="1" type="actual" format="percent">-1.74</value>
                    <value period="3" type="actual" format="percent">0.00</value>
                </element>
            </financials>
            <financials origin="csf" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Equilibre</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="IF01">
                    <elementName>Besoin en fond de roulement</elementName>
                    <value period="1" type="actual" format="currency">27832.00</value>
                    <value period="2" type="actual" format="currency">-34602.00</value>
                    <value period="3" type="actual" format="currency">-90470.00</value>
                </element>
                <element code="IF02">
                    <elementName>Capacité d'autofinancement</elementName>
                    <value period="1" type="actual" format="currency">-12049.00</value>
                    <value period="3" type="actual" format="currency">44000.00</value>
                </element>
                <element code="IF03">
                    <elementName>Gearing</elementName>
                    <value period="1" type="actual" format="percent">21.01</value>
                    <value period="2" type="actual" format="percent">186.76</value>
                    <value period="3" type="actual" format="percent">1094.04</value>
                </element>
                <element code="IF13">
                    <elementName>Gearing retraité</elementName>
                    <value period="3" type="actual" format="percent">567.72</value>
                </element>
                <element code="RF01">
                    <elementName>Autonomie Financière</elementName>
                    <value period="1" type="actual" format="percent">64.39</value>
                    <value period="2" type="actual" format="percent">14.33</value>
                    <value period="3" type="actual" format="percent">15.55</value>
                </element>
                <element code="RF02">
                    <elementName>Endettement à Long Terme</elementName>
                    <value period="1" type="actual" format="percent">0.00</value>
                    <value period="2" type="actual" format="percent">12.35</value>
                    <value period="3" type="actual" format="percent">224.17</value>
                </element>
            </financials>
            <financials origin="csf" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Exploitation</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="RX01">
                    <elementName>Délais de paiement des clients</elementName>
                    <value period="1" type="actual" format="days">63.69</value>
                    <value period="3" type="estimated" format="days">63.71</value>
                </element>
                <element code="RX02">
                    <elementName>Délais de paiement des fournisseurs</elementName>
                    <value period="1" type="actual" format="days">42.22</value>
                </element>
                <element code="RX03">
                    <elementName>Rotation des stocks</elementName>
                    <value period="1" type="actual" format="days">2.13</value>
                    <value period="3" type="actual" format="days">15.72</value>
                </element>
            </financials>
            <financials origin="csf" type="ratios" consolidated="false" ref="FINCAT" code="ratios-detail">
                <financialsName>Financement et trésorerie</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                    <sector>CIS</sector>
                    <duration unit="month">18</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                    <sector>CIS</sector>
                    <duration unit="month">12</duration>
                    <gaap ref="TYPBIL" code="SC">Comptes Sociaux Complets</gaap>
                    <currencyCode>EUR</currencyCode>
                    <currencyUnit>0</currencyUnit>
                </period>
                <element code="RT01">
                    <elementName>Liquidité générale</elementName>
                    <value period="1" type="actual" format="ratio">2.890</value>
                    <value period="2" type="actual" format="ratio">1.190</value>
                    <value period="3" type="actual" format="ratio">0.610</value>
                </element>
                <element code="RT02">
                    <elementName>Liquidité réduite</elementName>
                    <value period="1" type="actual" format="ratio">2.850</value>
                    <value period="2" type="actual" format="ratio">0.960</value>
                    <value period="3" type="actual" format="ratio">0.510</value>
                </element>
                <element code="RT03">
                    <elementName>Liquidité immédiate</elementName>
                    <value period="1" type="actual" format="ratio">1.670</value>
                    <value period="2" type="actual" format="ratio">0.080</value>
                    <value period="3" type="actual" format="ratio">0.000</value>
                </element>
            </financials>
            <financials origin="src" type="ratios" ref="FINCAT" code="financial-analysis">
                <financialsName>Synthèse financière</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                </period>
                <element code="DWARNING1">
                    <elementName>Équilibre financier</elementName>
                    <value period="1" format="text" type="actual">GREEN</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING2">
                    <elementName>Endettement</elementName>
                    <value period="1" format="text" type="actual">GREEN</value>
                    <value period="2" format="text" type="actual">GREEN</value>
                    <value period="3" format="text" type="actual">RED</value>
                </element>
                <element code="DWARNING3">
                    <elementName>Couverture de frais financiers</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING4">
                    <elementName>Liquidité</elementName>
                    <value period="1" format="text" type="actual">RED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING5">
                    <elementName>Flux de trésorerie</elementName>
                    <value period="1" format="text" type="actual">RED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <comment lang="fr">Le flux net de trésorerie de l'entreprise est positif. L'exploitation et l'activité globale n'ont néanmoins pas généré de cash.</comment>
                <comment lang="fr">Les deux flux potentiels de trésorerie de l'entreprise sont négatifs sur l'exercice. Malgré un niveau de liquidité encore correct, cette situation réduit sa capacité à pouvoir honorer ses dettes.</comment>
            </financials>
            <financials origin="src" type="ratios" ref="FINCAT" code="financial-warnings">
                <financialsName>Indicateurs financiers</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                </period>
                <element code="DSEUIL8">
                    <elementName>Marge brute d'exploitation</elementName>
                    <value period="1" format="text" type="actual">RED</value>
                    <comment period="1" lang="fr">La ressource tirée par l'entreprise de son cycle d'exploitation est faible. Inférieur à 2% du chiffre d'affaires, le niveau de marge brute, avant prise en compte des politiques de financement et d'investissement, constitue une fragilité.</comment>
                </element>
            </financials>
            <financials origin="src" type="ratios" ref="FINCAT" code="owcr-indicators">
                <financialsName>Indicateurs BFRE</financialsName>
                <period type="actual" number="1">
                    <date type="end">2021-06-30</date>
                </period>
                <period type="actual" number="2">
                    <date type="end">2019-12-31</date>
                </period>
                <period type="actual" number="3">
                    <date type="end">2018-06-30</date>
                </period>
                <element code="DWARNING7">
                    <elementName>BFRE</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING72">
                    <elementName>BFRE opérationnel</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING73">
                    <elementName>BFRE non opérationnel</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                </element>
                <element code="DWARNING74">
                    <elementName>BFRE opérationnel - Stocks</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                    <comment period="1" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="2" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="3" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                </element>
                <element code="DWARNING75">
                    <elementName>BFRE opérationnel - Clients</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                    <comment period="1" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="2" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="3" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                </element>
                <element code="DWARNING76">
                    <elementName>BFRE opérationnel - Fournisseurs</elementName>
                    <value period="1" format="text" type="actual">UNDEFINED</value>
                    <value period="2" format="text" type="actual">UNDEFINED</value>
                    <value period="3" format="text" type="actual">UNDEFINED</value>
                    <comment period="1" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="2" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                    <comment period="3" lang="fr">Non aplicable - Cet indicateur ne peut pas être calculé</comment>
                </element>
            </financials>
        </intlReport>
    </response>
</svcOnlineOrderResponse>"""


def prepare_xml_body(name, country_code):
    tree = ET.ElementTree(ET.fromstring(xml_body_search))
    tree.getroot().find('request/searchCriteria/name').text = name
    tree.getroot().find('request/searchCriteria/address/country').attrib['code'] = country_code
    xmlstr = ET.tostring(tree.getroot(), encoding='unicode')
    return xmlstr


def ellisphere_processing_search(xml_body):
    response = requests.post(url, data=xml_body, headers={'Content-Type': 'application/xml'})

    if response.status_code == 200:
        tree = ET.ElementTree(ET.fromstring(response.text))
        total = tree.getroot().find('response/providedHits').text

        if len(total) == 0:
            print('Aucun résultat trouvé')
            return

        for c in tree.getroot().findall('.//establishment')[:3]:
            # siren = national_id
            # siret = ellisphere provider id
            json = build_ellisphere_ids(c.findall('id'))

            json.update({
                "country_code": c.find('address/country').attrib['code'],
                "country": c.find('address/country').text,
                "name": c.find('name').text,
                "status": "Active" if c.attrib['companystatus'] == "active" else "Inactive",
                "postal_code": c.find('address/cityCode').text,
                "city": c.find('address/cityName').text,
                "adress_line": c.find('address/addressLine').text,

            })
            print(json)
            print('===============================')
    else:
        print('THROW EXCPETION HERE')
        # return 'THROW EXCPETION HERE'


# pip install json2xml
# pip install xmltodict
# def parse_xml_response(xml):
#     tree = ET.ElementTree(ET.fromstring(xml))
#     total = tree.getroot().find('response/providedHits').text
#     companies = []
#
#     if int(total) != 0:
#         for c in tree.getroot().findall('.//establishment')[:3]:
#             json = {}
#             for id in c.findall('id'):
#                 id_name = id.attrib['idName'].lower()
#                 if id_name == 'siren' or id_name == 'siret':
#                     json.update({id_name: id.text})
#
#             json.update({
#                 # "company_provider_id": c.find('id').attrib['idName'],
#                 "country_code": c.find('address/country').attrib['code'],
#                 "country": c.find('address/country').text,
#                 "name": c.find('name').text,
#                 "status": "Active" if c.attrib['companystatus'] == "active" else "Inactive",
#                 "postal_code": c.find('address/cityCode').text,
#                 "city": c.find('address/cityName').text,
#                 "adress_line": c.find('address/addressLine').text,
#
#             })
#             companies.append(json)
#     return companies

def build_ellisphere_ids(ids):
    json = {}
    for id in ids:
        id_name = id.attrib['type'].lower()
        if id_name == 'src':
            json.update({"company_provider_id": id.text})
        elif id_name == 'register':
            json.update({"national_id": id.text})
        else:
            json.update({id_name: id.text})

    return json


def prepare_xml_detail(company_provider_id, range, version):
    tree = ET.ElementTree(ET.fromstring(xml_details_body))
    tree.getroot().find('request/id').text = company_provider_id
    tree.getroot().find('request/product').attrib['range'] = range
    tree.getroot().find('request/product').attrib['version'] = version
    xmlstr = ET.tostring(tree.getroot(), encoding='unicode')
    return xmlstr


def detail():
    # xml_details = prepare_xml_detail("441768876", "101021", 1)
    response = requests.post(url_details, data=xml_details_body, headers={'Content-Type': 'Application/xml'})
    # print(response.text)
    # print(response.text)
    tree = ET.ElementTree(ET.fromstring(response.text))
    assessmentData = tree.getroot().find('response/intlReport/assessmentData')
    scores = assessmentData.findall('score')
    for s in scores:
        res = {
            "date": s.find('date').text,
            "origin": s.attrib['origin']
        }

        for v in s.findall('value'):
            res.update({v.attrib['type']: v.text})
        print(res)
        print('==============')


if __name__ == '__main__':
    # body = prepare_xml_body("CARTAN", "gbr")
    # ellisphere_processing_search(body)
    detail()
    # xml_details = prepare_xml_detail("11", "22", "3")
    # print(xml_details)

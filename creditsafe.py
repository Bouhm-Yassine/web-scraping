from datetime import datetime

import requests

data = {
    "correlationId": "c85e5f4e-c257-4397-a6bf-2d7adc0aed41",
    "report": {
        "companyId": "FR-X-49481445200012",
        "language": "EN",
        "companySummary": {
            "businessName": "LE JULES VERNE",
            "country": "FR",
            "companyNumber": "FR09532031",
            "companyRegistrationNumber": "49481445200012",
            "mainActivity": {
                "code": "5610A",
                "description": "Restauration traditionnelle",
                "classification": "NAF/APE"
            },
            "companyStatus": {
                "status": "NonActive",
                "description": "Closed"
            },
            "latestTurnoverFigure": {
                "currency": "EUR",
                "value": 226415
            },
            "latestShareholdersEquityFigure": {
                "currency": "EUR",
                "value": -167924
            },
            "creditRating": {
                "commonValue": "E",
                "commonDescription": "Not Scored",
                "creditLimit": {
                    "value": "Credit Limit not applicable"
                },
                "providerValue": {
                    "maxValue": "100",
                    "minValue": "0",
                    "value": "Not Rated"
                },
                "providerDescription": "Company in situation of failure and with a very high risk of winding up"
            }
        },
        "companyIdentification": {
            "basicInformation": {
                "businessName": "LE JULES VERNE",
                "registeredCompanyName": "SCORE",
                "companyRegistrationNumber": "49481445200012",
                "country": "FR",
                "vatRegistrationNumber": "FR85494814452",
                "companyRegistrationDate": "2007-03-29T00:00:00Z",
                "operationsStartDate": "2007-04-01T00:00:00Z",
                "commercialCourt": "RCS Orleans",
                "legalForm": {
                    "providerCode": "5499",
                    "description": "Limited Liability Company"
                },
                "companyStatus": {
                    "status": "NonActive",
                    "description": "Closed"
                },
                "principalActivity": {
                    "code": "5610A",
                    "description": "Restauration traditionnelle",
                    "classification": "NAF/APE"
                },
                "contactAddress": {
                    "simpleValue": "18 RUE EUGENE VIGNAT 45000 ORLEANS",
                    "street": "18 RUE EUGENE VIGNAT",
                    "houseNumber": "18",
                    "city": "ORLEANS",
                    "postalCode": "45000",
                    "province": "Centre",
                    "country": "FR"
                }
            },
            "activityClassifications": [
                {
                    "classification": "NAF/APE",
                    "activities": [
                        {
                            "code": "5610A",
                            "description": "Restauration traditionnelle"
                        }
                    ]
                }
            ]
        },
        "creditScore": {
            "currentCreditRating": {
                "commonValue": "E",
                "commonDescription": "Not Scored",
                "creditLimit": {
                    "value": "Credit Limit not applicable"
                },
                "providerValue": {
                    "maxValue": "100",
                    "minValue": "0",
                    "value": "Not Rated"
                },
                "providerDescription": "Company in situation of failure and with a very high risk of winding up"
            },
            "previousCreditRating": {
                "commonValue": "E",
                "commonDescription": "Not Scored",
                "creditLimit": {
                    "currency": "EUR",
                    "value": "0"
                },
                "providerValue": {
                    "maxValue": "100",
                    "minValue": "0",
                    "value": "Not Rated"
                },
                "providerDescription": "Company in situation of failure and with a very high risk of winding up"
            },
            "latestRatingChangeDate": "2021-05-07T00:00:00Z"
        },
        "contactInformation": {
            "mainAddress": {
                "simpleValue": "18 RUE EUGENE VIGNAT  45000 ORLEANS",
                "street": "RUE EUGENE VIGNAT",
                "houseNumber": "18",
                "city": "ORLEANS",
                "postalCode": "45000",
                "province": "Centre",
                "country": "FR"
            }
        },
        "shareCapitalStructure": {
            "nominalShareCapital": {
                "value": 7500
            }
        },
        "directors": {
            "currentDirectors": [
                {
                    "name": "M DUBOIS FLORENT JEAN ROGER ANDRE",
                    "gender": "Male",
                    "dateOfBirth": "1962-01-10T00:00:00Z",
                    "placeOfBirth": "CHATELLERAULT (86100)",
                    "directorType": "Person",
                    "positions": [
                        {
                            "positionName": "Manager"
                        }
                    ]
                }
            ],
            "previousDirectors": [
                {
                    "name": "M FLORENT JEAN ROGER ANDRE DUBOIS",
                    "gender": "Male",
                    "dateOfBirth": "1962-01-10T00:00:00Z",
                    "placeOfBirth": "CHATELLERAULT (86)",
                    "directorType": "Person",
                    "positions": [
                        {
                            "positionName": "Manager"
                        }
                    ]
                },
                {
                    "name": "M FLORENT JEAN ROGER ANDRE DUBOIS",
                    "gender": "Male",
                    "dateOfBirth": "1962-01-10T00:00:00Z",
                    "placeOfBirth": "CHATELLERAULT (86)",
                    "directorType": "Person",
                    "positions": [
                        {
                            "positionName": "Manager"
                        }
                    ]
                },
                {
                    "name": "M FLORENT DUBOIS",
                    "gender": "Male",
                    "dateOfBirth": "1962-01-10T00:00:00Z",
                    "placeOfBirth": "CHATELLERAULT",
                    "directorType": "Person",
                    "positions": [
                        {
                            "positionName": "Manager"
                        }
                    ]
                }
            ]
        },
        "otherInformation": {
            "employeesInformation": [
                {
                    "year": 2010,
                    "numberOfEmployees": "3"
                }
            ]
        },
        "financialStatements": [
            {
                "type": "GlobalFinancialsGGS",
                "yearEndDate": "2010-09-30T00:00:00Z",
                "numberOfWeeks": 52,
                "currency": "EUR",
                "profitAndLoss": {
                    "revenue": 234683,
                    "operatingCosts": 244458,
                    "operatingProfit": -9775,
                    "wagesAndSalaries": 62309,
                    "pensionCosts": 15783,
                    "depreciation": 20642,
                    "financialIncome": 0,
                    "financialExpenses": 12007,
                    "extraordinaryIncome": 6514,
                    "extraordinaryCosts": 21010,
                    "profitBeforeTax": -36276,
                    "tax": 0,
                    "profitAfterTax": -36276,
                    "dividends": 0,
                    "retainedProfit": -36276
                },
                "balanceSheet": {
                    "landAndBuildings": 0,
                    "plantAndMachinery": 23314,
                    "otherTangibleAssets": 67552,
                    "totalTangibleAssets": 90866,
                    "goodwill": 140200,
                    "otherIntangibleAssets": 0,
                    "totalIntangibleAssets": 140200,
                    "investments": 15,
                    "loansToGroup": 0,
                    "otherLoans": 0,
                    "miscellaneousFixedAssets": 5668,
                    "totalOtherFixedAssets": 5683,
                    "totalFixedAssets": 236749,
                    "rawMaterials": 3021,
                    "workInProgress": 0,
                    "finishedGoods": 0,
                    "otherInventories": 0,
                    "totalInventories": 3021,
                    "tradeReceivables": 800,
                    "miscellaneousReceivables": 13061,
                    "totalReceivables": 13861,
                    "cash": 16104,
                    "otherCurrentAssets": 968,
                    "totalCurrentAssets": 33954,
                    "totalAssets": 270703,
                    "tradePayables": 72881,
                    "bankLiabilities": 143297,
                    "otherLoansOrFinance": 92524,
                    "miscellaneousLiabilities": 129924,
                    "totalCurrentLiabilities": 438626,
                    "bankLiabilitiesDueAfter1Year": 0,
                    "otherLoansOrFinanceDueAfter1Year": 0,
                    "miscellaneousLiabilitiesDueAfter1Year": 0,
                    "totalLongTermLiabilities": 0,
                    "totalLiabilities": 438626,
                    "calledUpShareCapital": 7500,
                    "sharePremium": 0,
                    "revenueReserves": -183787,
                    "otherReserves": 8363,
                    "totalShareholdersEquity": -167924
                },
                "otherFinancials": {
                    "workingCapital": -404672,
                    "netWorth": -308124
                },
                "ratios": {
                    "preTaxProfitMargin": -15.46,
                    "returnOnCapitalEmployed": 21.6,
                    "returnOnTotalAssetsEmployed": -13.4,
                    "returnOnNetAssetsEmployed": 21.6,
                    "salesOrNetWorkingCapital": -0.58,
                    "stockTurnoverRatio": 1.29,
                    "debtorDays": 1.24,
                    "creditorDays": 113.35,
                    "currentRatio": 0.08,
                    "liquidityRatioOrAcidTest": 0.07,
                    "currentDebtRatio": -2.61,
                    "gearing": -85.33,
                    "equityInPercentage": -128.67,
                    "totalDebtRatio": -2.61
                }
            },
            {
                "type": "GlobalFinancialsGGS",
                "yearEndDate": "2009-09-30T00:00:00Z",
                "numberOfWeeks": 52,
                "currency": "EUR",
                "profitAndLoss": {
                    "revenue": 363697,
                    "operatingCosts": 400726,
                    "operatingProfit": -37029,
                    "wagesAndSalaries": 84907,
                    "pensionCosts": 24335,
                    "depreciation": 23336,
                    "financialIncome": 0,
                    "financialExpenses": 8688,
                    "extraordinaryIncome": 6426,
                    "extraordinaryCosts": 16497,
                    "profitBeforeTax": -55790,
                    "tax": 0,
                    "profitAfterTax": -55790,
                    "dividends": 0,
                    "retainedProfit": -55790
                },
                "balanceSheet": {
                    "landAndBuildings": 0,
                    "plantAndMachinery": 29846,
                    "otherTangibleAssets": 85385,
                    "totalTangibleAssets": 115231,
                    "goodwill": 140200,
                    "otherIntangibleAssets": 0,
                    "totalIntangibleAssets": 140200,
                    "investments": 15,
                    "loansToGroup": 0,
                    "otherLoans": 0,
                    "miscellaneousFixedAssets": 5232,
                    "totalOtherFixedAssets": 5247,
                    "totalFixedAssets": 260678,
                    "rawMaterials": 5050,
                    "workInProgress": 0,
                    "finishedGoods": 0,
                    "otherInventories": 0,
                    "totalInventories": 5050,
                    "tradeReceivables": 912,
                    "miscellaneousReceivables": 4791,
                    "totalReceivables": 5703,
                    "cash": 21660,
                    "otherCurrentAssets": 5033,
                    "totalCurrentAssets": 37446,
                    "totalAssets": 298124,
                    "tradePayables": 64612,
                    "bankLiabilities": 34369,
                    "otherLoansOrFinance": 71732,
                    "miscellaneousLiabilities": 125787,
                    "totalCurrentLiabilities": 296500,
                    "bankLiabilitiesDueAfter1Year": 129090,
                    "otherLoansOrFinanceDueAfter1Year": 0,
                    "miscellaneousLiabilitiesDueAfter1Year": 0,
                    "totalLongTermLiabilities": 129090,
                    "totalLiabilities": 425590,
                    "calledUpShareCapital": 7500,
                    "sharePremium": 0,
                    "revenueReserves": -147510,
                    "otherReserves": 12543,
                    "totalShareholdersEquity": -127467
                },
                "otherFinancials": {
                    "workingCapital": -259054,
                    "netWorth": -267667
                },
                "ratios": {
                    "preTaxProfitMargin": -15.34,
                    "returnOnCapitalEmployed": -3437.46,
                    "returnOnTotalAssetsEmployed": -18.71,
                    "returnOnNetAssetsEmployed": 43.77,
                    "salesOrNetWorkingCapital": -1.4,
                    "stockTurnoverRatio": 1.39,
                    "debtorDays": 0.92,
                    "creditorDays": 64.84,
                    "currentRatio": 0.13,
                    "liquidityRatioOrAcidTest": 0.11,
                    "currentDebtRatio": -2.33,
                    "gearing": -128.24,
                    "equityInPercentage": -80.71,
                    "totalDebtRatio": -3.34
                }
            },
            {
                "type": "GlobalFinancialsGGS",
                "yearEndDate": "2008-09-30T00:00:00Z",
                "numberOfWeeks": 52,
                "currency": "EUR",
                "profitAndLoss": {
                    "revenue": 545702,
                    "operatingCosts": 625243,
                    "operatingProfit": -79541,
                    "wagesAndSalaries": 145335,
                    "pensionCosts": 36733,
                    "depreciation": 23183,
                    "financialIncome": 0,
                    "financialExpenses": 14950,
                    "extraordinaryIncome": 13181,
                    "extraordinaryCosts": 10408,
                    "profitBeforeTax": -91720,
                    "tax": 0,
                    "profitAfterTax": -91720,
                    "dividends": 0,
                    "retainedProfit": -91720
                },
                "balanceSheet": {
                    "landAndBuildings": 0,
                    "plantAndMachinery": 32552,
                    "otherTangibleAssets": 100082,
                    "totalTangibleAssets": 132634,
                    "goodwill": 140200,
                    "otherIntangibleAssets": 2183,
                    "totalIntangibleAssets": 142383,
                    "investments": 15,
                    "loansToGroup": 0,
                    "otherLoans": 0,
                    "miscellaneousFixedAssets": 5232,
                    "totalOtherFixedAssets": 5247,
                    "totalFixedAssets": 280264,
                    "rawMaterials": 10250,
                    "workInProgress": 0,
                    "finishedGoods": 0,
                    "otherInventories": 0,
                    "totalInventories": 10250,
                    "tradeReceivables": 4823,
                    "miscellaneousReceivables": 9781,
                    "totalReceivables": 14604,
                    "cash": 8897,
                    "otherCurrentAssets": 2012,
                    "totalCurrentAssets": 35763,
                    "totalAssets": 316027,
                    "tradePayables": 58353,
                    "bankLiabilities": 33440,
                    "otherLoansOrFinance": 62860,
                    "miscellaneousLiabilities": 54717,
                    "totalCurrentLiabilities": 209370,
                    "bankLiabilitiesDueAfter1Year": 174153,
                    "otherLoansOrFinanceDueAfter1Year": 0,
                    "miscellaneousLiabilitiesDueAfter1Year": 0,
                    "totalLongTermLiabilities": 174153,
                    "totalLiabilities": 383523,
                    "calledUpShareCapital": 7500,
                    "sharePremium": 0,
                    "revenueReserves": -91720,
                    "otherReserves": 16723,
                    "totalShareholdersEquity": -67497
                },
                "otherFinancials": {
                    "workingCapital": -173607,
                    "netWorth": -209880
                },
                "ratios": {
                    "preTaxProfitMargin": -16.81,
                    "returnOnCapitalEmployed": -86,
                    "returnOnTotalAssetsEmployed": -29.02,
                    "returnOnNetAssetsEmployed": 135.89,
                    "salesOrNetWorkingCapital": -3.14,
                    "stockTurnoverRatio": 1.88,
                    "debtorDays": 3.23,
                    "creditorDays": 39.03,
                    "currentRatio": 0.17,
                    "liquidityRatioOrAcidTest": 0.12,
                    "currentDebtRatio": -3.1,
                    "gearing": -307.56,
                    "equityInPercentage": -38.87,
                    "totalDebtRatio": -5.68
                }
            }
        ],
        "localFinancialStatements": [
            {
                "type": "LocalFinancialsSynthesizedCSFR",
                "yearEndDate": "2010-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 12,
                "financialReportDescription": "Normal Account",
                "dateOfCapture": "2011-10-18T00:00:00Z",
                "numberOfEmployees": 3,
                "activityCode": "5610A",
                "assets": {
                    "capitalNotCalled": 0,
                    "totalFixedAssets": 236749,
                    "intangibleAssets": 140200,
                    "tangibleAssets": 90866,
                    "financialAssets": 5683,
                    "netCurrentAssets": 33952,
                    "stocks": 3021,
                    "advancedPayments": 0,
                    "receivables": 14827,
                    "tradeReceivables": 800,
                    "miscellaneousReceivables": 13061,
                    "securitiesAndCash": 16104,
                    "accountsOfRegularization": 0,
                    "totalAssets": 270703,
                    "miscellaneousTotalAssets": 236751,
                    "netWorth": -308124
                },
                "liabilities": {
                    "shareholdersEquity": -167924,
                    "shareCapital": 7500,
                    "revaluationReserve": 0,
                    "otherReserves": -175424,
                    "otherCapitalResources": 0,
                    "provisionsForRisksAndCharges": 0,
                    "liabilities": 438626,
                    "financialLiabilities": 235821,
                    "advancedPaymentsReceived": 0,
                    "tradeAccountPayables": 72881,
                    "taxAndSocialLiabilities": 48649,
                    "otherDebtsAndFixedAssetsLiabilities": 81275,
                    "accountRegularization": 0,
                    "totalLiabilitiesAndEquity": 270702,
                    "bankLoansAndLiabilities": 0,
                    "sundryLoansAndLiabilities": 92524,
                    "miscellaneousLiabilities": 81275
                },
                "profitAndLoss": {
                    "salesOfGoods": 234683,
                    "netTurnover": 226415,
                    "netExportTurnover": 0,
                    "operatingCharges": 244458,
                    "operatingProfit": -9775,
                    "financialIncome": 0,
                    "financialCharges": 12007,
                    "financialProfitOrLoss": -12007,
                    "pretaxNetOperatingIncome": -21782,
                    "extraordinaryIncome": 6514,
                    "extraordinaryCharges": 21010,
                    "extraordinaryProfitOrLoss": -14496,
                    "netResult": -36276
                }
            },
            {
                "type": "LocalFinancialsSynthesizedCSFR",
                "yearEndDate": "2009-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 12,
                "financialReportDescription": "Normal Account",
                "dateOfCapture": "2010-09-29T00:00:00Z",
                "numberOfEmployees": 0,
                "activityCode": "5610A",
                "assets": {
                    "capitalNotCalled": 0,
                    "totalFixedAssets": 260678,
                    "intangibleAssets": 140200,
                    "tangibleAssets": 115231,
                    "financialAssets": 5247,
                    "netCurrentAssets": 37444,
                    "stocks": 5050,
                    "advancedPayments": 0,
                    "receivables": 10734,
                    "tradeReceivables": 912,
                    "miscellaneousReceivables": 4791,
                    "securitiesAndCash": 21660,
                    "accountsOfRegularization": 0,
                    "totalAssets": 298124,
                    "miscellaneousTotalAssets": 260680,
                    "netWorth": -267667
                },
                "liabilities": {
                    "shareholdersEquity": -127467,
                    "shareCapital": 7500,
                    "revaluationReserve": 0,
                    "otherReserves": -134967,
                    "otherCapitalResources": 0,
                    "provisionsForRisksAndCharges": 0,
                    "liabilities": 425589,
                    "financialLiabilities": 235191,
                    "advancedPaymentsReceived": 0,
                    "tradeAccountPayables": 64612,
                    "taxAndSocialLiabilities": 71443,
                    "otherDebtsAndFixedAssetsLiabilities": 54343,
                    "accountRegularization": 0,
                    "totalLiabilitiesAndEquity": 298123,
                    "bankLoansAndLiabilities": 0,
                    "sundryLoansAndLiabilities": 71732,
                    "miscellaneousLiabilities": 54343
                },
                "profitAndLoss": {
                    "salesOfGoods": 363697,
                    "netTurnover": 351873,
                    "netExportTurnover": 0,
                    "operatingCharges": 400726,
                    "operatingProfit": -37029,
                    "financialIncome": 0,
                    "financialCharges": 8688,
                    "financialProfitOrLoss": -8688,
                    "pretaxNetOperatingIncome": -45717,
                    "extraordinaryIncome": 6426,
                    "extraordinaryCharges": 16497,
                    "extraordinaryProfitOrLoss": -10071,
                    "netResult": -55790
                }
            },
            {
                "type": "LocalFinancialsSynthesizedCSFR",
                "yearEndDate": "2008-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 18,
                "financialReportDescription": "Normal Account",
                "dateOfCapture": "2010-09-29T00:00:00Z",
                "numberOfEmployees": 0,
                "activityCode": "5610A",
                "assets": {
                    "capitalNotCalled": 0,
                    "totalFixedAssets": 280264,
                    "intangibleAssets": 142383,
                    "tangibleAssets": 132634,
                    "financialAssets": 5247,
                    "netCurrentAssets": 35763,
                    "stocks": 10250,
                    "advancedPayments": 0,
                    "receivables": 16616,
                    "tradeReceivables": 4823,
                    "miscellaneousReceivables": 9781,
                    "securitiesAndCash": 8897,
                    "accountsOfRegularization": 0,
                    "totalAssets": 316027,
                    "miscellaneousTotalAssets": 280264,
                    "netWorth": -209880
                },
                "liabilities": {
                    "shareholdersEquity": -67497,
                    "shareCapital": 7500,
                    "revaluationReserve": 0,
                    "otherReserves": -74997,
                    "otherCapitalResources": 0,
                    "provisionsForRisksAndCharges": 0,
                    "liabilities": 383522,
                    "financialLiabilities": 270453,
                    "advancedPaymentsReceived": 0,
                    "tradeAccountPayables": 58353,
                    "taxAndSocialLiabilities": 35156,
                    "otherDebtsAndFixedAssetsLiabilities": 19560,
                    "accountRegularization": 0,
                    "totalLiabilitiesAndEquity": 316026,
                    "bankLoansAndLiabilities": 0,
                    "sundryLoansAndLiabilities": 62860,
                    "miscellaneousLiabilities": 19560
                },
                "profitAndLoss": {
                    "salesOfGoods": 545702,
                    "netTurnover": 504987,
                    "netExportTurnover": 0,
                    "operatingCharges": 625243,
                    "operatingProfit": -79541,
                    "financialIncome": 0,
                    "financialCharges": 14950,
                    "financialProfitOrLoss": -14950,
                    "pretaxNetOperatingIncome": -94491,
                    "extraordinaryIncome": 13181,
                    "extraordinaryCharges": 10408,
                    "extraordinaryProfitOrLoss": 2773,
                    "netResult": -91720
                }
            },
            {
                "type": "LocalFinancialsFullCSFR",
                "yearEndDate": "2010-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 12,
                "assets": {
                    "grandTotalAssets": {
                        "grandTotalNet": 270703,
                        "grandTotalGross": 328436,
                        "grandTotalAmortisation": 57733
                    },
                    "capitalSubscribedNotCalled": {
                        "capitalSubscribed": 0,
                        "grossCapitalSubscribed": 0
                    },
                    "activeFixedAsset": {
                        "total": 236749,
                        "gross": 294482,
                        "amortisation": 57733
                    },
                    "activeIntangibleFixedAssets": {
                        "startupCost": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "researchAndDevelopmentExpenses": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "distributorshipsPatents": {
                            "total": 0,
                            "gross": 3460,
                            "amortisation": 3460
                        },
                        "goodwill": {
                            "total": 140200,
                            "gross": 140200,
                            "amortisation": 0
                        },
                        "otherIntangibleFixedAssets": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "prepaymentsAndDownpayments": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalIntangibleAsset": 140200
                    },
                    "tangilbleFixedAssets": {
                        "land": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "buildings": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "plant": {
                            "total": 23314,
                            "gross": 39162,
                            "amortisation": 15848
                        },
                        "otherTangibleFixedAssets": {
                            "total": 67552,
                            "gross": 105977,
                            "amortisation": 38425
                        },
                        "fixedAssetsInConstruction": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "advancesAndPaymentsOnAccount": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalTangibleAsset": 90866
                    },
                    "financialAssets": {
                        "associatesAtEquity": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherParticipations": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "intercompanyReceivables": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherInvestmentSecurities": {
                            "total": 15,
                            "gross": 15,
                            "amortisation": 0
                        },
                        "loans": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherFinancialAssets": {
                            "total": 5668,
                            "gross": 5668,
                            "amortisation": 0
                        },
                        "subTotalFinancialAssets": 5683
                    },
                    "activeAssets": {
                        "total": 33952,
                        "gross": 33952,
                        "amortisation": 0
                    },
                    "activeStocks": {
                        "rawMaterials": {
                            "total": 3021,
                            "gross": 3021,
                            "amortisation": 0
                        },
                        "workInProgressGoods": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "workInProgressServices": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "semiFinishedAndFinishedProducts": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "goodsForResale": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalStocks": 3021
                    },
                    "advancePaymentsToSupplier": {
                        "total": 0,
                        "gross": 0,
                        "amortisation": 0
                    },
                    "activeDebtors": {
                        "tradeAccountsReceivable": {
                            "total": 800,
                            "gross": 800,
                            "amortisation": 0
                        },
                        "otherDebtors": {
                            "total": 13061,
                            "gross": 13061,
                            "amortisation": 0
                        },
                        "capitalSubscribedAndCalledUp": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalDebtors": 13861
                    },
                    "activeDivers": {
                        "investmentSecurities": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "cashAndCashEquivalents": {
                            "total": 16104,
                            "gross": 16104,
                            "amortisation": 0
                        },
                        "subTotalDivers": 16104
                    },
                    "accountPrepaidExpenses": {
                        "total": 966,
                        "gross": 966,
                        "amortisation": 0
                    },
                    "equalizationAccounts": {
                        "multiPeriodCharges": 0,
                        "multiPeriodChargesGross": 0,
                        "premiumsOnRedemptionOfBonds": 0,
                        "premiumsOnRedemptionOfBondsGross": 0,
                        "currencyDifferentialGain": 0,
                        "currencyDifferentialGainGross": 0
                    },
                    "assetsReferences": {
                        "dueWithinOneYear": 0,
                        "dueAfterOneYear": 0
                    }
                },
                "liabilities": {
                    "grandTotal": 270702,
                    "shareholderEquity": {
                        "totalShareholdersEquity": -167924,
                        "equityAndShareholdersEquity": 7500,
                        "issueAndMergerPremiums": 0,
                        "revaluationDifferentials": 0,
                        "ofWhichEquityDiffeential": 0,
                        "legalReserve": 0,
                        "statutoryOrContractualReserve": 0,
                        "specialRegulatedReserves": 0,
                        "ofWhichSpecialReserveOfProvisions": 0,
                        "otherReservesOfLiabilities": 0,
                        "ofWhichReserveForBuyingOriginalsWorks": 0,
                        "profitsOrLossesBroughtForward": -147511,
                        "profitOrLossForThePeriod": -36276,
                        "investmentGrants": 8363,
                        "specialTaxAllowableReserves": 0
                    },
                    "otherCapitalResource": {
                        "totalOtherCapitalResources": 0,
                        "incomeFromParticipatingSecurities": 0,
                        "conditionalLoans": 0
                    },
                    "provisionsForRisksAndCharge": {
                        "totalProvisionsForRisksAndCharges": 0,
                        "riskProvisions": 0,
                        "reservesForCharges": 0
                    },
                    "liabilities": {
                        "totalLiabilities": 438626,
                        "convertibleDebentures": 0,
                        "otherDebentures": 0,
                        "bankLoansAndLiabilities": 143297,
                        "sundryLoansAndFinancialLiabilities": 92524,
                        "ofWhichParticipatingLoans": 0,
                        "advancePaymentsReceivedForCurrentOrders": 0,
                        "tradeAccountsPayables": 72881,
                        "taxAndSocialSecurityLiabilities": 48649,
                        "fixedAssetLiabilities": 0,
                        "otherDebts": 81275
                    },
                    "passiveAccountReferences": {
                        "ofWhichTaxAllowableReserve": 0,
                        "deferredIncomeAndLiabilities": 438626,
                        "ofWhichCurrentBankFacilities": 0
                    },
                    "extraInformation": {
                        "taxAllowableReserve": 0,
                        "deferredIncomeLiabilities": 438626,
                        "deferredBankIncome": 0,
                        "deferredIncome": 0,
                        "passiveTranslationLoss": 0
                    }
                },
                "profitAndLoss": {
                    "operatingResult": -9775,
                    "financialResult": -12007,
                    "resultsOfPreTaxNetOperatingIncome": -21782,
                    "extraordinaryResult": -14496,
                    "profitOrLoss": -36276,
                    "totalIncome": 241197,
                    "totalCharges": 277475,
                    "employeeProfitSharing": 0,
                    "taxOnProfits": 0,
                    "operatingIncome": {
                        "totalOperatingIncome": 234683,
                        "goodsForResaleTotal": 0,
                        "goodsForResaleFrance": 0,
                        "goodsForResaleExport": 0,
                        "goodsProducedTotal": 208671,
                        "goodsProducedFrance": 208671,
                        "goodsProducedExport": 0,
                        "saleOfServicesTotal": 17744,
                        "saleOfServicesFrance": 17744,
                        "saleOfServicesExport": 0,
                        "netTurnoverTotal": 226415,
                        "netTurnoverFrance": 226415,
                        "netTurnoverExport": 0,
                        "stockedProduction": 0,
                        "selfConstructedAssets": 0,
                        "operatingGrants": 3678,
                        "releaseOfReservesAndProvisions": 4568,
                        "otherIncome": 22
                    },
                    "totalOperatingCharge": {
                        "totalOperatingCharges": 244458,
                        "purchaseOfGoodsForResale": 0,
                        "changeInStocksOfGoodsForResale": 0,
                        "purchaseOfRawMaterials": 55586,
                        "changeInStocksOfRawMaterials": 2029,
                        "otherExternalPurchasesAndCharges": 76061,
                        "taxDutyAndSimilarPayments": 5713,
                        "payroll": 62309,
                        "socialSecurityCosts": 15783
                    },
                    "depreciation": {
                        "depreciationOfFixedAssets": 20642,
                        "amortisationOfFixedAssets": 0,
                        "depreciationAmortisationOfCurrentAssets": 0,
                        "provisionsForRisksAndChargesOfResults": 0
                    },
                    "otherCharge": {
                        "otherCharges": 6335,
                        "shareOfJointVentureTransferredToOtherPartner": 0,
                        "shareOfJointVentureTransferredFromOtherPartner": 0
                    },
                    "resultsFinancialIncome": {
                        "totalFinancialIncome": 0,
                        "shareFinancialIncome": 0,
                        "otherInvestmentIncomeAndCapitalisedReceivables": 0,
                        "otherInterestAndSimilarIncome": 0,
                        "releasedProvisions": 0,
                        "exchangeGains": 0,
                        "netIncomeFromDisposalOfInvestmentSecurities": 0
                    },
                    "financialCharge": {
                        "totalFinancialChargeTotal": 12007,
                        "financialReservesAndProvisions": 0,
                        "interestAndSimilarCharges": 12007,
                        "exchangeLosses": 0,
                        "netLossFromDisposalOfInvestmentSecurities": 0
                    },
                    "additionalFinancialCharge": {
                        "totalExtraordinaryIncome": 6514,
                        "extraordinaryOperatingIncome": 665,
                        "extraordinaryIncomeFromCapitalTransactions": 5849,
                        "releasedProvisionsCharges": 0
                    },
                    "extraordinaryCharge": {
                        "totalExtraordinaryCharges": 21010,
                        "extraordinaryOperatingCharges": 14887,
                        "extraordinaryChargesFromCapitalTransactions": 6123,
                        "extraordinaryReservesAndProvisions": 0
                    },
                    "references": {
                        "ofWhichEquipmentLeases": 0,
                        "ofWhichPropertyLeases": 0,
                        "ofWhichTransferredCharges": 0,
                        "ofWhichTradersOwnContributions": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsIncome": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsCharges": 0
                    }
                },
                "otherIncomes": {
                    "grossGrandTotalFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossResearchAndDevelopmentChargeFixed": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherBudgetItemFromIntangibleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherTangilbleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherFinancialAsset": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "situationAndMovementOfReserveForDepreciationGrandTotal": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "researchAndDevelopmentChargeReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "otherIntangibleAssetsReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalFixedAssedAmotisationReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netMovementsDuringPeriodAffectingChargeAllocatedOverSeveralPeriod": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netPremiumRefundOfObligations": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grandTotals": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "includesTotalAllocations": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "includesTotalWithdrawal": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "totalRegulatedProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalRiskAndChargeProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalProvisionForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "stateClaims": {
                        "stateClaimsGrossValue": 20496,
                        "stateClaimsWhenOneYearAtMost": 14828,
                        "stateClaimsWhenmoreThanOneYear": 5668
                    },
                    "stateOfLoans": {
                        "claimsRelatedToHoldingsGross": 0,
                        "claimsRelatedToShareholdingsOneYearAtMost": 0,
                        "grossOfLoans": 0,
                        "loansOneYearAtMost": 0,
                        "otherFinancialAssetsGross": 5668,
                        "otherFinancialAssetsOneYearAtMost": 0
                    },
                    "receivablesStatementOfAssets": {
                        "customersDoubtfulOrDisputed": 0,
                        "otherClaimsCustomer": 800,
                        "receivablesRepresentLoanedSecurities": 0,
                        "provisionForDepreciationPreviouslyEstablished": 0,
                        "personnelAndAssociatedAccounts": 0,
                        "socialSecurityAndOtherSocialOrganizations": 0,
                        "incomeTaxes": 0,
                        "valueAddedTax": 0,
                        "otherTaxesAndPaymentsAssimilatedOfReceivables": 0,
                        "stateAndOtherPublicMiscellaneous": 0,
                        "groupAndAssociates": 0,
                        "accountsReceivableIncOtherClaims": 13061
                    },
                    "stateDebt": {
                        "totalDebtGross": 438627,
                        "debtOneYearAtMost": 438627,
                        "debtMoreThanOneYearAndFiveYearsAtMost": 0,
                        "debtMoreThanFiveYears": 0
                    },
                    "details": {
                        "convertibleBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "borrowingDebtsToOneYearMaximumAtTheOrigin": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "borrowingDebtsToMoreThanOneYearAtTheOrigin": {
                            "gross": 143297,
                            "oneYearAtMost": 143297,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "financialLiabilities": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "suppliersAssociatedAccounts": {
                            "gross": 72881,
                            "oneYearAtMost": 72881,
                            "moreThanOneYearAndFiveYearsAtMost": 72881
                        },
                        "personnelAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherSocialOrganizations": {
                            "gross": 48649,
                            "oneYearAtMost": 48649,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "taxesOnProfits": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "vat": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "backedObligations": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherTaxesAssimilated": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "assetsAndLiabilitiesAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "groupsAndAssociates": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "otherLiabilities": {
                            "gross": 173799,
                            "oneYearAtMost": 173799,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "debtOfBorrowedSecurities": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "productsInAdvance": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        }
                    },
                    "referencesOthers": {
                        "loansMadeDuringThePeriod": 0,
                        "debtRepaidDuringThePeriod": 0
                    },
                    "commitments": {
                        "commitmentsLeasingFurniture": 0,
                        "commitmentsRealEstateLeasing": 0,
                        "effectsBroughtToTheDiscountAndUnmatured": 0
                    },
                    "otherChargesExternal": {
                        "subContracting": 0,
                        "rentalsRentalChargesAndCondominiums": 0,
                        "staffOutsideTheCompany": 0,
                        "remunerationIntermediariesAndFeesExcludingFees": 0,
                        "feesCommissionsAndBrokerage": 0,
                        "otherAccounts": 0,
                        "totalOtherPurchasesAndExternal": 0
                    },
                    "taxesAndFees": {
                        "businessTax": 0,
                        "otherTaxesAndPaymentsAssimilated": 0,
                        "totalTaxesAndFees": 0
                    },
                    "vat": {
                        "amountVatCollected": 0,
                        "totalVatOnGoodsAndServices": 0
                    },
                    "extraInformation": {
                        "averageNumberOfEmployees": 3,
                        "dividends": 0,
                        "prepaid": 966,
                        "groupsAndShareholders": 0
                    }
                },
                "ratios": {
                    "structureAndLiquidity": {
                        "fixedAssetFinancing": 0.43,
                        "globalDebt": 697,
                        "workingCapitalFundOverallNet": -268,
                        "financialIndependence": -71.21,
                        "solvability": -62.03,
                        "capacityDebtFutures": -117.19,
                        "coverageOfCurrentAssets": -511.89,
                        "generalLiquidity": 0.03,
                        "restrictedLiquidity": 0.07
                    },
                    "managementOrRotation": {
                        "needBackgroundInOperatingWorkingCapital": -296,
                        "treasury": 26,
                        "averageLengthOfCreditGrantedCoCustomers": 1,
                        "averageLengthOfCreditObtainedSuppliers": 196,
                        "inventoryTurnoverOfRawMaterials": 20
                    },
                    "profitabilityOfTheBusiness": {
                        "marginTrading": 0,
                        "profitabilityOfTheBusiness": 5.57,
                        "netprofit": -16.02,
                        "growthRateOfTurnover": -35.65,
                        "ratesIntegration": 40.96,
                        "rateLeasingFurniture": 0,
                        "workFactor": 84.21,
                        "weightInterests": 5.3
                    },
                    "returnOnCapital": {
                        "cashFlowFromTheOverallProfitability": -6.78,
                        "ratesOfEconomicProfitability": 19,
                        "financialProfitability": 21.6,
                        "returnOnInvestment": -35.74
                    },
                    "syntheticFinancialPerformanceIndicators": {
                        "conanHolderScore": -0.022,
                        "conanHolderSituation": 80
                    }
                },
                "sig": {
                    "turnover": 226415,
                    "saleOfGoods": 0,
                    "purchaseOfGoods": 0,
                    "stockOfGoodsVariation": 0,
                    "tradingMarginOfSalesOfGoods": 0,
                    "saleOfGoodsPercentage": 0,
                    "saleOfGoodsProduce": 226415,
                    "valueOfStockedProduction": 0,
                    "valueOfSelfConstructedAssets": 0,
                    "periodProductionOfSaleOfGoodsProduce": 226415,
                    "saleOfGoodsProducedPercentage": 100,
                    "tradingMargin": 0,
                    "periodProductionOfTradingMargin": 226415,
                    "purchaseOfawMaterials": 55586,
                    "differenceInStocksOfRawMaterials": 2029,
                    "variousExternalPurchasesAndCharges": 76061,
                    "addedValueOfTradingMargin": 92739,
                    "tradingMarginPercentage": 40.96,
                    "addedValue": 92739,
                    "opertingGrants": 3678,
                    "taxAndDutyAndSimilarPayments": 5713,
                    "personalCharges": 78092,
                    "grossOperatingSurplusOfAddedValue": 12612,
                    "grossOperatingSurplusDifference": 5.57,
                    "grossOperatingSurplus": 12612,
                    "changeInReleaseOfReservesAndProvisions": 4568,
                    "otherOperatingIncome": 22,
                    "depreciationOrAmmortisation": 20642,
                    "changesInOtherCharges": 6335,
                    "operatingResultOfGrossOperatingSurplus": -9775,
                    "operatingSurplusPercentage": -4.32,
                    "operatingResult": -9775,
                    "resultOfJointVentureTransferredFromOrToOtherPartners": 0,
                    "financialIncomeOfOperatingResult": 0,
                    "financialChargesOfOperatingResult": 12007,
                    "preTaxResultOfOperatingResult": -21782,
                    "operatingResultsPercentage": -9.62,
                    "extraodinaryIncome": 6514,
                    "extaordinaryCharges": 21010,
                    "extraordinaryResultOfExtraordinaryIncome": -14496,
                    "extraordinaryIncomePercentage": -6.4,
                    "preTaxResult": -21782,
                    "exceptionalIncomeResult": -14496,
                    "employeeProfitSharing": 0,
                    "taxOnProfit": 0,
                    "netResultOfPreTaxResult": -36278,
                    "preTaxResultPercentage": -16.02
                }
            },
            {
                "type": "LocalFinancialsFullCSFR",
                "yearEndDate": "2009-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 12,
                "assets": {
                    "grandTotalAssets": {
                        "grandTotalNet": 298124,
                        "grandTotalGross": 344641,
                        "grandTotalAmortisation": 46517
                    },
                    "capitalSubscribedNotCalled": {
                        "capitalSubscribed": 0,
                        "grossCapitalSubscribed": 0
                    },
                    "activeFixedAsset": {
                        "total": 260678,
                        "gross": 307195,
                        "amortisation": 46517
                    },
                    "activeIntangibleFixedAssets": {
                        "startupCost": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "researchAndDevelopmentExpenses": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "distributorshipsPatents": {
                            "total": 0,
                            "gross": 3460,
                            "amortisation": 3460
                        },
                        "goodwill": {
                            "total": 140200,
                            "gross": 140200,
                            "amortisation": 0
                        },
                        "otherIntangibleFixedAssets": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "prepaymentsAndDownpayments": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalIntangibleAsset": 140200
                    },
                    "tangilbleFixedAssets": {
                        "land": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "buildings": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "plant": {
                            "total": 29846,
                            "gross": 42768,
                            "amortisation": 12922
                        },
                        "otherTangibleFixedAssets": {
                            "total": 85385,
                            "gross": 115520,
                            "amortisation": 30135
                        },
                        "fixedAssetsInConstruction": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "advancesAndPaymentsOnAccount": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalTangibleAsset": 115231
                    },
                    "financialAssets": {
                        "associatesAtEquity": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherParticipations": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "intercompanyReceivables": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherInvestmentSecurities": {
                            "total": 15,
                            "gross": 15,
                            "amortisation": 0
                        },
                        "loans": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherFinancialAssets": {
                            "total": 5232,
                            "gross": 5232,
                            "amortisation": 0
                        },
                        "subTotalFinancialAssets": 5247
                    },
                    "activeAssets": {
                        "total": 37444,
                        "gross": 37444,
                        "amortisation": 0
                    },
                    "activeStocks": {
                        "rawMaterials": {
                            "total": 5050,
                            "gross": 5050,
                            "amortisation": 0
                        },
                        "workInProgressGoods": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "workInProgressServices": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "semiFinishedAndFinishedProducts": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "goodsForResale": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalStocks": 5050
                    },
                    "advancePaymentsToSupplier": {
                        "total": 0,
                        "gross": 0,
                        "amortisation": 0
                    },
                    "activeDebtors": {
                        "tradeAccountsReceivable": {
                            "total": 912,
                            "gross": 912,
                            "amortisation": 0
                        },
                        "otherDebtors": {
                            "total": 4791,
                            "gross": 4791,
                            "amortisation": 0
                        },
                        "capitalSubscribedAndCalledUp": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalDebtors": 5703
                    },
                    "activeDivers": {
                        "investmentSecurities": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "cashAndCashEquivalents": {
                            "total": 21660,
                            "gross": 21660,
                            "amortisation": 0
                        },
                        "subTotalDivers": 21660
                    },
                    "accountPrepaidExpenses": {
                        "total": 5031,
                        "gross": 5031,
                        "amortisation": 0
                    },
                    "equalizationAccounts": {
                        "multiPeriodCharges": 0,
                        "multiPeriodChargesGross": 0,
                        "premiumsOnRedemptionOfBonds": 0,
                        "premiumsOnRedemptionOfBondsGross": 0,
                        "currencyDifferentialGain": 0,
                        "currencyDifferentialGainGross": 0
                    },
                    "assetsReferences": {
                        "dueWithinOneYear": 0,
                        "dueAfterOneYear": 0
                    }
                },
                "liabilities": {
                    "grandTotal": 298123,
                    "shareholderEquity": {
                        "totalShareholdersEquity": -127467,
                        "equityAndShareholdersEquity": 7500,
                        "issueAndMergerPremiums": 0,
                        "revaluationDifferentials": 0,
                        "ofWhichEquityDiffeential": 0,
                        "legalReserve": 0,
                        "statutoryOrContractualReserve": 0,
                        "specialRegulatedReserves": 0,
                        "ofWhichSpecialReserveOfProvisions": 0,
                        "otherReservesOfLiabilities": 0,
                        "ofWhichReserveForBuyingOriginalsWorks": 0,
                        "profitsOrLossesBroughtForward": -91720,
                        "profitOrLossForThePeriod": -55790,
                        "investmentGrants": 12543,
                        "specialTaxAllowableReserves": 0
                    },
                    "otherCapitalResource": {
                        "totalOtherCapitalResources": 0,
                        "incomeFromParticipatingSecurities": 0,
                        "conditionalLoans": 0
                    },
                    "provisionsForRisksAndCharge": {
                        "totalProvisionsForRisksAndCharges": 0,
                        "riskProvisions": 0,
                        "reservesForCharges": 0
                    },
                    "liabilities": {
                        "totalLiabilities": 425589,
                        "convertibleDebentures": 0,
                        "otherDebentures": 0,
                        "bankLoansAndLiabilities": 163459,
                        "sundryLoansAndFinancialLiabilities": 71732,
                        "ofWhichParticipatingLoans": 0,
                        "advancePaymentsReceivedForCurrentOrders": 0,
                        "tradeAccountsPayables": 64612,
                        "taxAndSocialSecurityLiabilities": 71443,
                        "fixedAssetLiabilities": 0,
                        "otherDebts": 54343
                    },
                    "passiveAccountReferences": {
                        "ofWhichTaxAllowableReserve": 0,
                        "deferredIncomeAndLiabilities": 0,
                        "ofWhichCurrentBankFacilities": 0
                    },
                    "extraInformation": {
                        "taxAllowableReserve": 0,
                        "deferredIncomeLiabilities": 0,
                        "deferredBankIncome": 0,
                        "deferredIncome": 0,
                        "passiveTranslationLoss": 0
                    }
                },
                "profitAndLoss": {
                    "operatingResult": -37029,
                    "financialResult": -8688,
                    "resultsOfPreTaxNetOperatingIncome": -45717,
                    "extraordinaryResult": -10071,
                    "profitOrLoss": -55790,
                    "totalIncome": 370123,
                    "totalCharges": 425911,
                    "employeeProfitSharing": 0,
                    "taxOnProfits": 0,
                    "operatingIncome": {
                        "totalOperatingIncome": 363697,
                        "goodsForResaleTotal": 0,
                        "goodsForResaleFrance": 0,
                        "goodsForResaleExport": 0,
                        "goodsProducedTotal": 316713,
                        "goodsProducedFrance": 316713,
                        "goodsProducedExport": 0,
                        "saleOfServicesTotal": 35160,
                        "saleOfServicesFrance": 35160,
                        "saleOfServicesExport": 0,
                        "netTurnoverTotal": 351873,
                        "netTurnoverFrance": 351873,
                        "netTurnoverExport": 0,
                        "stockedProduction": 0,
                        "selfConstructedAssets": 0,
                        "operatingGrants": 5816,
                        "releaseOfReservesAndProvisions": 5999,
                        "otherIncome": 9
                    },
                    "totalOperatingCharge": {
                        "totalOperatingCharges": 400726,
                        "purchaseOfGoodsForResale": 552,
                        "changeInStocksOfGoodsForResale": 0,
                        "purchaseOfRawMaterials": 155486,
                        "changeInStocksOfRawMaterials": 5200,
                        "otherExternalPurchasesAndCharges": 91805,
                        "taxDutyAndSimilarPayments": 8766,
                        "payroll": 84907,
                        "socialSecurityCosts": 24335
                    },
                    "depreciation": {
                        "depreciationOfFixedAssets": 23336,
                        "amortisationOfFixedAssets": 0,
                        "depreciationAmortisationOfCurrentAssets": 0,
                        "provisionsForRisksAndChargesOfResults": 0
                    },
                    "otherCharge": {
                        "otherCharges": 6339,
                        "shareOfJointVentureTransferredToOtherPartner": 0,
                        "shareOfJointVentureTransferredFromOtherPartner": 0
                    },
                    "resultsFinancialIncome": {
                        "totalFinancialIncome": 0,
                        "shareFinancialIncome": 0,
                        "otherInvestmentIncomeAndCapitalisedReceivables": 0,
                        "otherInterestAndSimilarIncome": 0,
                        "releasedProvisions": 0,
                        "exchangeGains": 0,
                        "netIncomeFromDisposalOfInvestmentSecurities": 0
                    },
                    "financialCharge": {
                        "totalFinancialChargeTotal": 8688,
                        "financialReservesAndProvisions": 0,
                        "interestAndSimilarCharges": 8688,
                        "exchangeLosses": 0,
                        "netLossFromDisposalOfInvestmentSecurities": 0
                    },
                    "additionalFinancialCharge": {
                        "totalExtraordinaryIncome": 6426,
                        "extraordinaryOperatingIncome": 2246,
                        "extraordinaryIncomeFromCapitalTransactions": 4180,
                        "releasedProvisionsCharges": 0
                    },
                    "extraordinaryCharge": {
                        "totalExtraordinaryCharges": 16497,
                        "extraordinaryOperatingCharges": 16497,
                        "extraordinaryChargesFromCapitalTransactions": 0,
                        "extraordinaryReservesAndProvisions": 0
                    },
                    "references": {
                        "ofWhichEquipmentLeases": 0,
                        "ofWhichPropertyLeases": 0,
                        "ofWhichTransferredCharges": 5999,
                        "ofWhichTradersOwnContributions": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsIncome": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsCharges": 6230
                    }
                },
                "otherIncomes": {
                    "grossGrandTotalFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossResearchAndDevelopmentChargeFixed": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherBudgetItemFromIntangibleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherTangilbleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherFinancialAsset": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "situationAndMovementOfReserveForDepreciationGrandTotal": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "researchAndDevelopmentChargeReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "otherIntangibleAssetsReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalFixedAssedAmotisationReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netMovementsDuringPeriodAffectingChargeAllocatedOverSeveralPeriod": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netPremiumRefundOfObligations": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grandTotals": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "includesTotalAllocations": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "includesTotalWithdrawal": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "totalRegulatedProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalRiskAndChargeProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalProvisionForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "stateClaims": {
                        "stateClaimsGrossValue": 15967,
                        "stateClaimsWhenOneYearAtMost": 10735,
                        "stateClaimsWhenmoreThanOneYear": 5232
                    },
                    "stateOfLoans": {
                        "claimsRelatedToHoldingsGross": 0,
                        "claimsRelatedToShareholdingsOneYearAtMost": 0,
                        "grossOfLoans": 0,
                        "loansOneYearAtMost": 0,
                        "otherFinancialAssetsGross": 5232,
                        "otherFinancialAssetsOneYearAtMost": 0
                    },
                    "receivablesStatementOfAssets": {
                        "customersDoubtfulOrDisputed": 0,
                        "otherClaimsCustomer": 0,
                        "receivablesRepresentLoanedSecurities": 0,
                        "provisionForDepreciationPreviouslyEstablished": 0,
                        "personnelAndAssociatedAccounts": 0,
                        "socialSecurityAndOtherSocialOrganizations": 0,
                        "incomeTaxes": 0,
                        "valueAddedTax": 0,
                        "otherTaxesAndPaymentsAssimilatedOfReceivables": 0,
                        "stateAndOtherPublicMiscellaneous": 0,
                        "groupAndAssociates": 0,
                        "accountsReceivableIncOtherClaims": 10735
                    },
                    "stateDebt": {
                        "totalDebtGross": 425591,
                        "debtOneYearAtMost": 296501,
                        "debtMoreThanOneYearAndFiveYearsAtMost": 129090,
                        "debtMoreThanFiveYears": 0
                    },
                    "details": {
                        "convertibleBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "borrowingDebtsToOneYearMaximumAtTheOrigin": {
                            "gross": 163459,
                            "oneYearAtMost": 34369,
                            "moreThanOneYearAndFiveYearsAtMost": 129090
                        },
                        "borrowingDebtsToMoreThanOneYearAtTheOrigin": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "financialLiabilities": {
                            "gross": 71732,
                            "oneYearAtMost": 71732,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "suppliersAssociatedAccounts": {
                            "gross": 64612,
                            "oneYearAtMost": 64612,
                            "moreThanOneYearAndFiveYearsAtMost": 64612
                        },
                        "personnelAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherSocialOrganizations": {
                            "gross": 71443,
                            "oneYearAtMost": 71443,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "taxesOnProfits": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "vat": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "backedObligations": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherTaxesAssimilated": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "assetsAndLiabilitiesAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "groupsAndAssociates": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "otherLiabilities": {
                            "gross": 54343,
                            "oneYearAtMost": 54343,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "debtOfBorrowedSecurities": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "productsInAdvance": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        }
                    },
                    "referencesOthers": {
                        "loansMadeDuringThePeriod": 0,
                        "debtRepaidDuringThePeriod": 0
                    },
                    "commitments": {
                        "commitmentsLeasingFurniture": 0,
                        "commitmentsRealEstateLeasing": 0,
                        "effectsBroughtToTheDiscountAndUnmatured": 0
                    },
                    "otherChargesExternal": {
                        "subContracting": 0,
                        "rentalsRentalChargesAndCondominiums": 0,
                        "staffOutsideTheCompany": 0,
                        "remunerationIntermediariesAndFeesExcludingFees": 0,
                        "feesCommissionsAndBrokerage": 0,
                        "otherAccounts": 0,
                        "totalOtherPurchasesAndExternal": 0
                    },
                    "taxesAndFees": {
                        "businessTax": 0,
                        "otherTaxesAndPaymentsAssimilated": 0,
                        "totalTaxesAndFees": 0
                    },
                    "vat": {
                        "amountVatCollected": 0,
                        "totalVatOnGoodsAndServices": 0
                    },
                    "extraInformation": {
                        "averageNumberOfEmployees": 0,
                        "dividends": 0,
                        "prepaid": 0
                    }
                },
                "ratios": {
                    "structureAndLiquidity": {
                        "fixedAssetFinancing": 0.5,
                        "globalDebt": 435,
                        "workingCapitalFundOverallNet": -156,
                        "financialIndependence": -54.2,
                        "solvability": -42.76,
                        "capacityDebtFutures": -43.57,
                        "coverageOfCurrentAssets": -471.89,
                        "generalLiquidity": 0.04,
                        "restrictedLiquidity": 0.11
                    },
                    "managementOrRotation": {
                        "needBackgroundInOperatingWorkingCapital": -184,
                        "treasury": 22,
                        "inventoryTurnoverOfGoods": 0,
                        "averageLengthOfCreditGrantedCoCustomers": 1,
                        "averageLengthOfCreditObtainedSuppliers": 92,
                        "inventoryTurnoverOfRawMaterials": 12
                    },
                    "profitabilityOfTheBusiness": {
                        "marginTrading": -0.16,
                        "profitabilityOfTheBusiness": -3.8,
                        "netprofit": -15.86,
                        "growthRateOfTurnover": -30.32,
                        "ratesIntegration": 28.09,
                        "rateLeasingFurniture": 0,
                        "workFactor": 110.54,
                        "weightInterests": 2.47
                    },
                    "returnOnCapital": {
                        "cashFlowFromTheOverallProfitability": -10.41,
                        "ratesOfEconomicProfitability": -12,
                        "financialProfitability": 43.77,
                        "returnOnInvestment": -43.72
                    },
                    "syntheticFinancialPerformanceIndicators": {
                        "conanHolderScore": -0.039,
                        "conanHolderSituation": 80
                    }
                },
                "sig": {
                    "turnover": 351873,
                    "saleOfGoods": 0,
                    "purchaseOfGoods": 552,
                    "stockOfGoodsVariation": 0,
                    "tradingMarginOfSalesOfGoods": -552,
                    "saleOfGoodsPercentage": -0.16,
                    "saleOfGoodsProduce": 351873,
                    "valueOfStockedProduction": 0,
                    "valueOfSelfConstructedAssets": 0,
                    "periodProductionOfSaleOfGoodsProduce": 351873,
                    "saleOfGoodsProducedPercentage": 100,
                    "tradingMargin": -552,
                    "periodProductionOfTradingMargin": 351873,
                    "purchaseOfawMaterials": 155486,
                    "differenceInStocksOfRawMaterials": 5200,
                    "variousExternalPurchasesAndCharges": 91805,
                    "addedValueOfTradingMargin": 98830,
                    "tradingMarginPercentage": 28.09,
                    "addedValue": 98830,
                    "opertingGrants": 5816,
                    "taxAndDutyAndSimilarPayments": 8766,
                    "personalCharges": 109242,
                    "grossOperatingSurplusOfAddedValue": -13362,
                    "grossOperatingSurplusDifference": -3.8,
                    "grossOperatingSurplus": -13362,
                    "changeInReleaseOfReservesAndProvisions": 5999,
                    "otherOperatingIncome": 9,
                    "depreciationOrAmmortisation": 23336,
                    "changesInOtherCharges": 6339,
                    "operatingResultOfGrossOperatingSurplus": -37029,
                    "operatingSurplusPercentage": -10.52,
                    "operatingResult": -37029,
                    "resultOfJointVentureTransferredFromOrToOtherPartners": 0,
                    "financialIncomeOfOperatingResult": 0,
                    "financialChargesOfOperatingResult": 8688,
                    "preTaxResultOfOperatingResult": -45717,
                    "operatingResultsPercentage": -12.99,
                    "extraodinaryIncome": 6426,
                    "extaordinaryCharges": 16497,
                    "extraordinaryResultOfExtraordinaryIncome": -10071,
                    "extraordinaryIncomePercentage": -2.86,
                    "preTaxResult": -45717,
                    "exceptionalIncomeResult": -10071,
                    "employeeProfitSharing": 0,
                    "taxOnProfit": 0,
                    "netResultOfPreTaxResult": -55788,
                    "preTaxResultPercentage": -15.85
                }
            },
            {
                "type": "LocalFinancialsFullCSFR",
                "yearEndDate": "2008-09-30T00:00:00Z",
                "currency": "EUR",
                "consolidatedAccounts": False,
                "month": 18,
                "assets": {
                    "grandTotalAssets": {
                        "grandTotalNet": 316027,
                        "grandTotalGross": 339208,
                        "grandTotalAmortisation": 23181
                    },
                    "capitalSubscribedNotCalled": {
                        "capitalSubscribed": 0,
                        "grossCapitalSubscribed": 0
                    },
                    "activeFixedAsset": {
                        "total": 280264,
                        "gross": 303443,
                        "amortisation": 23179
                    },
                    "activeIntangibleFixedAssets": {
                        "startupCost": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "researchAndDevelopmentExpenses": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "distributorshipsPatents": {
                            "total": 2183,
                            "gross": 3460,
                            "amortisation": 1277
                        },
                        "goodwill": {
                            "total": 140200,
                            "gross": 140200,
                            "amortisation": 0
                        },
                        "otherIntangibleFixedAssets": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "prepaymentsAndDownpayments": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalIntangibleAsset": 142383
                    },
                    "tangilbleFixedAssets": {
                        "land": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "buildings": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "plant": {
                            "total": 32552,
                            "gross": 39016,
                            "amortisation": 6464
                        },
                        "otherTangibleFixedAssets": {
                            "total": 100082,
                            "gross": 115520,
                            "amortisation": 15438
                        },
                        "fixedAssetsInConstruction": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "advancesAndPaymentsOnAccount": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalTangibleAsset": 132634
                    },
                    "financialAssets": {
                        "associatesAtEquity": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherParticipations": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "intercompanyReceivables": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherInvestmentSecurities": {
                            "total": 15,
                            "gross": 15,
                            "amortisation": 0
                        },
                        "loans": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "otherFinancialAssets": {
                            "total": 5232,
                            "gross": 5232,
                            "amortisation": 0
                        },
                        "subTotalFinancialAssets": 5247
                    },
                    "activeAssets": {
                        "total": 35763,
                        "gross": 35763,
                        "amortisation": 0
                    },
                    "activeStocks": {
                        "rawMaterials": {
                            "total": 10250,
                            "gross": 10250,
                            "amortisation": 0
                        },
                        "workInProgressGoods": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "workInProgressServices": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "semiFinishedAndFinishedProducts": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "goodsForResale": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalStocks": 10250
                    },
                    "advancePaymentsToSupplier": {
                        "total": 0,
                        "gross": 0,
                        "amortisation": 0
                    },
                    "activeDebtors": {
                        "tradeAccountsReceivable": {
                            "total": 4823,
                            "gross": 4823,
                            "amortisation": 0
                        },
                        "otherDebtors": {
                            "total": 9781,
                            "gross": 9781,
                            "amortisation": 0
                        },
                        "capitalSubscribedAndCalledUp": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "subTotalDebtors": 14604
                    },
                    "activeDivers": {
                        "investmentSecurities": {
                            "total": 0,
                            "gross": 0,
                            "amortisation": 0
                        },
                        "cashAndCashEquivalents": {
                            "total": 8897,
                            "gross": 8897,
                            "amortisation": 0
                        },
                        "subTotalDivers": 8897
                    },
                    "accountPrepaidExpenses": {
                        "total": 2012,
                        "gross": 2012,
                        "amortisation": 0
                    },
                    "equalizationAccounts": {
                        "multiPeriodCharges": 0,
                        "multiPeriodChargesGross": 0,
                        "premiumsOnRedemptionOfBonds": 0,
                        "premiumsOnRedemptionOfBondsGross": 0,
                        "currencyDifferentialGain": 0,
                        "currencyDifferentialGainGross": 0
                    },
                    "assetsReferences": {
                        "dueWithinOneYear": 0,
                        "dueAfterOneYear": 0
                    }
                },
                "liabilities": {
                    "grandTotal": 316026,
                    "shareholderEquity": {
                        "totalShareholdersEquity": -67497,
                        "equityAndShareholdersEquity": 7500,
                        "issueAndMergerPremiums": 0,
                        "revaluationDifferentials": 0,
                        "ofWhichEquityDiffeential": 0,
                        "legalReserve": 0,
                        "statutoryOrContractualReserve": 0,
                        "specialRegulatedReserves": 0,
                        "ofWhichSpecialReserveOfProvisions": 0,
                        "otherReservesOfLiabilities": 0,
                        "ofWhichReserveForBuyingOriginalsWorks": 0,
                        "profitsOrLossesBroughtForward": 0,
                        "profitOrLossForThePeriod": -91720,
                        "investmentGrants": 16723,
                        "specialTaxAllowableReserves": 0
                    },
                    "otherCapitalResource": {
                        "totalOtherCapitalResources": 0,
                        "incomeFromParticipatingSecurities": 0,
                        "conditionalLoans": 0
                    },
                    "provisionsForRisksAndCharge": {
                        "totalProvisionsForRisksAndCharges": 0,
                        "riskProvisions": 0,
                        "reservesForCharges": 0
                    },
                    "liabilities": {
                        "totalLiabilities": 383522,
                        "convertibleDebentures": 0,
                        "otherDebentures": 0,
                        "bankLoansAndLiabilities": 207593,
                        "sundryLoansAndFinancialLiabilities": 62860,
                        "ofWhichParticipatingLoans": 0,
                        "advancePaymentsReceivedForCurrentOrders": 0,
                        "tradeAccountsPayables": 58353,
                        "taxAndSocialSecurityLiabilities": 35156,
                        "fixedAssetLiabilities": 0,
                        "otherDebts": 19560
                    },
                    "passiveAccountReferences": {
                        "ofWhichTaxAllowableReserve": 0,
                        "deferredIncomeAndLiabilities": 0,
                        "ofWhichCurrentBankFacilities": 0
                    },
                    "extraInformation": {
                        "taxAllowableReserve": 0,
                        "deferredIncomeLiabilities": 0,
                        "deferredBankIncome": 0,
                        "deferredIncome": 0,
                        "passiveTranslationLoss": 0
                    }
                },
                "profitAndLoss": {
                    "operatingResult": -79541,
                    "financialResult": -14950,
                    "resultsOfPreTaxNetOperatingIncome": -94491,
                    "extraordinaryResult": 2773,
                    "profitOrLoss": -91720,
                    "totalIncome": 558883,
                    "totalCharges": 650601,
                    "employeeProfitSharing": 0,
                    "taxOnProfits": 0,
                    "operatingIncome": {
                        "totalOperatingIncome": 545702,
                        "goodsForResaleTotal": 0,
                        "goodsForResaleFrance": 0,
                        "goodsForResaleExport": 0,
                        "goodsProducedTotal": 451112,
                        "goodsProducedFrance": 451112,
                        "goodsProducedExport": 0,
                        "saleOfServicesTotal": 53875,
                        "saleOfServicesFrance": 53875,
                        "saleOfServicesExport": 0,
                        "netTurnoverTotal": 504987,
                        "netTurnoverFrance": 504987,
                        "netTurnoverExport": 0,
                        "stockedProduction": 0,
                        "selfConstructedAssets": 17845,
                        "operatingGrants": 8997,
                        "releaseOfReservesAndProvisions": 13868,
                        "otherIncome": 5
                    },
                    "totalOperatingCharge": {
                        "totalOperatingCharges": 625243,
                        "purchaseOfGoodsForResale": 762,
                        "changeInStocksOfGoodsForResale": 0,
                        "purchaseOfRawMaterials": 262919,
                        "changeInStocksOfRawMaterials": -10250,
                        "otherExternalPurchasesAndCharges": 151335,
                        "taxDutyAndSimilarPayments": 12061,
                        "payroll": 145335,
                        "socialSecurityCosts": 36733
                    },
                    "depreciation": {
                        "depreciationOfFixedAssets": 23183,
                        "amortisationOfFixedAssets": 0,
                        "depreciationAmortisationOfCurrentAssets": 0,
                        "provisionsForRisksAndChargesOfResults": 0
                    },
                    "otherCharge": {
                        "otherCharges": 3165,
                        "shareOfJointVentureTransferredToOtherPartner": 0,
                        "shareOfJointVentureTransferredFromOtherPartner": 0
                    },
                    "resultsFinancialIncome": {
                        "totalFinancialIncome": 0,
                        "shareFinancialIncome": 0,
                        "otherInvestmentIncomeAndCapitalisedReceivables": 0,
                        "otherInterestAndSimilarIncome": 0,
                        "releasedProvisions": 0,
                        "exchangeGains": 0,
                        "netIncomeFromDisposalOfInvestmentSecurities": 0
                    },
                    "financialCharge": {
                        "totalFinancialChargeTotal": 14950,
                        "financialReservesAndProvisions": 0,
                        "interestAndSimilarCharges": 14950,
                        "exchangeLosses": 0,
                        "netLossFromDisposalOfInvestmentSecurities": 0
                    },
                    "additionalFinancialCharge": {
                        "totalExtraordinaryIncome": 13181,
                        "extraordinaryOperatingIncome": 0,
                        "extraordinaryIncomeFromCapitalTransactions": 13181,
                        "releasedProvisionsCharges": 0
                    },
                    "extraordinaryCharge": {
                        "totalExtraordinaryCharges": 10408,
                        "extraordinaryOperatingCharges": 1410,
                        "extraordinaryChargesFromCapitalTransactions": 8998,
                        "extraordinaryReservesAndProvisions": 0
                    },
                    "references": {
                        "ofWhichEquipmentLeases": 0,
                        "ofWhichPropertyLeases": 0,
                        "ofWhichTransferredCharges": 13868,
                        "ofWhichTradersOwnContributions": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsIncome": 0,
                        "ofWhichRoyaltiesOnLicencesAndPatentsCharges": 3067
                    }
                },
                "otherIncomes": {
                    "grossGrandTotalFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossResearchAndDevelopmentChargeFixed": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherBudgetItemFromIntangibleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherTangilbleFixedAssets": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grossOtherFinancialAsset": {
                        "valueAtBeginOfPeriod": 0,
                        "increasesDueToRevaluation": 0,
                        "increasesOfAcquisitionsCreationsContributions": 0,
                        "decreasesByBudgetItemTransfer": 0,
                        "decreasesByTransfers": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "situationAndMovementOfReserveForDepreciationGrandTotal": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "researchAndDevelopmentChargeReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "otherIntangibleAssetsReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalFixedAssedAmotisationReserveForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netMovementsDuringPeriodAffectingChargeAllocatedOverSeveralPeriod": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "netPremiumRefundOfObligations": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "grandTotals": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "includesTotalAllocations": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "includesTotalWithdrawal": {
                        "operating": 0,
                        "financial": 0,
                        "exceptional": 0
                    },
                    "totalRegulatedProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalRiskAndChargeProvisions": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "totalProvisionForDepreciation": {
                        "valueAtBeginOfPeriod": 0,
                        "increases": 0,
                        "decreases": 0,
                        "valueAtEndOfPeriod": 0
                    },
                    "stateClaims": {
                        "stateClaimsGrossValue": 21848,
                        "stateClaimsWhenOneYearAtMost": 16616,
                        "stateClaimsWhenmoreThanOneYear": 5232
                    },
                    "stateOfLoans": {
                        "claimsRelatedToHoldingsGross": 0,
                        "claimsRelatedToShareholdingsOneYearAtMost": 0,
                        "grossOfLoans": 0,
                        "loansOneYearAtMost": 0,
                        "otherFinancialAssetsGross": 5232,
                        "otherFinancialAssetsOneYearAtMost": 0
                    },
                    "receivablesStatementOfAssets": {
                        "customersDoubtfulOrDisputed": 0,
                        "otherClaimsCustomer": 0,
                        "receivablesRepresentLoanedSecurities": 0,
                        "provisionForDepreciationPreviouslyEstablished": 0,
                        "personnelAndAssociatedAccounts": 0,
                        "socialSecurityAndOtherSocialOrganizations": 0,
                        "incomeTaxes": 0,
                        "valueAddedTax": 0,
                        "otherTaxesAndPaymentsAssimilatedOfReceivables": 0,
                        "stateAndOtherPublicMiscellaneous": 0,
                        "groupAndAssociates": 0,
                        "accountsReceivableIncOtherClaims": 16616
                    },
                    "stateDebt": {
                        "totalDebtGross": 383524,
                        "debtOneYearAtMost": 209371,
                        "debtMoreThanOneYearAndFiveYearsAtMost": 145478,
                        "debtMoreThanFiveYears": 28675
                    },
                    "details": {
                        "convertibleBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherBonds": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "borrowingDebtsToOneYearMaximumAtTheOrigin": {
                            "gross": 207593,
                            "oneYearAtMost": 33440,
                            "moreThanOneYearAndFiveYearsAtMost": 145478
                        },
                        "borrowingDebtsToMoreThanOneYearAtTheOrigin": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "financialLiabilities": {
                            "gross": 62860,
                            "oneYearAtMost": 62860,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "suppliersAssociatedAccounts": {
                            "gross": 58353,
                            "oneYearAtMost": 58353,
                            "moreThanOneYearAndFiveYearsAtMost": 58353
                        },
                        "personnelAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherSocialOrganizations": {
                            "gross": 35156,
                            "oneYearAtMost": 35156,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "taxesOnProfits": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "vat": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "backedObligations": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "otherTaxesAssimilated": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "assetsAndLiabilitiesAssociatedAccounts": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "groupsAndAssociates": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0,
                            "moreThanFiveYears": 0
                        },
                        "otherLiabilities": {
                            "gross": 19560,
                            "oneYearAtMost": 19560,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "debtOfBorrowedSecurities": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        },
                        "productsInAdvance": {
                            "gross": 0,
                            "oneYearAtMost": 0,
                            "moreThanOneYearAndFiveYearsAtMost": 0
                        }
                    },
                    "referencesOthers": {
                        "loansMadeDuringThePeriod": 0,
                        "debtRepaidDuringThePeriod": 0
                    },
                    "commitments": {
                        "commitmentsLeasingFurniture": 0,
                        "commitmentsRealEstateLeasing": 0,
                        "effectsBroughtToTheDiscountAndUnmatured": 0
                    },
                    "otherChargesExternal": {
                        "subContracting": 0,
                        "rentalsRentalChargesAndCondominiums": 0,
                        "staffOutsideTheCompany": 0,
                        "remunerationIntermediariesAndFeesExcludingFees": 0,
                        "feesCommissionsAndBrokerage": 0,
                        "otherAccounts": 0,
                        "totalOtherPurchasesAndExternal": 0
                    },
                    "taxesAndFees": {
                        "businessTax": 0,
                        "otherTaxesAndPaymentsAssimilated": 0,
                        "totalTaxesAndFees": 0
                    },
                    "vat": {
                        "amountVatCollected": 0,
                        "totalVatOnGoodsAndServices": 0
                    },
                    "extraInformation": {
                        "averageNumberOfEmployees": 0,
                        "dividends": 0,
                        "prepaid": 0
                    }
                },
                "ratios": {
                    "structureAndLiquidity": {
                        "fixedAssetFinancing": 0.75,
                        "globalDebt": 410,
                        "workingCapitalFundOverallNet": -83,
                        "financialIndependence": -24.96,
                        "solvability": -21.36,
                        "capacityDebtFutures": -20.81,
                        "coverageOfCurrentAssets": -229.05,
                        "generalLiquidity": 0.08,
                        "restrictedLiquidity": 0.12
                    },
                    "managementOrRotation": {
                        "needBackgroundInOperatingWorkingCapital": -94,
                        "treasury": 10,
                        "inventoryTurnoverOfGoods": 0,
                        "averageLengthOfCreditGrantedCoCustomers": 3,
                        "averageLengthOfCreditObtainedSuppliers": 52,
                        "inventoryTurnoverOfRawMaterials": 14
                    },
                    "profitabilityOfTheBusiness": {
                        "marginTrading": -0.15,
                        "profitabilityOfTheBusiness": -13.28,
                        "netprofit": -18.16,
                        "ratesIntegration": 23.38,
                        "rateLeasingFurniture": 0,
                        "workFactor": 154.21,
                        "weightInterests": 2.96
                    },
                    "returnOnCapital": {
                        "cashFlowFromTheOverallProfitability": -14.4,
                        "ratesOfEconomicProfitability": -33,
                        "financialProfitability": 135.89,
                        "returnOnInvestment": -37.83
                    },
                    "syntheticFinancialPerformanceIndicators": {
                        "conanHolderScore": -0.055,
                        "conanHolderSituation": 90
                    }
                },
                "sig": {
                    "turnover": 504987,
                    "saleOfGoods": 0,
                    "purchaseOfGoods": 762,
                    "stockOfGoodsVariation": 0,
                    "tradingMarginOfSalesOfGoods": -762,
                    "saleOfGoodsPercentage": -0.15,
                    "saleOfGoodsProduce": 504987,
                    "valueOfStockedProduction": 0,
                    "valueOfSelfConstructedAssets": 17845,
                    "periodProductionOfSaleOfGoodsProduce": 522832,
                    "saleOfGoodsProducedPercentage": 103.53,
                    "tradingMargin": -762,
                    "periodProductionOfTradingMargin": 522832,
                    "purchaseOfawMaterials": 262919,
                    "differenceInStocksOfRawMaterials": -10250,
                    "variousExternalPurchasesAndCharges": 151335,
                    "addedValueOfTradingMargin": 118066,
                    "tradingMarginPercentage": 23.38,
                    "addedValue": 118066,
                    "opertingGrants": 8997,
                    "taxAndDutyAndSimilarPayments": 12061,
                    "personalCharges": 182068,
                    "grossOperatingSurplusOfAddedValue": -67066,
                    "grossOperatingSurplusDifference": -13.28,
                    "grossOperatingSurplus": -67066,
                    "changeInReleaseOfReservesAndProvisions": 13868,
                    "otherOperatingIncome": 5,
                    "depreciationOrAmmortisation": 23183,
                    "changesInOtherCharges": 3165,
                    "operatingResultOfGrossOperatingSurplus": -79541,
                    "operatingSurplusPercentage": -15.75,
                    "operatingResult": -79541,
                    "resultOfJointVentureTransferredFromOrToOtherPartners": 0,
                    "financialIncomeOfOperatingResult": 0,
                    "financialChargesOfOperatingResult": 14950,
                    "preTaxResultOfOperatingResult": -94491,
                    "operatingResultsPercentage": -18.71,
                    "extraodinaryIncome": 13181,
                    "extaordinaryCharges": 10408,
                    "extraordinaryResultOfExtraordinaryIncome": 2773,
                    "extraordinaryIncomePercentage": 0.55,
                    "preTaxResult": -94491,
                    "exceptionalIncomeResult": 2773,
                    "employeeProfitSharing": 0,
                    "taxOnProfit": 0,
                    "netResultOfPreTaxResult": -91718,
                    "preTaxResultPercentage": -18.16
                }
            }
        ],
        "paymentData": {
            "industryDbt": "6",
            "paymentTrend": "TrendNotAvailable",
            "averageMonthlyBalance": "0",
            "balanceP1": "0",
            "balanceP2": "0",
            "balanceP3": "0",
            "balanceP4": "0",
            "balanceWithinTerms": "0",
            "recentHighBalance": "0",
            "totalTradeLines": "0",
            "totalTradeLinesOutstanding": "0"
        },
        "negativeInformation": {
            "judgements": [
                {
                    "effectiveDate": "2014-09-26T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "CI",
                        "value": "Closure for Insufficient Assets"
                    }
                },
                {
                    "effectiveDate": "2014-09-17T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "CI",
                        "value": "Closure for Insufficient Assets"
                    },
                    "court": "Orléans",
                    "details": "Jugement de clôture Jugement de clôture pour insuffisance d'actif Jugement prononçant la clôture de la procédure de liquidation judiciaire pour insuffisance d'actif."
                },
                {
                    "effectiveDate": "2014-02-27T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "CRE",
                        "value": "Rulings linked to debts"
                    },
                    "court": "Orléans",
                    "details": "Avis de dépôt Dépôt de l'état des créances et du projet de répartition L'état des créances complété par le projet de répartition prévu par l'article L 644-4 du code de commerce est déposé au greffe. Tout intéressé peut contester ledit état devant le juge-commissaire dans un délai d'un mois à compter de la présente publication."
                },
                {
                    "effectiveDate": "2013-03-27T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "LJ",
                        "value": "Involuntary Liquidation"
                    },
                    "court": "Orléans",
                    "details": "Extrait de jugement Jugement prononçant la résolution du plan de redressement et la liquidation judiciaire Jugement prononçant la résolution du plan de redressement et la liquidation judiciaire, date de cessation des paiements le 30 Septembre 2012, désignant liquidateur Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations de créances sont à déposer auprès du liquidateur dans le délai de deux mois à compter de la présente publication à l'exception des créanciers admis au plan qui en sont dispensés."
                },
                {
                    "effectiveDate": "2012-10-24T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "CRE",
                        "value": "Rulings linked to debts"
                    },
                    "court": "Orléans",
                    "details": "Avis de dépôt Dépôt de l'état des créances L'état des créances est déposé au greffe où tout intéressé peut présenter réclamation devant le juge-commissaire dans le délai d'un mois à compter de la présente publication."
                },
                {
                    "effectiveDate": "2012-09-26T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "PCR",
                        "value": "Recovery Plan"
                    },
                    "court": "Orléans",
                    "details": "Extrait de jugement Jugement de plan de redressement Jugement arrêtant le plan de redressement, durée du plan 120 mois nomme Commissaire à l'exécution du plan Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans ."
                },
                {
                    "effectiveDate": "2011-11-17T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "RJ",
                        "value": "Receivership"
                    },
                    "court": "ORLEANS",
                    "details": "JUGEMENT DE REDRESSEMENT JUDICIAIRE  : Suivant jugement en date du 16/11/2011, le Tribunal de Commerce d'Orléans a ouvert une procédure de redressement judiciaire a l'égard de la société : SCORE Mandataire judiciaire : Maître Christian SAULNIER 6 Bis, Rue des Anglaises 45000 ORLEANS Date de cessation des paiements : 16/06/2010 - DATE D'EFFET : 16/11/2011"
                },
                {
                    "effectiveDate": "2011-11-16T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "RJ",
                        "value": "Receivership"
                    },
                    "court": "Orléans",
                    "details": "Jugement d'ouverture Jugement d'ouverture d'une procédure de redressement judiciaire Jugement prononçant l'ouverture d'une procédure de redressement judiciaire, date de cessation des paiements le 16 Juin 2010 désignant mandataire judiciaire Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations des créances sont à déposer au mandataire judiciaire dans les deux mois à compter de la présente publication."
                },
                {
                    "effectiveDate": "2011-11-16T00:00:00Z",
                    "typeOfJudgement": {
                        "code": "RJ",
                        "value": "Receivership"
                    },
                    "court": "Tribunal de Commerce d'ORLEANS",
                    "liquidators": [
                        "MAîTRE CHRISTIAN SAULNIER 6 BIS"
                    ]
                }
            ],
            "collectiveProcedures": {
                "courts": [
                    {
                        "judgment": "Receivership",
                        "court": "ORLEANS",
                        "details": "JUGEMENT DE REDRESSEMENT JUDICIAIRE  : Suivant jugement en date du 16/11/2011, le Tribunal de Commerce d'Orléans a ouvert une procédure de redressement judiciaire a l'égard de la société : SCORE Mandataire judiciaire : Maître Christian SAULNIER 6 Bis, Rue des Anglaises 45000 ORLEANS Date de cessation des paiements : 16/06/2010 - DATE D'EFFET : 16/11/2011",
                        "effectiveDate": "2011-11-17T00:00:00Z"
                    }
                ],
                "rncs": [
                    {
                        "judgment": "Closure for Insufficient Assets",
                        "effectiveDate": "2014-09-26T00:00:00Z"
                    }
                ],
                "bodacc": [
                    {
                        "judgment": "Closure for Insufficient Assets",
                        "court": "Orléans",
                        "details": "Jugement de clôtureJugement de clôture pour insuffisance d'actifJugement prononçant la clôture de la procédure de liquidation judiciaire pour insuffisance d'actif.",
                        "effectiveDate": "2014-09-17T00:00:00Z",
                        "publicationDate": "2014-10-05T00:00:00Z"
                    },
                    {
                        "judgment": "Rulings linked to debts",
                        "court": "Orléans",
                        "details": "Avis de dépôtDépôt de l'état des créances et du projet de répartitionL'état des créances complété par le projet de répartition prévu par l'article L 644-4 du code de commerce est déposé au greffe. Tout intéressé peut contester ledit état devant le juge-commissaire dans un délai d'un mois à compter de la présente publication.",
                        "effectiveDate": "2014-02-27T00:00:00Z",
                        "publicationDate": "2014-04-01T00:00:00Z"
                    },
                    {
                        "judgment": "Involuntary Liquidation",
                        "court": "Orléans",
                        "details": "Extrait de jugementJugement prononçant la résolution du plan de redressement et la liquidation judiciaireJugement prononçant la résolution du plan de redressement et la liquidation judiciaire, date de cessation des paiements le 30 Septembre 2012, désignant liquidateur Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations de créances sont à déposer auprès du liquidateur dans le délai de deux mois à compter de la présente publication à l'exception des créanciers admis au plan qui en sont dispensés.",
                        "effectiveDate": "2013-03-27T00:00:00Z",
                        "publicationDate": "2013-04-17T00:00:00Z"
                    },
                    {
                        "judgment": "Rulings linked to debts",
                        "court": "Orléans",
                        "details": "Avis de dépôtDépôt de l'état des créancesL'état des créances est déposé au greffe où tout intéressé peut présenter réclamation devant le juge-commissaire dans le délai d'un mois à compter de la présente publication.",
                        "effectiveDate": "2012-10-24T00:00:00Z",
                        "publicationDate": "2012-11-16T00:00:00Z"
                    },
                    {
                        "judgment": "Recovery Plan",
                        "court": "Orléans",
                        "details": "Extrait de jugementJugement de plan de redressementJugement arrêtant le plan de redressement, durée du plan 120 mois nomme Commissaire à l'exécution du plan Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans .",
                        "effectiveDate": "2012-09-26T00:00:00Z",
                        "publicationDate": "2012-10-19T00:00:00Z"
                    },
                    {
                        "judgment": "Receivership",
                        "court": "Orléans",
                        "details": "Jugement d'ouvertureJugement d'ouverture d'une procédure de redressement judiciaireJugement prononçant l'ouverture d'une procédure de redressement judiciaire, date de cessation des paiements le 16 Juin 2010 désignant mandataire judiciaire Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations des créances sont à déposer au mandataire judiciaire dans les deux mois à compter de la présente publication.",
                        "effectiveDate": "2011-11-16T00:00:00Z",
                        "publicationDate": "2011-12-14T00:00:00Z"
                    }
                ],
                "otherSources": [
                    {
                        "judgment": "Redressement Judiciaire",
                        "court": "Tribunal de Commerce d'ORLEANS",
                        "representative": "MAîTRE CHRISTIAN SAULNIER 6 BIS",
                        "effectiveDate": "2011-11-16T00:00:00Z"
                    }
                ]
            },
            "preferentialRightsDetails": {
                "statusOfMonitoring": "This company is not under monitoring",
                "numberOfActivePreferentialRights": 0,
                "socialSecurityAndPensionFunds": {
                    "numberOfPreferentialRights": 0
                },
                "taxOffice": {
                    "numberOfPreferentialRights": 0
                }
            }
        },
        "additionalInformation": {
            "misc": {
                "sizeOfUrbanArea": "Urban unit with 200 000 to 1 999 999 inhabitants",
                "reasonForFormation": "Purchase",
                "financialAccountsType": "F",
                "statusCode": "C",
                "officeType": "1",
                "numberOfBranches": "0",
                "numberOfEmployeesAtAddress": "Workforce unknown",
                "previousSiret": "43501314900016",
                "numberOfEmployeesAtCompany": "1 or 2 employees",
                "activityClassification": "NAF/APE",
                "inseeCode": "45234",
                "additionToName": "LE JULES VERNE",
                "streetAddress": "18 RUE EUGENE VIGNAT",
                "postalCode": "45000",
                "municipality": "ORLEANS",
                "subRegion": "Loiret (45)",
                "numberOfCompanies": 0,
                "deregistrationDate": "2014-09-26T00:00:00Z",
                "courtRegistryNumber": "494814452",
                "courtRegistryNumberAdditional": "20 0 7B00336",
                "registrationCourt": "Orleans (45)",
                "nationality": "France",
                "numberOfDirectors": 1,
                "lastJudgement": "2014-09-26T00:00:00Z",
                "rcsRegistration": "RCS Orleans B 494 814 452",
                "regionDbt": 17,
                "workforceAccount": "3 to 5 employees",
                "preferentialStatus": "-",
                "negativeRating": -1,
                "summaryFormationDate": "04/2007",
                "postalAddress": "SCORE, LE JULES VERNE, 18 RUE EUGENE VIGNAT, 45000 ORLEANS"
            },
            "trends": {
                "profitability": "Less",
                "liquidity": "Greater",
                "netWorth": "Less"
            },
            "establishmentDetails": {
                "activityNature": "Retail trade",
                "typeOfEstablishmentDescription": "Head Office",
                "formationDate": "2007-04-01T00:00:00Z",
                "locationSurface": "Less than 300 m²",
                "activityLocation": "Store",
                "department": "Loiret (45)",
                "district": "2",
                "area": "99",
                "tradingAddress": "18 RUE EUGENE VIGNAT 45000 ORLEANS",
                "city": "ORLEANS"
            },
            "otherEstablishmentDetails": {
                "apeNafCode": "5610A"
            },
            "exposureIndicator": {
                "companyExposure": 0,
                "activityLoss": 0
            },
            "companyHistory": [
                {
                    "date": "2018-07-30T00:00:00Z",
                    "description": "Update Rating"
                },
                {
                    "date": "2014-10-06T00:00:00Z",
                    "description": "Payment incident closed"
                },
                {
                    "date": "2014-10-05T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2014-09-26T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2014-04-01T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2013-10-18T00:00:00Z",
                    "description": "Update Rating"
                },
                {
                    "date": "2013-09-20T00:00:00Z",
                    "description": "Payment incident closed"
                },
                {
                    "date": "2013-08-12T00:00:00Z",
                    "description": "Payment incident detected"
                },
                {
                    "date": "2013-04-17T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2013-04-05T00:00:00Z",
                    "description": "Payment incident detected"
                },
                {
                    "date": "2013-03-27T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2012-11-16T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2012-10-19T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2012-10-01T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2012-09-26T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2012-05-04T00:00:00Z",
                    "description": "Payment incident closed"
                },
                {
                    "date": "2011-12-14T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2011-11-21T00:00:00Z",
                    "description": "Payment incident detected"
                },
                {
                    "date": "2011-11-17T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2011-11-17T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2011-11-16T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2011-11-16T00:00:00Z",
                    "description": "New collective procedure"
                },
                {
                    "date": "2011-10-20T00:00:00Z",
                    "description": "Consideration of a balance sheet that has led to a reassessment of this company's creditworthiness"
                },
                {
                    "date": "2010-10-18T00:00:00Z",
                    "description": "Bodacc C : Deposit accounts notice"
                },
                {
                    "date": "2010-09-30T00:00:00Z",
                    "description": "New accounts available"
                },
                {
                    "date": "2009-09-30T00:00:00Z",
                    "description": "New accounts available"
                },
                {
                    "date": "2008-09-30T00:00:00Z",
                    "description": "New accounts available"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Update of Company Activity"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Reactivation of Company"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Modification of Company Activity"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Update of Company Concern status"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Modification to Establishment Address or Identifier"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Formation of Company"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Appointment/resignation of company officers"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Appointment/resignation of company officers"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Articles of association"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Company formation"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Fund deposit certificate"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Fund deposit certificate"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Private document"
                },
                {
                    "date": "2007-03-29T00:00:00Z",
                    "description": "Private document"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Update of Company Activity"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Modification of Company Activity (error correction)"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Deactivation of Company (error correction)"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Update of Company Concern status"
                }
            ],
            "establishmentHistory": [
                {
                    "date": "2013-01-13T00:00:00Z",
                    "description": "Update of phone numbers"
                },
                {
                    "date": "2007-07-25T00:00:00Z",
                    "description": "Update of phone numbers"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Update of Establishment Activity"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Modification of Head office"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Update of Establishment Trade name"
                },
                {
                    "date": "2007-04-06T00:00:00Z",
                    "description": "Update of Establishment Concern status"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Modification of Head office Identification"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Formation of Head office"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Formation of Establishment"
                },
                {
                    "date": "2007-04-01T00:00:00Z",
                    "description": "Update of Establishment Trade name"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Update of Establishment Activity"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Modification of Head office Activity"
                },
                {
                    "date": "2007-03-05T00:00:00Z",
                    "description": "Update of Establishment Concern status"
                }
            ],
            "gazettes": [
                {
                    "publicationDate": "2014-10-05T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Jugement de clôture",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "912 - Date : 17 septembre 2014. Jugement de clôture pour insuffisance d'actif. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Café bar brasserie jeux locaux meubles avec licence Iv. Adresse : 18 rue Eugene Vignat, 45000 Orleans. Complément de jugement : Jugement prononçant la clôture de la procédure de liquidation judiciaire pour insuffisance d'actif."
                },
                {
                    "publicationDate": "2014-04-01T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Avis de dépôt",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "1872 - Date : 27 février 2014. Dépôt de l'état des créances et du projet de répartition. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Restauration traditionnelle. Adresse : 18 rue Eugène Vignat, 45000 Orléans. Complément de jugement : L'état des créances complété par le projet de répartition prévu par l'article L 644-4 du code de commerce est déposé au greffe. Tout intéressé peut contester ledit état devant le juge-commissaire dans un délai d'un mois à compter de la présente publication."
                },
                {
                    "publicationDate": "2013-04-17T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Extrait de jugement",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "1885 - Date : 27 mars 2013. Jugement prononçant la résolution du plan de redressement et la liquidation judiciaire. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Restauration traditionnelle. Adresse : 18 rue Eugène Vignat, 45000 Orléans. Complément de jugement : Jugement prononçant la résolution du plan de redressement et la liquidation judiciaire, date de cessation des paiements le 30 Septembre 2012, désignant liquidateur Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations de créances sont à déposer auprès du liquidateur dans le délai de deux mois à compter de la présente publication à l'exception des créanciers admis au plan qui en sont dispensés."
                },
                {
                    "publicationDate": "2012-11-16T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Avis de dépôt",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "779 - Date : 24 octobre 2012. Dépôt de l'état des créances. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Restauration traditionnelle. Adresse : 18 rue Eugène Vignat, 45000 Orléans. Complément de jugement : L'état des créances est déposé au greffe où tout intéressé peut présenter réclamation devant le juge-commissaire dans le délai d'un mois à compter de la présente publication."
                },
                {
                    "publicationDate": "2012-10-19T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Extrait de jugement",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "1347 - Date : 26 septembre 2012. Jugement de plan de redressement. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Restauration traditionnelle. Adresse : 18 rue Eugène Vignat, 45000 Orléans. Complément de jugement : Jugement arrêtant le plan de redressement, durée du plan 120 mois nomme Commissaire à l'exécution du plan Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans ."
                },
                {
                    "publicationDate": "2011-12-14T00:00:00Z",
                    "type": "Bodacc A : Procédures collectives",
                    "name": "A_PCL",
                    "description": "Jugement d'ouverture",
                    "publicationArea": "45 - LOIRET",
                    "court": "TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "1339 - Date : 16 novembre 2011. Jugement d'ouverture d'une procédure de redressement judiciaire. 494 814 452 RCS Orléans. SCORE. Forme : Société à responsabilité limitée. Activité : Restauration traditionnelle. Adresse : 18 rue Eugène Vignat, 45000 Orléans. Complément de jugement : Jugement prononçant l'ouverture d'une procédure de redressement judiciaire, date de cessation des paiements le 16 Juin 2010 désignant mandataire judiciaire Maître Christian SAULNIER 6 Bis, rue des Anglaises - 45000 Orléans . Les déclarations des créances sont à déposer au mandataire judiciaire dans les deux mois à compter de la présente publication."
                },
                {
                    "publicationDate": "2010-10-18T00:00:00Z",
                    "type": "Bodacc",
                    "name": "C",
                    "description": "Comptes annuels et rapports",
                    "publicationArea": "45 - LOIRET",
                    "court": "GREFFE DU TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "6718 - 494814452 RCS. SCORE. Forme : Société à responsabilité limitée. Adresse : 18 rue Eugène Vignat    45000 Orléans. Commentaires : Comptes annuels et rapports de l'exercice clos le : 30/09/2008."
                },
                {
                    "publicationDate": "2010-10-18T00:00:00Z",
                    "type": "Bodacc",
                    "name": "C",
                    "description": "Comptes annuels et rapports",
                    "publicationArea": "45 - LOIRET",
                    "court": "GREFFE DU TRIBUNAL DE COMMERCE D'ORLÉANS",
                    "detail": "6719 - 494814452 RCS. SCORE. Forme : Société à responsabilité limitée. Adresse : 18 rue Eugène Vignat    45000 Orléans. Commentaires : Comptes annuels et rapports de l'exercice clos le : 30/09/2009."
                },
                {
                    "publicationDate": "2007-07-13T00:00:00Z",
                    "type": "Bodacc",
                    "name": "A_REG",
                    "description": "Vente et cession",
                    "publicationArea": "1190 - RCS Orléans B 494 814 452. SCORE. Forme : S.A.R.L. Capital : 7 500 euros. Adresse du siège social : 18 rue Eugène-Vignat, 45000 Orléans. Etablissement principal - Activité : café, bar, brasserie, jeux, locaux meublés avec licence de 4e catégorie. Adresse : 18 rue Eugène-Vignat, 45000 Orléans. Etablissement principal acquis par achat au prix stipulé de 132 000 euros. Date de début d'activité : 6 avril 2007. Précédent propriétaire : REDA. RCS Orléans 435 013 149. Publication légale : Le Courrier du Loiret du 17 mai 2007. Oppositions : Me Blachier, 2 avenue de Paris, 45000 Orléans."
                },
                {
                    "publicationDate": "2007-04-29T00:00:00Z",
                    "type": "Bodacc",
                    "name": "A_REG",
                    "description": "Création d'établissement",
                    "publicationArea": "0832 - RCS Orléans B 494 814 452. RC 07-B 336. SCORE. Forme : S.A.R.L. Capital : 7 500 euros. Adresse du siège social : 18 rue Eugène-Vignat, 45000 Orléans. Administration : gérant : DUBOIS (Florent, Jean, Roger, André) (Nom d'usage : DUBOIS). Cette société se constitue , mais n'exploite provisoirement aucun établissement."
                }
            ],
            "commentaries": [
                {
                    "commentaryText": "Company closed or dissolved",
                    "positiveOrNegative": "Negative"
                }
            ],
            "ratingHistory": [
                {
                    "date": "2021-05-07T00:00:00Z",
                    "commonRating": {
                        "commonValue": "E",
                        "commonDescription": "Not Scored"
                    },
                    "description2": "Not Rated"
                },
                {
                    "date": "2021-05-07T00:00:00Z",
                    "localRating": "-1",
                    "commonRating": {
                        "commonValue": "E",
                        "commonDescription": "Not Scored"
                    },
                    "description2": "Not Rated",
                    "limit": 0
                },
                {
                    "date": "2018-07-30T00:00:00Z",
                    "localRating": "-1",
                    "commonRating": {
                        "commonValue": "E",
                        "commonDescription": "Not Scored"
                    },
                    "description2": "Not Rated",
                    "limit": 0
                },
                {
                    "date": "2013-10-18T00:00:00Z",
                    "localRating": "-1",
                    "commonRating": {
                        "commonValue": "E",
                        "commonDescription": "Not Scored"
                    },
                    "description2": "Not Rated",
                    "limit": 0
                },
                {
                    "localRating": "-1",
                    "commonRating": {
                        "commonValue": "E",
                        "commonDescription": "Not Scored"
                    },
                    "description2": "Not Rated",
                    "limit": 0
                }
            ],
            "industryAverages": {
                "creditLimit": 5649,
                "creditRating": 35
            },
            "keyFinancials": [
                {
                    "yearToDate": "2010-09-30T00:00:00Z",
                    "turnover": 226415,
                    "grossOperatingSurplus": 5.57,
                    "shareholdersEquity": -167924,
                    "netResult": -36276,
                    "employees": "3 employees"
                },
                {
                    "yearToDate": "2009-09-30T00:00:00Z",
                    "turnover": 351873,
                    "grossOperatingSurplus": -3.8,
                    "shareholdersEquity": -127467,
                    "netResult": -55790,
                    "employees": "1 or 2 employees"
                },
                {
                    "yearToDate": "2008-09-30T00:00:00Z",
                    "turnover": 504987,
                    "grossOperatingSurplus": -13.28,
                    "shareholdersEquity": -67497,
                    "netResult": -91720,
                    "employees": "1 or 2 employees"
                }
            ],
            "branches": [
                {
                    "companyNumber": "49481445200012",
                    "companyName": "SCORE",
                    "type": "Head Office",
                    "lineOfBusiness": "Traditional catering",
                    "status": "C",
                    "activityApe": "5610A",
                    "name": "SCORE",
                    "additionToName": "LE JULES VERNE",
                    "address": {
                        "simpleValue": "18 RUE EUGENE VIGNAT ORLEANS 45000",
                        "street": "18 RUE EUGENE VIGNAT",
                        "city": "ORLEANS",
                        "postalCode": "45000"
                    },
                    "distribution": "45000 ORLEANS"
                }
            ],
            "enquiriesTrend": {
                "month1": 0,
                "month2": 0,
                "month3": 0,
                "month4": 0,
                "month5": 0,
                "month6": 0,
                "month7": 0,
                "month8": 0,
                "month9": 0,
                "month10": 0,
                "month11": 0,
                "month12": 0,
                "months1to3": 0,
                "months4to6": 0,
                "months7to9": 0,
                "months10to12": 0,
                "monthlyAverage": 0
            }
        }
    },
    "companyId": "FR-X-49481445200012",
    "dateOfOrder": "2022-07-22T11:24:39.894Z",
    "language": "en",
    "userId": "101713178"
}

credentials = {
    "username": "VPERES@scor.com",
    "password": "Wy05!UQKPkE'*HVN%Gh("
}
auth_url = "https://connect.creditsafe.com/v1/authenticate"
url = "https://connect.creditsafe.com/v1/companies?name={}&countries={}"
detail_url = "https://connect.creditsafe.com/v1/companies/{}"


def authenticate():
    response = requests.post(auth_url, credentials)
    if response.status_code == 200:
        return response.json()['token']
    else:
        print('Auth Failed')


def credit_safe(token):
    req_url = url.format("score", "FR")
    response = requests.get(req_url, headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(token)})
    if response.status_code == 200:
        companies = response.json()['companies']
        if len(companies) == 0:
            print('Aucun résultat trouvé')
            return

        for company in companies[:1]:
            json = {
                "company_provider_id": company['id'], "country_code": company['country'], "name": company['name'],
                "status": "Inactive" if company['status'] == "NonActive" else "Active",
                "city": company['address']['city'],
                "postal_code": company['address']['postCode'], "adress_line": company['address']['street']
            }
            print(json)
            print('===============================')

    else:
        print('THROW EXCPETION HERE')
        # return 'THROW EXCPETION HERE'


def credit_safe_processing_search():
    token = authenticate()
    credit_safe(token)


def credit_safe_processing_detail():
    token = authenticate()
    get_company_detail_from_provider(token, "FR-X-49481445200012")


def check_company_validity():
    company = get_a_company("FR-X-49481445200012")
    company['created_on'] = "2022/05/01"
    company['company_provider_id'] = "FR-X-49481445200012"
    if company and check_date_validity(company['created_on'], 90):
        # nous allons récupérer les info du client depuis la base de données unlockfree
        print('KOLCHI MZYANA')
    else:
        get_company_detail_from_provider(company['company_provider_id'])


def get_a_company(company_provider_id):
    c = Company().load({'company_provider_id': company_provider_id})
    return c if c.id else None


def check_date_validity(created_on, threshold):
    format = "%Y/%m/%d"
    to_day = datetime.now().strftime(format)

    d1 = datetime.strptime(to_day, format)
    d2 = datetime.strptime(created_on, format)

    difference = (d1 - d2).days

    if difference > threshold:
        print('Date Invalide')
    else:
        print('OK')


def get_company_detail_from_provider(token, company_provider_id):
    req_url = detail_url.format(company_provider_id)
    response = requests.get(req_url, headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(token)})
    if response.status_code == 200:
        company_report = response.json()
        company_report['data_provider_comapny_id'] = company_provider_id

        store_company_unlockfree(company_report)
        # store_company_dtw(company_report)

    else:
        print('THROW EXCPETION HERE')
        return 'THROW EXCPETION HERE'


def store_company_unlockfree(company_report):
    dict = get_a_company(company_report['company_provider_id'])

    if not dict.id:
        new_dict = Company(**{**company_report, **{
            'id': "generate_id",
            'created_on': datetime.now().strftime("%Y/%m/%d"),
        }})
        dict = new_dict

    dict.credit_rating = data['report']['companySummary']['creditRating'] or None
    dict.modified_on = datetime.now().strftime("%Y/%m/%d")
    dict.save()


if __name__ == '__main__':
    # print(data['report']['companySummary']['creditRating'] or None)
    # credit_safe_processing_detail()
    credit_safe_processing()
    # check_date_validity("2022/05/01", 90)
    # get_company_detail_from_provider('FR-X-49481445200012')

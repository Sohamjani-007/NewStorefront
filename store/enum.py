
gender_dict = {"1": "MALE", "2": "FEMALE", "3": "TRANSGENDER"}

account_holder_type_code = {"1": "Individual", "2": "Joint", "3": "Authorized User", "7": "Guarantor", "20": "Deceased"}

marital_status_code = {"1": "Single", "2": "Married", "4": "Divorced", "3": "Widow/Widower"}

phone_type_dict = {"01": "Mobile", "02": "Mobile"}

account_type_code_dict = {"1":"AUTO LOAN","2":"HOUSING LOAN","3":"PROPERTY LOAN","4":"LOAN AGAINST SHARES/SECURITIES","5":"PERSONAL LOAN","6":"CONSUMER LOAN","7":"GOLD LOAN","8":"EDUCATIONAL LOAN","9":"LOAN TO PROFESSIONAL", "10":"CREDIT CARD","11":"LEASING","12":"OVERDRAFT","13":"TWO-WHEELER LOAN","14":"NON-FUNDED CREDIT FACILITY","15":"LOAN AGAINST BANK DEPOSITS","16":"FLEET CARD","17":"Commercial Vehicle Loan","18":"Telco – Wireless","19":"Telco – Broadband","20":"Telco – Landline","23":"GECL Secured","24":"GECL Unsecured","31":"Secured Credit Card","32":"Used Car Loan","33":"Construction Equipment Loan","34":"Tractor Loan","35":"Corporate Credit Card","36":"Kisan Credit Card","37":"Loan on Credit Card","38":"Prime Minister Jaan Dhan Yojana - Overdraft","39":"Mudra Loans – Shishu / Kishor / Tarun","40":"Microfinance – Business Loan","41":"Microfinance – Personal Loan","42":"Microfinance – Housing Loan","43":"Microfinance – Others","44":"Pradhan Mantri Awas Yojana - Credit Link Subsidy Scheme MAY CLSS", "45" : "P2P Personal Loan", "46" : "P2P Auto Loan", "47" : "P2P Education Loan", "51" : "BUSINESS LOAN – GENERAL", "52" : "BUSINESS LOAN –PRIORITY SECTOR – SMALL BUSINESS", "53" : "BUSINESS LOAN –PRIORITY SECTOR – AGRICULTURE", "54" : "BUSINESS LOAN –PRIORITY SECTOR – OTHERS", "55" : "BUSINESS NON-FUNDED CREDIT FACILITY – GENERAL", "56" : "BUSINESS NON-FUNDED CREDIT FACILITY – PRIORITY SECTOR – SMALL BUSINESS", "57" : "BUSINESS NON-FUNDED CREDIT FACILITY – PRIORITY SECTOR – AGRICULTURE", "58" : "BUSINESS NON-FUNDED CREDIT FACILITY – PRIORITY SECTOR – OTHERS", "59" : "BUSINESS LOANS AGAINST BANK DEPOSITS", "60" : "Staff Loan", "61" : "Business Loan - Unsecured", "00" : "Others"}

account_status_code = {"00": "No Suit Filed", "89": "Wilful default", "93": "Suit Filed(Wilful default)",
                       "97": "Suit Filed(Wilful Default) and Written-off", "30": "Restructured",
                       "31": "Restructured Loan (Govt. Mandated)", "32": "Settled", "33": "Post (WO) Settled",
                       "34": "Account Sold", "35": "Written Off and Account Sold", "36": "Account Purchased",
                       "37": "Account Purchased and Written Off", "38": "Account Purchased and Settled",
                       "39": "Account Purchased and Restructured", "40": "Status Cleared", "41": "Restructured Loan",
                       "42": "Restructured Loan (Govt. Mandated)", "43": "Written-off", "44": "Settled",
                       "45": "Post (WO) Settled", "46": "Account Sold", "47": "Written Off and Account Sold",
                       "48": "Account Purchased", "49": "Account Purchased and Written Off",
                       "50": "Account Purchased and Settled", "51": "Account Purchased and Restructured", "52": "Status Cleared",
                       "53": "Suit Filed", "54": "Suit Filed and Written-off", "55": "Suit Filed and Settled",
                       "56": "Suit Filed and Post (WO) Settled", "57": "Suit Filed and Account Sold",
                       "58": "Suit Filed and Written Off and Account Sold", "59": "Suit Filed and Account Purchased",
                       "60": "Suit Filed and Account Purchased and Written Off", "61": "Suit Filed and Account Purchased and Settled",
                       "62": "Suit Filed and Account Purchased and Restructured", "63": "Suit Filed and Status Cleared",
                       "64": "Wilful Default and Restructured Loan", "65": "Wilful Default and Restructured Loan (Govt. Mandated)",
                       "66": "Wilful Default and Settled", "67": "Wilful Default and Post (WO) Settled",
                       "68": "Wilful Default and Account Sold", "69": "Wilful Default and Written Off and Account Sold",
                       "70": "Wilful Default and Account Purchased", "72": "Wilful Default and Account Purchased and Written Off",
                       "73": "Wilful Default and Account Purchased and Settled", "74": "Wilful Default and Account Purchased and Restructured",
                       "75": "Wilful Default and Status Cleared", "76": "Suit filed (Wilful default) and Restructured",
                       "77": "Suit filed (Wilful default) and Restructured Loan (Govt.Mandated)",
                       "79": "Suit filed (Wilful default) and Settled", "81": "Suit filed (Wilful default) and Post (WO) Settled",
                       "85": "Suit filed (Wilful default) and Account Sold", "86": "Suit filed (Wilful default) and Written Off and Account Sold",
                       "87": "Suit filed (Wilful default) and Account Purchased", "88": "Suit filed (Wilful default) and Account Purchased and WrittenOff",
                       "94": "Suit filed (Wilful default) and Account Purchased and Settled", "90": "Suit filed (Wilful default) and Account Purchased and Restructured",
                       "91": "Suit filed (Wilful default) and Status Cleared", "13": "CLOSED", "14": "CLOSED", "15": "CLOSED",
                       "16": "CLOSED", "16": "CLOSED", "16": "CLOSED", "17": "CLOSED", "12": "CLOSED", "11": "ACTIVE",
                       "71": "ACTIVE", "78": "ACTIVE", "80": "ACTIVE", "82": "ACTIVE", "83": "ACTIVE", "84": "ACTIVE",
                       "DEFAULTVALUE": "ACTIVE", "21": "ACTIVE", "22": "ACTIVE", "23": "ACTIVE", "24": "ACTIVE", "25": "ACTIVE",
                       "131": "Restructured due to natural calamity", "130": "Restructured due to COVID-19"}

search_type_dict = {"1": {"value": "Agriculture Loan", "option": {"1": "Agricultural Machinery", "2": "Animal Husbandry",
                                                                  "3": "Aquaculture", "4": "Biogas Plant", "5": "Crop Loan",
                                                                  "6": "Horticulture", "7": "Irrigation System", "99": "Others"}},
                    "2": {"value": "Auto Loan", "option": {"8": "New Car", "9": "Overdraft against Car", "10": "Used Car", "99": "Others"}},
                    "3": {"value": "Business Loan", "option": {"11": "General", "12": "Small & Medium Business", "13": "Professionals", "14": "Trade", "99": "Others"}},
                    "4": {"value": "Commercial Vehicle Loans", "option": {"15": "Bus", "16": "Tempo", "17": "Tipper", "18": "Truck", "99": "Others"}},
                    "5": {"value": "Construction Equipment loan", "option": {"20": "Forklift", "21": "Wheel Loaders", "99": "Others"}},
                    "6": {"value": "Consumer Loan ", "option": {"22": "Consumer Search", "66": "Consumer Search Loan", "68": "Consumer Search Loan", "99": "Others"}},
                    "7": {"value": "Credit Card ", "option": {"23": "Credit Card", "24": "Fleet Card", "99": "Others"}},
                    "8": {"value": "Education Loan ", "option": {"25":"For Working Executives", "26": "Study Abroad", "27": "Study in India", "99": "Others"}},
                    "9": {"value": "Leasing ", "option": {"28": "Leasing", "99": "Others"}},
                    "10": {"value": "Loan against collateral ", "optional": {"29": "Bank Deposits", "30": "Gold", "31": "Govt. Bonds / PPF / NSC / KVP / FD", "32": "Shares and Mutual Funds", "99": "Others"}},
                    "11": {"value": "Microfinance ", "option": {"33": "Business Loan", "34": "Housing Loan", "35": "Personal Loan", "99": "Others"}},
                    "12": {"value": "Non-funded Credit Facility ", "optional": {"36": "Agriculture", "37": "General", "38": "Small Business", "99": "Others"}},
                    "13": {"value": "Personal Loan ", "option": {"39": "Computers / Laptops", "40": "Consumer Durables", "41": "Marriage / Religious Ceremonies", "42": "Travel", "99": "Others"}},
                    "14": {"value": "Property Loan", "option": {"43": "Balance Transfer", "44": "Home Improvement / Extension", "45": "Land", "46": "Lease Rental Discounting", "47": "Loan against Property", "48": "New Home", "49": "Office Premises", "50": "Under construction", "99": "Others"}},
                    "15": {"value": "Telecom", "option": {"51": "Broadband", "52": "Landline", "53": "Mobile", "99": "Others"}},
                    "16": {"value": "Two/Three Wheeler Loan ", "option": {"54": "Three Wheeler", "55": "Two Wheeler", "99": "Others"}},
                    "17": {"value": "Working Capital Loan", "option": {"56": "Cash credit facility", "57": "Overdraft", "58": "Term Loan", "99": "Others"}},
                    "18": {"value": "Consumer Loan", "option": {"39": "Computers / Laptops", "40": "Consumer Durables", "99": "Others"}},
                    "19": {"value": "Credit Review", "option": {"60": "Microfinance Detailed Report", "61": "Summary Report", "62": "VB OLM Retrieval Service", "63": "Account Review", "64": "Retro Enquiry", "65": "Locate Plus", "67": "Indicative Report", "69": "Bank OLM Retrieval Service", "70": "Adviser Liability", "71": "Secured (Account Group for Portfolio Review response)", "72": "Unsecured (Account Group for Portfolio Review response)", "99": "Others"}},
                    "99": {"value": "Others ", "option": {"99": "Others "}}
                    }

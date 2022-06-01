from itertools import groupby
from django.db.models import Value
from django.views.generic import ListView
import json
from multiprocessing import context
from random import sample
import xmltodict
import datetime
import calendar
from django.template.loader import get_template 
from django import template
from store.enum import gender_dict, account_holder_type_code, marital_status_code, phone_type_dict, account_type_code_dict, account_status_code, search_type_dict, income_segment_dict



class CustomerCreditReport:

    def get_payment_history(self, input_data):
        """
        Empty list is given to append output_dict.

        For loop:
            To make grouping of year by groupby method.

          For loop:
           Includes all month names in lower().
           Finally appended.

        Month names starting from jan [1:] Index=1.
        Added into list,  empty list final_output.
        if month_short_name != days_past_due , add 0.
        Added into final_output and return it.
        """

        def key_func(k):
            return k['Year']

        output_data_v1 = []
        for key, value in groupby(input_data, key_func):
            output_dict = dict(year=key)
            for input_dict in list(value):
                month = input_dict.get("Month")
                month_name = datetime.datetime.strptime(month, "%m").strftime("%b").lower()
                days_past_due = input_dict.get("Days_Past_Due", "") if input_dict.get("Days_Past_Due", "") else ""
                asset_classification = input_dict.get("Asset_Classification", "") if input_dict.get("Asset_Classification", "") else ""
                output_dict[str(month_name)] = days_past_due if days_past_due else asset_classification
            output_data_v1.append(output_dict)

        month_long_name_list = calendar.month_name[1:]
        month_short_name_list = list()
        for month_long_name in month_long_name_list:
            short_name = datetime.datetime.strptime(month_long_name, '%B').strftime(
                '%b').lower()
            month_short_name_list.append(short_name)

        final_output = []
        for output_data_dict in output_data_v1:
            for month_short_name in month_short_name_list:
                if month_short_name not in output_data_dict.keys():
                    output_data_dict[month_short_name] = ""
            final_output.append(output_data_dict)
        return final_output

    def get_account_review_data(self, account_review_data):
        def key_func(k):
            return k['Year']

        # actual payment amount from account review data
        output_data_v2 = []
        for key, value in groupby(account_review_data, key_func):
            output_account_review_dict = dict(year=key)
            for input_dict in list(value):
                month = input_dict.get("Month")
                month_name = datetime.datetime.strptime(month, "%m").strftime("%b").lower()
                month_data_dict = dict(credit_limit_amount=input_dict.get("Credit_Limit_Amount", '') if input_dict.get("Credit_Limit_Amount", '') else '',
                                       current_balance=input_dict.get("Current_Balance", '') if input_dict.get("Current_Balance", '') else '',
                                       actual_payment_amount=input_dict.get("Actual_Payment_Amount", '') if input_dict.get("Actual_Payment_Amount", '') else '',
                                       cash_limit=input_dict.get('Cash_Limit', '') if input_dict.get('Cash_Limit', '') else '',
                                       emi_amount=input_dict.get('EMI_Amount', '') if input_dict.get('EMI_Amount', '') else '',
                                       account_status=input_dict.get('Account_Status', '') if input_dict.get('Account_Status', '') else '',
                                       amount_past_due=input_dict.get('Amount_Past_Due', '') if input_dict.get('Amount_Past_Due', '') else ''
                                       )
                output_account_review_dict[str(month_name)] = month_data_dict
            output_data_v2.append(output_account_review_dict)

        month_long_name_list = calendar.month_name[1:]
        month_short_name_list = list()
        for month_long_name in month_long_name_list:
            short_name = datetime.datetime.strptime(month_long_name, '%B').strftime('%b').lower()
            month_short_name_list.append(short_name)

        final_output_payment_amt = []
        for output_data_dict2 in output_data_v2:
            for month_short_name in month_short_name_list:
                if month_short_name not in output_data_dict2.keys():
                    output_data_dict2[month_short_name] = dict(credit_limit_amount='', current_balance='',
                                                               actual_payment_amount='', cash_limit='',
                                                               emi_amount='', account_status='',
                                                               amount_past_due='')
            final_output_payment_amt.append(output_data_dict2)

        return final_output_payment_amt

    def get_json_data(self):
        json_data = {"INProfileResponse": {
            "CAPS": {
                "CAPS_Summary": {
                    "CAPSLast7Days": "2",
                    "CAPSLast30Days": "2",
                    "CAPSLast90Days": "3",
                    "CAPSLast180Days": "3"
                },
                "CAPS_Application_Details": [
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1653016671315",
                        "Enquiry_Reason": "7",
                        "Amount_Financed": "10000",
                        "Date_of_Request": "20220520",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Axis Bank",
                        "Subscriber_code": "PVTAXIS001",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "36",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "919411635394",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "MODINAGAR",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "KADIM",
                            "FlatNoPlotNoHouseNo": "MOHAMMADPUR",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1652860374373",
                        "Enquiry_Reason": "2",
                        "Amount_Financed": "650000",
                        "Date_of_Request": "20220518",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "State Bank of India",
                        "Subscriber_code": "PUBSBI0008",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "3",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "00",
                            "Passport_number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Telephone_Extension": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None,
                            "Telephone_Number_Applicant_1st": "09411635394"
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "GHAZIABAD-NOIDA",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "HAZIABAD",
                            "FlatNoPlotNoHouseNo": "S/O SATYAPRAKASH TYAGIMOHAMMADPUR KADIM",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": {
                            "City": "GHAZIABAD-NOIDA",
                            "State": "09",
                            "PINCode": "201002",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "353,NEW FRIENDS  COLONYSEC-23 SANJAY NAG",
                            "FlatNoPlotNoHouseNo": "RADHE TOURS AND TRAVELSPLOT NO-35 KH NO-",
                            "RoadNoNameAreaLocality": "AR GZB"
                        }
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1646285342502",
                        "Enquiry_Reason": "7",
                        "Amount_Financed": "10000",
                        "Date_of_Request": "20220303",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Axis Bank",
                        "Subscriber_code": "PVTAXIS001",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "36",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "919411635394",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "MODINAGAR",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": "PRIMARY SCHOOL",
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "MODINAGAR GHAZIABAD",
                            "FlatNoPlotNoHouseNo": "HNO 85/8, MOHAMMADPUR KADIM",
                            "RoadNoNameAreaLocality": "NEAR PRIMARY SCHOOL"
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1616417174559",
                        "Enquiry_Reason": "13",
                        "Amount_Financed": "0",
                        "Date_of_Request": "20210322",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Whizdm Finance Pvt Ltd",
                        "Subscriber_code": "85307",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "0",
                        "CAPS_Applicant_Details": {
                            "EMailId": "abneeshmishra626@gmail.com",
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "8800467530",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "Gautam Buddha Nagar",
                            "State": "09",
                            "PINCode": "201307",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": None,
                            "FlatNoPlotNoHouseNo": "Gautam Buddha Nagar_UTTAR PRADESH",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1610688405453",
                        "Enquiry_Reason": "13",
                        "Amount_Financed": "0",
                        "Date_of_Request": "20210115",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "IVL Finance Ltd",
                        "Subscriber_code": "51334",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "48",
                        "CAPS_Applicant_Details": {
                            "EMailId": "ZZZZZ@ZZZ.COM",
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "8171039067",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "ZZZZZ",
                            "State": "99",
                            "PINCode": "201017",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "ZZZZZ",
                            "FlatNoPlotNoHouseNo": "ZZZZZ",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": {
                            "City": "ZZZZZ",
                            "State": "99",
                            "PINCode": "201017",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": None,
                            "FlatNoPlotNoHouseNo": "ZZZZZ",
                            "RoadNoNameAreaLocality": None
                        }
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1592477579067",
                        "Enquiry_Reason": "13",
                        "Amount_Financed": "0",
                        "Date_of_Request": "20200618",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Whizdm Finance Pvt Ltd",
                        "Subscriber_code": "85307",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "0",
                        "CAPS_Applicant_Details": {
                            "EMailId": "vikashtyagi517@gmail.com",
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "8171039067",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "Ghaziabad",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": None,
                            "FlatNoPlotNoHouseNo": "None",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1580978628565",
                        "Enquiry_Reason": "13",
                        "Amount_Financed": "10000",
                        "Date_of_Request": "20200206",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "PC Financial Services Pvt. Ltd.",
                        "Subscriber_code": "77306",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "15",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "Tyagi",
                            "First_Name": "Vikash Kumar Tyagi",
                            "Gender_Code": None,
                            "IncomeTaxPan": "AJXPT0186G",
                            "Middle_Name1": "KUMAR",
                            "Middle_Name2": "TYAGI",
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "01",
                            "Passport_number": None,
                            "MobilePhoneNumber": "9412571095",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": None,
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "Ghaziabad",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": None,
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "Khanjarpur B.O",
                            "FlatNoPlotNoHouseNo": "NA Adress",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1498270659162",
                        "Enquiry_Reason": "99",
                        "Amount_Financed": "1",
                        "Date_of_Request": "20170624",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Home Credit India Finance Pvt. Ltd",
                        "Subscriber_code": "NBFHOM2832",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "30",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": None,
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "00",
                            "Passport_number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Telephone_Extension": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": "JHX4967212",
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None,
                            "Telephone_Number_Applicant_1st": "8171039067"
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "Modinagar",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": "GOVT SCHOOL",
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "GHAZIABAD MODINAGAR NEAR GOVT SCHOOL &amp;",
                            "FlatNoPlotNoHouseNo": "H.N-85/8 MOHMMADPUR KADEEM PS-MODINAGAR",
                            "RoadNoNameAreaLocality": "PANCHAYAT GHAR"
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    },
                    {
                        "ReportTime": "141952",
                        "ReportNumber": "1489519951931",
                        "Enquiry_Reason": "99",
                        "Amount_Financed": "1",
                        "Date_of_Request": "20170315",
                        "Finance_Purpose": "99",
                        "Subscriber_Name": "Home Credit India Finance Pvt. Ltd",
                        "Subscriber_code": "NBFHOM2832",
                        "CAPS_Other_Details": {
                            "Income": None,
                            "Marital_Status": None,
                            "Employment_Status": None,
                            "Time_with_Employer": None,
                            "Number_of_Major_Credit_Card_Held": None
                        },
                        "Duration_Of_Agreement": "30",
                        "CAPS_Applicant_Details": {
                            "EMailId": None,
                            "Last_Name": "TYAGI",
                            "First_Name": "VIKAS",
                            "Gender_Code": "1",
                            "IncomeTaxPan": None,
                            "Middle_Name1": None,
                            "Middle_Name2": None,
                            "Middle_Name3": None,
                            "PAN_Issue_Date": None,
                            "Telephone_Type": "00",
                            "Passport_number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Telephone_Extension": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Voter_s_Identity_Card": "JHX4967212",
                            "Ration_Card_Issue_Date": None,
                            "Date_Of_Birth_Applicant": "19800525",
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None,
                            "Telephone_Number_Applicant_1st": "9412571095"
                        },
                        "CAPS_Applicant_Address_Details": {
                            "City": "Modinagar",
                            "State": "09",
                            "PINCode": "201204",
                            "Landmark": "PRIMARY SCHOOL",
                            "Country_Code": "IB",
                            "BldgNoSocietyName": "MODINAGAR NEAR PRIMARY SCHOOL",
                            "FlatNoPlotNoHouseNo": "H.NO 85/8, MOHMMAD PUR KADEEM MODINAGAR",
                            "RoadNoNameAreaLocality": None
                        },
                        "CAPS_Applicant_Additional_Address_Details": None
                    }
                ]
            },
            "SCORE": {
                "BureauScore": "583",
                "BureauScoreConfidLevel": "H"
            },
            "Header": {
                "ReportDate": "20220524",
                "ReportTime": "141952",
                "SystemCode": "0",
                "MessageText": None
            },
            "UserMessage": {
                "UserMessageText": "Normal Response"
            },
            "CAIS_Account": {
                "CAIS_Summary": {
                    "Credit_Account": {
                        "CreditAccountTotal": "13",
                        "CreditAccountActive": "8",
                        "CreditAccountClosed": "5",
                        "CreditAccountDefault": "0",
                        "CADSuitFiledCurrentBalance": "0"
                    },
                    "Total_Outstanding_Balance": {
                        "Outstanding_Balance_All": "908322",
                        "Outstanding_Balance_Secured": "838167",
                        "Outstanding_Balance_UnSecured": "70342",
                        "Outstanding_Balance_Secured_Percentage": "92",
                        "Outstanding_Balance_UnSecured_Percentage": "8"
                    }
                },
                "CAIS_Account_DETAILS": [
                    {
                        "Income": None,
                        "Open_Date": "20150124",
                        "Date_Closed": None,
                        "Account_Type": "13",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220331",
                        "Account_Number": "XXXX1480",
                        "Account_Status": "97",
                        "DateOfAddition": "20150531",
                        "Payment_Rating": "6",
                        "Portfolio_Type": "I",
                        "Terms_Duration": None,
                        "Amount_Past_Due": "19216",
                        "Current_Balance": "17598",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "HDFC Bank Ltd",
                        "Terms_Frequency": None,
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "0",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKASH",
                            "First_Name_Non_Normalized": "TYAGI",
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": "0",
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2022",
                                "Month": "01",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "12",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "11",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "10",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "09",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "08",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "07",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "06",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "05",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "04",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "03",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "02",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2021",
                                "Month": "01",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "12",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "11",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "10",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "09",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "08",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "07",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "06",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "05",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "04",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "03",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "02",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2020",
                                "Month": "01",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "12",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "11",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "10",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "09",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "08",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "07",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "06",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "05",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "04",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "03",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "02",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2019",
                                "Month": "01",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "12",
                                "Days_Past_Due": "900",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "11",
                                "Days_Past_Due": "878",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "10",
                                "Days_Past_Due": "848",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "09",
                                "Days_Past_Due": "817",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "08",
                                "Days_Past_Due": "787",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "07",
                                "Days_Past_Due": "756",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "06",
                                "Days_Past_Due": "725",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "05",
                                "Days_Past_Due": "695",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "04",
                                "Days_Past_Due": "664",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "03",
                                "Days_Past_Due": "634",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "02",
                                "Days_Past_Due": "603",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2018",
                                "Month": "01",
                                "Days_Past_Due": "575",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "12",
                                "Days_Past_Due": "544",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "11",
                                "Days_Past_Due": "513",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "10",
                                "Days_Past_Due": "483",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "09",
                                "Days_Past_Due": "452",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "08",
                                "Days_Past_Due": "422",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "07",
                                "Days_Past_Due": "391",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "06",
                                "Days_Past_Due": "360",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "05",
                                "Days_Past_Due": "330",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "04",
                                "Days_Past_Due": "299",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "03",
                                "Days_Past_Due": "269",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "02",
                                "Days_Past_Due": "238",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2017",
                                "Month": "01",
                                "Days_Past_Due": "210",
                                "Asset_Classification": "L"
                            },
                            {
                                "Year": "2016",
                                "Month": "12",
                                "Days_Past_Due": "179",
                                "Asset_Classification": "B"
                            },
                            {
                                "Year": "2016",
                                "Month": "11",
                                "Days_Past_Due": "148",
                                "Asset_Classification": "B"
                            },
                            {
                                "Year": "2016",
                                "Month": "10",
                                "Days_Past_Due": "118",
                                "Asset_Classification": "B"
                            },
                            {
                                "Year": "2016",
                                "Month": "09",
                                "Days_Past_Due": "87",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "08",
                                "Days_Past_Due": "87",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "07",
                                "Days_Past_Due": "87",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "06",
                                "Days_Past_Due": "86",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "05",
                                "Days_Past_Due": "87",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "04",
                                "Days_Past_Due": "56",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "03",
                                "Days_Past_Due": "26",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2016",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "11",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "10",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "09",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "08",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "07",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "06",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2015",
                                "Month": "05",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            }
                        ],
                        "Date_of_Last_Payment": None,
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "PVTHDFC007",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": "60426",
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": None,
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "666666666666666666666666666666666666",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": [
                            {
                                "EMailId": None,
                                "FaxNumber": None,
                                "Telephone_Type": "01",
                                "Telephone_Number": None,
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": "9412571095"
                            },
                            {
                                "EMailId": None,
                                "FaxNumber": None,
                                "Telephone_Type": "02",
                                "Telephone_Number": "9412571095",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            },
                            {
                                "EMailId": None,
                                "FaxNumber": None,
                                "Telephone_Type": "03",
                                "Telephone_Number": "9412571095",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            }
                        ],
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": "17598",
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": "02",
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": None,
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM SIKRIKALAN",
                            "Third_Line_Of_Address_non_normalized": None,
                            "Second_Line_Of_Address_non_normalized": None
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "45451",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20161124",
                        "Date_Closed": "20170627",
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20170630",
                        "Account_Number": "XXXXXX2535",
                        "Account_Status": "13",
                        "DateOfAddition": "20170228",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "007",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "0",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "Home Credit India Finance Pvt. Ltd",
                        "Terms_Frequency": "M",
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "7",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2017",
                                "Month": "06",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "05",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "02",
                                "Days_Past_Due": "5",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20170626",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFHOM2832",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": None,
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": "JHX4967212",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "0000????????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8750115572"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": "SCHOOL  MODINAGAR",
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "00  H.NO-85/8 MOHMMAD PUR KADEEM",
                            "Third_Line_Of_Address_non_normalized": "MOHMMAD PUR KADEEM NEAR BY SARKARI",
                            "Second_Line_Of_Address_non_normalized": "MODINAGAR GZB MODINAGAR H.NO-85/8"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "5799",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20170622",
                        "Date_Closed": "20180221",
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20180228",
                        "Account_Number": "XXXXXX3903",
                        "Account_Status": "13",
                        "DateOfAddition": "20170630",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "006",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "0",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "Home Credit India Finance Pvt. Ltd",
                        "Terms_Frequency": "M",
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "6",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2018",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2018",
                                "Month": "01",
                                "Days_Past_Due": "71",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "12",
                                "Days_Past_Due": "40",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "11",
                                "Days_Past_Due": "9",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "10",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "09",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "08",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "07",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2017",
                                "Month": "06",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20180220",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFHOM2832",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": None,
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": "JHX4967212",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "21000000????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8171039067"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": "PANCHAYAT GHAR  MODINAGAR",
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "H.N-85/8 MOHMMADPUR KADEEM PS-MODINAGAR",
                            "Third_Line_Of_Address_non_normalized": "PS-MODINAGAR NEAR GOVT SCHOOL &amp;",
                            "Second_Line_Of_Address_non_normalized": "GHAZIABAD MODINAGAR MOHMMADPUR KADEEM"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "6825",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20200827",
                        "Date_Closed": "20210508",
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20210508",
                        "Account_Number": "XXXXXXXXX2302",
                        "Account_Status": "13",
                        "DateOfAddition": "20200831",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": None,
                        "Amount_Past_Due": "0",
                        "Current_Balance": "0",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "DMI Finance Private Limited",
                        "Terms_Frequency": None,
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "0",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": "0",
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19741231",
                            "Income_TAX_PAN": "AJXPT0186G",
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "TYAGI VIKAS",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2021",
                                "Month": "05",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "03",
                                "Days_Past_Due": None,
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2020",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2020",
                                "Month": "11",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2020",
                                "Month": "10",
                                "Days_Past_Due": None,
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2020",
                                "Month": "09",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2020",
                                "Month": "08",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            }
                        ],
                        "Date_of_Last_Payment": "20210508",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFDMI2641",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": "0",
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "?S0000S00???????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": "0",
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": "DESH",
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "S/O: SATYAPRAKASH TYAGI,SIKRI KALAN,MOHA",
                            "Third_Line_Of_Address_non_normalized": "PRADESH,INDIA,201204 GHAZIABAD UTTAR PRA",
                            "Second_Line_Of_Address_non_normalized": "MMADPUR KADIM,MODINAGAR,GHAZIABAD,UTTAR"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "16672",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20210128",
                        "Date_Closed": "20211005",
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20211031",
                        "Account_Number": "XXXXXXXXX9995",
                        "Account_Status": "13",
                        "DateOfAddition": "20210131",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": None,
                        "Amount_Past_Due": "0",
                        "Current_Balance": "0",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "DMI Finance Private Limited",
                        "Terms_Frequency": None,
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "0",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800524",
                            "Income_TAX_PAN": "AJXPT0186G",
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "TYAGI VIKAS",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2021",
                                "Month": "10",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "08",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "07",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "06",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "05",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2021",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "S"
                            }
                        ],
                        "Date_of_Last_Payment": "20211005",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFDMI2641",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": "0",
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "?00000000???????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": "VIKASHTYAGIHHHHH@GMAIL.COM",
                            "FaxNumber": None,
                            "Telephone_Type": None,
                            "Telephone_Number": "919411635394",
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": None
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": "0",
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": "DESH",
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "S/O: SATYAPRAKASH TYAGI,SIKRI KALAN,MOHA",
                            "Third_Line_Of_Address_non_normalized": "PRADESH,INDIA,201204 GHAZIABAD UTTAR PRA",
                            "Second_Line_Of_Address_non_normalized": "MMADPUR KADIM,MODINAGAR,GHAZIABAD,UTTAR"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "15216",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20211111",
                        "Date_Closed": None,
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220430",
                        "Account_Number": "XXXXXXXXXX9858",
                        "Account_Status": "11",
                        "DateOfAddition": "20211130",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "012",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "3000",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "Bajaj Finserv",
                        "Terms_Frequency": "M",
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "12",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": [
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASTYAGI I",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            },
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASH TYAGI",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            }
                        ],
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "11",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20220301",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFBAJ1263",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "00000???????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8171039067"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": [
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM MAU MODINAGAR",
                                "Third_Line_Of_Address_non_normalized": "UTTAR PRADESH 201204",
                                "Second_Line_Of_Address_non_normalized": "MOHAMMADPUR SARKARI SCHOOL GHAZIABAD"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD UTTAR",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "PRADESH 201204"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD SARKARI",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "SCHOOL GHAZIABAD UTTAR PRADESH 201204"
                            }
                        ],
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "12000",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20211111",
                        "Date_Closed": None,
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220430",
                        "Account_Number": "XXXXXXXXXX8858",
                        "Account_Status": "11",
                        "DateOfAddition": "20211130",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "008",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "4125",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "Bajaj Finserv",
                        "Terms_Frequency": "M",
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "8",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": [
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASTYAGI I",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            },
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASH TYAGI",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            }
                        ],
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "11",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20220301",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFBAJ1263",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "00000???????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8171039067"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": [
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM MAU MODINAGAR",
                                "Third_Line_Of_Address_non_normalized": "UTTAR PRADESH 201204",
                                "Second_Line_Of_Address_non_normalized": "MOHAMMADPUR SARKARI SCHOOL GHAZIABAD"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD UTTAR",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "PRADESH 201204"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD SARKARI",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "SCHOOL GHAZIABAD UTTAR PRADESH 201204"
                            }
                        ],
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "11000",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Income": None,
                        "Open_Date": "20211110",
                        "Date_Closed": None,
                        "Account_Type": "13",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220430",
                        "Account_Number": "XXXX4187",
                        "Account_Status": "11",
                        "DateOfAddition": "20211130",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "036",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "62478",
                        "Occupation_Code": None,
                        "Special_Comment": None,
                        "Subscriber_Name": "IDFC FIRST BANK LIMITED",
                        "Terms_Frequency": "M",
                        "Income_Indicator": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "36",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": "AJXPT0186G",
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS  TYAGI",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "11",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20220402",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFFUCAP62",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "00000???????????????????????????????",
                        "SuitFiled_WilfulDefault": "00",
                        "CAIS_Holder_Phone_Details": [
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "02",
                                "Telephone_Number": "8171039067",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            },
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "03",
                                "Telephone_Number": "8171039067",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            },
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "02",
                                "Telephone_Number": "9411635394",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            },
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "00",
                                "Telephone_Number": "9411635394",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            },
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "01",
                                "Telephone_Number": None,
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": "8171039067"
                            },
                            {
                                "EMailId": "VIKAS.TYAGI1980@GMAIL.COM",
                                "FaxNumber": None,
                                "Telephone_Type": "00",
                                "Telephone_Number": "8171039067",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            }
                        ],
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Income_Frequency_Indicator": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": None,
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD 1449",
                            "Third_Line_Of_Address_non_normalized": None,
                            "Second_Line_Of_Address_non_normalized": "UTTAR PRADESH"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "70000",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Open_Date": "20211223",
                        "Date_Closed": None,
                        "Account_Type": "06",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220430",
                        "Account_Number": "XXXXXXXXXX5271",
                        "Account_Status": "11",
                        "DateOfAddition": "20211231",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "015",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "10963",
                        "Special_Comment": None,
                        "Subscriber_Name": "Bajaj Finserv",
                        "Terms_Frequency": "M",
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "15",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": [
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASTYAGI I",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            },
                            {
                                "Alias": None,
                                "Gender_Code": "1",
                                "Date_of_birth": "19800525",
                                "Income_TAX_PAN": "AJXPT0186G",
                                "Passport_Number": None,
                                "Voter_ID_Number": None,
                                "Surname_Non_Normalized": "VIKASH TYAGI",
                                "First_Name_Non_Normalized": None,
                                "Middle_Name_1_Non_Normalized": None,
                                "Middle_Name_2_Non_Normalized": None,
                                "Middle_Name_3_Non_Normalized": None
                            }
                        ],
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "04",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "01",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2021",
                                "Month": "12",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20220302",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "NBFBAJ1263",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "0000????????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8171039067"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": [
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM MAU MODINAGAR",
                                "Third_Line_Of_Address_non_normalized": "UTTAR PRADESH 201204",
                                "Second_Line_Of_Address_non_normalized": "MOHAMMADPUR SARKARI SCHOOL GHAZIABAD"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD UTTAR",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "PRADESH 201204"
                            },
                            {
                                "City_non_normalized": None,
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201204",
                                "Address_indicator_non_normalized": "02",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD SARKARI",
                                "Third_Line_Of_Address_non_normalized": None,
                                "Second_Line_Of_Address_non_normalized": "SCHOOL GHAZIABAD UTTAR PRADESH 201204"
                            }
                        ],
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "23499",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Open_Date": "20211116",
                        "Date_Closed": None,
                        "Account_Type": "10",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220430",
                        "Account_Number": "XXXXXXXXXXXX2564",
                        "Account_Status": "11",
                        "DateOfAddition": "20220228",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "R",
                        "Terms_Duration": None,
                        "Amount_Past_Due": "0",
                        "Current_Balance": "52254",
                        "Special_Comment": None,
                        "Subscriber_Name": "BOBCARDS LIMITED",
                        "Terms_Frequency": None,
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "0",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": "AJXPT0186G",
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS TYAGI",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": "50000",
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "04",
                                "Days_Past_Due": "11",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": "0",
                                "Asset_Classification": "?"
                            }
                        ],
                        "Date_of_Last_Payment": "20220312",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "51467",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "00??????????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": "TYAGIVIKAS7827@GMAIL.COM",
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "8171039067"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": None,
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "04",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD GHAZIABAD",
                            "Third_Line_Of_Address_non_normalized": None,
                            "Second_Line_Of_Address_non_normalized": "201204"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "53741",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Open_Date": "20220228",
                        "Date_Closed": "20220302",
                        "Account_Type": "00",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220331",
                        "Account_Number": "XXXXXXXXXX0542",
                        "Account_Status": "15",
                        "DateOfAddition": "20220228",
                        "Payment_Rating": "S",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "036",
                        "Amount_Past_Due": None,
                        "Current_Balance": "0",
                        "Special_Comment": None,
                        "Subscriber_Name": "Bank Of Baroda",
                        "Terms_Frequency": "M",
                        "Rate_of_Interest": "8.950",
                        "Repayment_Tenure": "36",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS",
                            "First_Name_Non_Normalized": "TYAGI",
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": [
                            {
                                "Year": "2022",
                                "Month": "03",
                                "Days_Past_Due": None,
                                "Asset_Classification": "S"
                            },
                            {
                                "Year": "2022",
                                "Month": "02",
                                "Days_Past_Due": None,
                                "Asset_Classification": "S"
                            }
                        ],
                        "Date_of_Last_Payment": None,
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "PUBBOB0006",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "S???????????????????????????????????",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": [
                            {
                                "EMailId": "tyagivikash7827@gmail.com",
                                "FaxNumber": None,
                                "Telephone_Type": "01",
                                "Telephone_Number": None,
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": "8171039067"
                            },
                            {
                                "EMailId": "tyagivikash7827@gmail.com",
                                "FaxNumber": None,
                                "Telephone_Type": "00",
                                "Telephone_Number": "8171039067",
                                "Telephone_Extension": None,
                                "Mobile_Telephone_Number": None
                            }
                        ],
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": None,
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": None,
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM  GHAZIABAD UTTAR PRADE",
                            "Third_Line_Of_Address_non_normalized": "DESH",
                            "Second_Line_Of_Address_non_normalized": "SHMOHAMMADPUR KADIM  GHAZIABAD UTTAR PRA"
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "195000",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Open_Date": "20140902",
                        "Date_Closed": None,
                        "Account_Type": "38",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220331",
                        "Account_Number": "XXXXXXXXXX2413",
                        "Account_Status": "11",
                        "DateOfAddition": "20220331",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": None,
                        "Amount_Past_Due": None,
                        "Current_Balance": "-187",
                        "Special_Comment": None,
                        "Subscriber_Name": "Canara Bank",
                        "Terms_Frequency": None,
                        "Rate_of_Interest": "16.000",
                        "Repayment_Tenure": "0",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS TYAGI",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": None,
                        "CAIS_Account_History": {
                            "Year": "2022",
                            "Month": "03",
                            "Days_Past_Due": "0",
                            "Asset_Classification": "S"
                        },
                        "Date_of_Last_Payment": "20220331",
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "PUBCANAR03",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": "AJXPT0186G",
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": "JHX3719135",
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "N",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": "tyagivikash7827@gmail.com",
                            "FaxNumber": None,
                            "Telephone_Type": "00",
                            "Telephone_Number": "918171039067",
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": None
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": None,
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": [
                            {
                                "City_non_normalized": "GHAZIABAD",
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201206",
                                "Address_indicator_non_normalized": "04",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "SO SATYAPRAKASH TYAGI",
                                "Third_Line_Of_Address_non_normalized": "MODINAGAR",
                                "Second_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM"
                            },
                            {
                                "City_non_normalized": "DIST GHAZIABAD",
                                "State_non_normalized": "09",
                                "CountryCode_non_normalized": "IB",
                                "Residence_code_non_normalized": None,
                                "ZIP_Postal_Code_non_normalized": "201206",
                                "Address_indicator_non_normalized": "04",
                                "Fifth_Line_Of_Address_non_normalized": None,
                                "First_Line_Of_Address_non_normalized": "MPUR KADDIM",
                                "Third_Line_Of_Address_non_normalized": "GHAZIABAD",
                                "Second_Line_Of_Address_non_normalized": "MODINAGAR"
                            }
                        ],
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "187",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    },
                    {
                        "Open_Date": "20220317",
                        "Date_Closed": None,
                        "Account_Type": "01",
                        "CurrencyCode": "INR",
                        "Date_Reported": "20220331",
                        "Account_Number": "XXXXXXXXXXX5565",
                        "Account_Status": "11",
                        "DateOfAddition": "20220331",
                        "Payment_Rating": "0",
                        "Portfolio_Type": "I",
                        "Terms_Duration": "084",
                        "Amount_Past_Due": "0",
                        "Current_Balance": "758091",
                        "Special_Comment": None,
                        "Subscriber_Name": "Axis Bank",
                        "Terms_Frequency": "M",
                        "Rate_of_Interest": None,
                        "Repayment_Tenure": "84",
                        "Consumer_comments": None,
                        "DefaultStatusDate": None,
                        "Settlement_Amount": None,
                        "Type_of_Collateral": None,
                        "WriteOffStatusDate": None,
                        "CAIS_Holder_Details": {
                            "Alias": None,
                            "Gender_Code": "1",
                            "Date_of_birth": "19800525",
                            "Income_TAX_PAN": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Surname_Non_Normalized": "VIKAS  TYAGI",
                            "First_Name_Non_Normalized": None,
                            "Middle_Name_1_Non_Normalized": None,
                            "Middle_Name_2_Non_Normalized": None,
                            "Middle_Name_3_Non_Normalized": None
                        },
                        "Credit_Limit_Amount": None,
                        "Subscriber_comments": None,
                        "Value_of_Collateral": "864044",
                        "CAIS_Account_History": {
                            "Year": "2022",
                            "Month": "03",
                            "Days_Past_Due": "0",
                            "Asset_Classification": "?"
                        },
                        "Date_of_Last_Payment": None,
                        "LitigationStatusDate": None,
                        "AccountHoldertypeCode": "1",
                        "Identification_Number": "PVTAXIS001",
                        "Promotional_Rate_Flag": None,
                        "Written_Off_Amt_Total": None,
                        "CAIS_Holder_ID_Details": {
                            "EMailId": None,
                            "Income_TAX_PAN": None,
                            "PAN_Issue_Date": None,
                            "Passport_Number": None,
                            "Voter_ID_Number": None,
                            "Ration_Card_Number": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Issue_Date": None,
                            "Universal_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Driver_License_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Universal_ID_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "Driver_License_Expiration_Date": None
                        },
                        "Payment_History_Profile": "N",
                        "SuitFiled_WilfulDefault": None,
                        "CAIS_Holder_Phone_Details": {
                            "EMailId": None,
                            "FaxNumber": None,
                            "Telephone_Type": "01",
                            "Telephone_Number": None,
                            "Telephone_Extension": None,
                            "Mobile_Telephone_Number": "9411635394"
                        },
                        "Date_of_First_Delinquency": None,
                        "Written_Off_Amt_Principal": "0",
                        "Original_Charge_Off_Amount": None,
                        "Written_off_Settled_Status": None,
                        "CAIS_Holder_Address_Details": {
                            "City_non_normalized": None,
                            "State_non_normalized": "09",
                            "CountryCode_non_normalized": "IB",
                            "Residence_code_non_normalized": None,
                            "ZIP_Postal_Code_non_normalized": "201204",
                            "Address_indicator_non_normalized": "02",
                            "Fifth_Line_Of_Address_non_normalized": None,
                            "First_Line_Of_Address_non_normalized": "MOHAMMADPUR KADIM GHAZIABAD",
                            "Third_Line_Of_Address_non_normalized": None,
                            "Second_Line_Of_Address_non_normalized": None
                        },
                        "Value_of_Credits_Last_Month": None,
                        "Scheduled_Monthly_Payment_Amount": None,
                        "Highest_Credit_or_Original_Loan_Amount": "758091",
                        "SuitFiledWillfulDefaultWrittenOffStatus": None
                    }
                ]
            },
            "Match_result": {
                "Exact_match": "Y"
            },
            "NonCreditCAPS": {
                "NonCreditCAPS_Summary": {
                    "NonCreditCAPSLast7Days": "0",
                    "NonCreditCAPSLast30Days": "0",
                    "NonCreditCAPSLast90Days": "0",
                    "NonCreditCAPSLast180Days": "0"
                }
            },
            "TotalCAPS_Summary": {
                "TotalCAPSLast7Days": "2",
                "TotalCAPSLast30Days": "2",
                "TotalCAPSLast90Days": "3",
                "TotalCAPSLast180Days": "3"
            },
            "CreditProfileHeader": {
                "Version": "V2.4",
                "ReportDate": "20220524",
                "ReportTime": "141952",
                "Subscriber": None,
                "ReportNumber": "1653382191390",
                "Subscriber_Name": "Bureau Disclosure Report with Credit Caps",
                "Enquiry_Username": "bureau_report__oto_capital"
            },
            "Current_Application": {
                "Current_Application_Details": {
                    "Enquiry_Reason": "6",
                    "Amount_Financed": "0",
                    "Finance_Purpose": None,
                    "Current_Other_Details": {
                        "Income": "0",
                        "Marital_Status": None,
                        "Employment_Status": None,
                        "Time_with_Employer": None,
                        "Number_of_Major_Credit_Card_Held": None
                    },
                    "Duration_Of_Agreement": "0",
                    "Current_Applicant_Details": {
                        "EMailId": "SK78290@GMAIL.COM",
                        "Last_Name": "TYAGI",
                        "First_Name": "VIKAS",
                        "Gender_Code": "1",
                        "IncomeTaxPan": "AJXPT0186G",
                        "Middle_Name1": None,
                        "Middle_Name2": None,
                        "Middle_Name3": None,
                        "PAN_Issue_Date": None,
                        "Telephone_Type": None,
                        "Passport_number": None,
                        "MobilePhoneNumber": "8171039067",
                        "Ration_Card_Number": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Issue_Date": None,
                        "Telephone_Extension": None,
                        "Universal_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Driver_License_Number": None,
                        "Voter_s_Identity_Card": None,
                        "Ration_Card_Issue_Date": None,
                        "Date_Of_Birth_Applicant": "19800525",
                        "Universal_ID_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Telephone_Number_Applicant_1st": None
                    },
                    "Current_Applicant_Address_Details": {
                        "City": "Ghaziabad",
                        "State": "09",
                        "PINCode": "201204",
                        "Landmark": None,
                        "Country_Code": "IB",
                        "BldgNoSocietyName": None,
                        "FlatNoPlotNoHouseNo": "MOHAMMADPUR",
                        "RoadNoNameAreaLocality": None
                    },
                    "Current_Applicant_Additional_AddressDetails": None
                }
            }
        }}
        return json_data

    def get_CAIS_Holder_Address_Details_address(self, CAIS_Holder_Address_Details):
        CAIS_Holder_Address_Details_address1 = ""
        CAIS_Holder_Address_Details_address2 = ""
        if CAIS_Holder_Address_Details:
            for CAIS_Holder_Address_Details_dict in CAIS_Holder_Address_Details:
                first_line_address = CAIS_Holder_Address_Details_dict.get("Fifth_Line_Of_Address_non_normalized")
                second_line_address = CAIS_Holder_Address_Details_dict.get("Second_Line_Of_Address_non_normalized")
                third_line_address = CAIS_Holder_Address_Details_dict.get("Third_Line_Of_Address_non_normalized")
                city = CAIS_Holder_Address_Details_dict.get("City_non_normalized")
                fifth_line_address = CAIS_Holder_Address_Details_dict.get("Fifth_Line_Of_Address_non_normalized")
                state = CAIS_Holder_Address_Details_dict.get("State_non_normalized")
                zip = CAIS_Holder_Address_Details_dict.get("ZIP_Postal_Code_non_normalized")
                country_code = CAIS_Holder_Address_Details_dict.get("CountryCode_non_normalized")
                landmark = CAIS_Holder_Address_Details_dict.get("Address_indicator_non_normalized")
                residence_code = CAIS_Holder_Address_Details_dict.get("Residence_code_non_normalized")
                pos = CAIS_Holder_Address_Details.index(CAIS_Holder_Address_Details_dict)
                if pos == 0:
                  CAIS_Holder_Address_Details_address1 = f"{first_line_address if first_line_address else ''} {second_line_address if second_line_address else ''} {third_line_address if third_line_address else ''} {city if city else ''} {fifth_line_address if fifth_line_address else ''} {state if state else ''} {zip if zip else ''} {country_code if country_code else ''} {landmark if landmark else ''} {residence_code if residence_code else ''}"
                else:
                  CAIS_Holder_Address_Details_address2 = f"{first_line_address if first_line_address else ''} {second_line_address if second_line_address else ''} {third_line_address if third_line_address else ''} {city if city else ''} {fifth_line_address if fifth_line_address else ''} {state if state else ''} {zip if zip else ''} {country_code if country_code else ''} {landmark if landmark else ''} {residence_code if residence_code else ''}"
        return CAIS_Holder_Address_Details_address1, CAIS_Holder_Address_Details_address2

    def get_credit_holder_phone_detail(self, CAIS_Holder_Phone_Details):
        phone_detail_dict1 = dict()
        phone_detail_dict2 = dict()
        if CAIS_Holder_Phone_Details:
            for cias_dolder_phone_detail in CAIS_Holder_Phone_Details:
                index = CAIS_Holder_Phone_Details.index(cias_dolder_phone_detail)
                if index == 0:
                    phone_detail_dict1 = dict(
                      email_address=cias_dolder_phone_detail.get("EMailId"),
                      consumer_mob1=cias_dolder_phone_detail.get("Mobile_Telephone_Number"),
                      consumer_extent1=cias_dolder_phone_detail.get("Telephone_Extension"),
                      consumer_ptype1=phone_type_dict.get(cias_dolder_phone_detail.get("Telephone_Type")),
                      consumer_pnum1=cias_dolder_phone_detail.get("Telephone_Number")
                    )
                else:
                    phone_detail_dict2 = dict(
                      # email_address=cias_dolder_phone_detail.get("EMailId"),
                      consumer_mob2=cias_dolder_phone_detail.get("Mobile_Telephone_Number"),
                      consumer_extent2=cias_dolder_phone_detail.get("Telephone_Extension"),
                      consumer_ptype2=phone_type_dict.get(cias_dolder_phone_detail.get("Telephone_Type")),
                      consumer_pnum2=cias_dolder_phone_detail.get("Telephone_Number")
                    )

        return phone_detail_dict1, phone_detail_dict2

    def get_caps_details(self, caps_application_detail):
        caps_application_data = []
        serial_number=0
        for caps_application_detail_dict in caps_application_detail:
            serial_number += 1
            caps_application_dict = dict(
              cr_enq=f"Cr Enq{serial_number}",
              ern=caps_application_detail_dict.get("ReportNumber"),
              application_date=caps_application_detail_dict.get("Date_of_Request"),
              credit_institution_name=caps_application_detail_dict.get("Subscriber_Name"),
              duration_of_agreement=caps_application_detail_dict.get("Duration_Of_Agreement"),
              amount_applied=caps_application_detail_dict.get("Amount_Financed"),
              date_of_birth=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Date_Of_Birth_Applicant"),
              telephone=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Telephone_Number_Applicant_1st"),
              pan=caps_application_detail_dict.get("CAPS_Applicant_Details").get("IncomeTaxPan"),
              passport_number=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Passport_number"),
              mobile_phone=caps_application_detail_dict.get("CAPS_Applicant_Details").get(""),
              voter_id=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Voter_s_Identity_Card"),
              gender=gender_dict.get(caps_application_detail_dict.get("CAPS_Applicant_Details").get("Gender_Code")),
              driving_license=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Driver_License_Number"),
              marital_status=marital_status_code.get(caps_application_detail_dict.get("CAPS_Other_Details").get("Marital_Status")),
              ration_card=caps_application_detail_dict.get("CAPS_Applicant_Details").get("Ration_Card_Number"),
              email=caps_application_detail_dict.get("CAPS_Applicant_Details").get("EMailId"),
              enquiry_reason=search_type_dict.get(caps_application_detail_dict.get("Enquiry_Reason")).get("value"),
              finance_purpose=search_type_dict.get(caps_application_detail_dict.get("Enquiry_Reason"), dict()
                                                   ).get("option", dict()).get(caps_application_detail_dict.get("Finance_Purpose"))
            )
            caps_application_data.append(caps_application_dict)
        return caps_application_data

    def get_cias_detail_data(self, credit_summary_details):
        try:
            credit_summary_details_list = []
            credit_accnt_information_details_list = []
            serial_no = 1

            for credit_summary_dict in credit_summary_details:
                account_type = account_type_code_dict.get(str(int(credit_summary_dict.get("Account_Type")))) if credit_summary_dict.get("Account_Type") else ""

                new_credit_summary_dict = dict(
                    serial_no=f"Acct {serial_no}",
                    credit_lender=credit_summary_dict.get("Subscriber_Name"),
                    credit_acctnum=credit_summary_dict.get("Account_Number"),
                    credit_type=account_type,
                    credit_dateopen=credit_summary_dict.get("Open_Date"),
                    credit_highest=credit_summary_dict.get("Highest_Credit_or_Original_Loan_Amount"),
                    credit_accnt_status=account_status_code.get(credit_summary_dict.get("Account_Status")),
                    credit_current_balance=credit_summary_dict.get("Current_Balance"),
                    credit_amt_overdue=credit_summary_dict.get("Amount_Past_Due"),
                    credit_date_reported=credit_summary_dict.get("Date_Reported"),
                    credit_sanct_highest=credit_summary_dict.get("Highest_Credit_or_Original_Loan_Amount"),
                    credit_datereported=credit_summary_dict.get("Date_Reported"),
                    credit_currentbalance=credit_summary_dict.get("Current_Balance"),
                    credit_opendate=credit_summary_dict.get("Open_Date"),
                    credit_accntstatus=account_status_code.get(credit_summary_dict.get("Account_Status")),
                    credit_ammntoverdue=credit_summary_dict.get("Amount_Past_Due"),
                    credit_ownership=account_holder_type_code.get(credit_summary_dict.get("AccountHoldertypeCode"))
                )

                credit_summary_details_list.append(new_credit_summary_dict)
                CAIS_Holder_Address_Details = credit_summary_dict.get("CAIS_Holder_Address_Details")
                CAIS_Holder_Details = credit_summary_dict.get("CAIS_Holder_Details")
                lname = ""
                fname = ""
                credit_holder_detail = dict()
                if CAIS_Holder_Details:
                    if isinstance(CAIS_Holder_Details, list):
                        lname = CAIS_Holder_Details[-1].get("Surname_Non_Normalized")
                        fname = CAIS_Holder_Details[-1].get("First_Name_Non_Normalized")
                        credit_holder_detail = dict(
                            consumer_dob=CAIS_Holder_Details[-1].get("Date_of_birth"),
                            consumer_gender=gender_dict.get(CAIS_Holder_Details[-1].get("Gender_Code")),
                            consumer_occupation=CAIS_Holder_Details[-1].get("Occupation_Code")
                        )
                        # CAIS_Holder_Address_Details = credit_summary_dict.get("CAIS_Holder_Address_Details")[-1]
                    else:
                        lname = CAIS_Holder_Details.get("Surname_Non_Normalized")
                        fname = CAIS_Holder_Details.get("First_Name_Non_Normalized")
                        credit_holder_detail = dict(
                            consumer_dob=CAIS_Holder_Details.get("Date_of_birth"),
                            consumer_gender=gender_dict.get(CAIS_Holder_Details.get("Gender_Code")),
                            consumer_occupation=CAIS_Holder_Details.get("Occupation_Code")
                        )
                    # CAIS_Holder_Address_Details = credit_summary_dict.get("CAIS_Holder_Address_Details")
                cais_address1 = ""
                cais_address2 = ""
                if CAIS_Holder_Address_Details:
                    if isinstance(CAIS_Holder_Address_Details, list):
                        cais_address1, cais_address2 = self.get_CAIS_Holder_Address_Details_address(CAIS_Holder_Address_Details)
                    else:
                        cais_address1, cais_address2 = self.get_CAIS_Holder_Address_Details_address([CAIS_Holder_Address_Details])

                # credit_holder_details = credit_summary_dict.get("CAIS_Holder_Details")

                CAIS_Holder_Phone_Details = credit_summary_dict.get("CAIS_Holder_Phone_Details")
                credit_holder_phone_detail1 = dict()
                credit_holder_phone_detail2 = dict()
                if CAIS_Holder_Phone_Details:
                    if isinstance(CAIS_Holder_Phone_Details, list):
                        credit_holder_phone_detail1, credit_holder_phone_detail2 = self.get_credit_holder_phone_detail(CAIS_Holder_Phone_Details)
                    else:
                        credit_holder_phone_detail1, credit_holder_phone_detail2 = self.get_credit_holder_phone_detail([CAIS_Holder_Phone_Details])

                header = dict(
                  credit_accounts=f"Acct {serial_no}",
                  bank_name=credit_summary_dict.get("Subscriber_Name"),
                  name=f"{lname if lname else ''} {fname if fname else ''}",
                  address1=cais_address1,
                  address2=cais_address2,
                  account_type=account_type
                )

                credit_account_details = dict(
                    credit_account_number=credit_summary_dict.get("Account_Number"),
                    credit_opendate=credit_summary_dict.get("Open_Date"),
                    credit_dateclose=credit_summary_dict.get("Date_Closed"),
                    credit_ownership=account_holder_type_code.get(credit_summary_dict.get("AccountHoldertypeCode")),
                    credit_voc=credit_summary_dict.get("Value_of_Collateral"),
                    credit_toc=credit_summary_dict.get("Type_of_Collateral"),
                    credit_roi=credit_summary_dict.get("Rate_of_Interest"),
                    suitfiled_wil_def_writeoff_status=account_status_code.get(credit_summary_dict.get("SuitFiledWillfulDefaultWrittenOffStatus")),
                    credit_written_status=account_status_code.get(credit_summary_dict.get("Written_off_Settled_Status")),
                    credit_date_reported=credit_summary_dict.get("Date_Reported"),
                    credit_loan_type=account_type,
                    credit_accnt_status=account_status_code.get(credit_summary_dict.get("Account_Status")),
                    credit_highest=credit_summary_dict.get("Highest_Credit_or_Original_Loan_Amount"),
                    credit_current_balance=credit_summary_dict.get("Current_Balance"),
                    credit_amt_overdue=credit_summary_dict.get("Amount_Past_Due"),
                    credit_last_paymt_date=credit_summary_dict.get("Date_of_Last_Payment"),
                    credit_willfull_default=account_status_code.get(credit_summary_dict.get("SuitFiled_WilfulDefault")),
                    credit_limit_amt=credit_summary_dict.get("Credit_Limit_Amount"),
                    credit_emi=credit_summary_dict.get("Scheduled_Monthly_Payment_Amount"),
                    credit_repay_tenure=credit_summary_dict.get("Repayment_Tenure"),
                    credit_total_writeoff_amt=credit_summary_dict.get("Written_Off_Amt_Total"),
                    credit_settlement_amt=credit_summary_dict.get("Settlement_Amount"),
                    credit_principle_writeoff=credit_summary_dict.get("Written_Off_Amt_Principal")
                )

                # credit_holder_detail = dict(
                #     consumer_dob=credit_holder_details.get("Date_of_birth"),
                #     consumer_gender=gender_dict.get(credit_holder_details.get("Gender_Code")),
                #     consumer_occupation=credit_holder_details.get("Occupation_Code")
                # )
                credit_holder_id_details = credit_summary_dict.get("CAIS_Holder_ID_Details")
                assert credit_holder_id_details is not None, "CAIS_Holder_ID_Details field missing"
                if isinstance(credit_holder_id_details, list):
                    credit_holder_id_details = credit_holder_id_details[-1]
                    credit_holderid_details = dict(
                        # pan
                        consumer_panid=credit_holder_id_details.get("Income_TAX_PAN"),
                        consumer_pan_doi=credit_holder_id_details.get("PAN_Issue_Date"),
                        consumer_pan_doe=credit_holder_id_details.get("PAN_Expiration_Date"),
                        # passport
                        consumer_passprtid=credit_holder_id_details.get("Passport_Number"),
                        consumer_passprt_doi=credit_holder_id_details.get("Passport_Issue_Date"),
                        consumer_passprt_doe=credit_holder_id_details.get("Passport_Expiration_Date"),
                        # voter id
                        consumer_voterid=credit_holder_id_details.get("Voter_ID_Number"),
                        consumer_voter_doi=credit_holder_id_details.get("Voter_ID_Issue_Date"),
                        consumer_voter_doe=credit_holder_id_details.get("Voter_ID_Expiration_Date"),
                        # uid
                        consumer_adhrid=credit_holder_id_details.get("Universal_ID_Number"),
                        consumer_adhr_doi=credit_holder_id_details.get("Universal_ID_Issue_Date"),
                        consumer_adhr_doe=credit_holder_id_details.get("Universal_ID_Expiration_Date"),
                        # driving license
                        consumer_drivinid=credit_holder_id_details.get("Driver_License_Number"),
                        consumer_drivin_doi=credit_holder_id_details.get("Driver_License_Issue_Date"),
                        consumer_drivin_doe=credit_holder_id_details.get("Driver_License_Expiration_Date"),
                        # ration card
                        consumer_rationid=credit_holder_id_details.get("Ration_Card_Number"),
                        consumer_ration_doi=credit_holder_id_details.get("Ration_Card_Issue_Date"),
                        consumer_ration_doe=credit_holder_id_details.get("Ration_Card_Expiration_Date")
                    )

                else:
                    credit_holderid_details = dict(
                        # pan
                        consumer_panid=credit_holder_id_details.get("Income_TAX_PAN"),
                        consumer_pan_doi=credit_holder_id_details.get("PAN_Issue_Date"),
                        consumer_pan_doe=credit_holder_id_details.get("PAN_Expiration_Date"),
                        # passport
                        consumer_passprtid=credit_holder_id_details.get("Passport_Number"),
                        consumer_passprt_doi=credit_holder_id_details.get("Passport_Issue_Date"),
                        consumer_passprt_doe=credit_holder_id_details.get("Passport_Expiration_Date"),
                        # voter id
                        consumer_voterid=credit_holder_id_details.get("Voter_ID_Number"),
                        consumer_voter_doi=credit_holder_id_details.get("Voter_ID_Issue_Date"),
                        consumer_voter_doe=credit_holder_id_details.get("Voter_ID_Expiration_Date"),
                        # uid
                        consumer_adhrid=credit_holder_id_details.get("Universal_ID_Number"),
                        consumer_adhr_doi=credit_holder_id_details.get("Universal_ID_Issue_Date"),
                        consumer_adhr_doe=credit_holder_id_details.get("Universal_ID_Expiration_Date"),
                        # driving license
                        consumer_drivinid=credit_holder_id_details.get("Driver_License_Number"),
                        consumer_drivin_doi=credit_holder_id_details.get("Driver_License_Issue_Date"),
                        consumer_drivin_doe=credit_holder_id_details.get("Driver_License_Expiration_Date"),
                        # ration card
                        consumer_rationid=credit_holder_id_details.get("Ration_Card_Number"),
                        consumer_ration_doi=credit_holder_id_details.get("Ration_Card_Issue_Date"),
                        consumer_ration_doe=credit_holder_id_details.get("Ration_Card_Expiration_Date")
                    )

                serial_no += 1

                # Payment History Data
                payment_history_data = credit_summary_dict.get("CAIS_Account_History")
                if isinstance(payment_history_data, list):
                  payment_history = self.get_payment_history(payment_history_data)
                else:
                  payment_history = self.get_payment_history([payment_history_data])


                # Account Review Data
                account_review_data = credit_summary_dict.get("Account_Review_Data")
                account_review = list()
                if account_review_data:
                    if isinstance(payment_history_data, list):
                      account_review = self.get_account_review_data(account_review_data)
                    else:
                      account_review = self.get_account_review_data([account_review_data])

                credit_accnt_information_details_dict = dict(header=header, credit_account_details=credit_account_details,
                                                             payment_history=payment_history,
                                                             credit_holder_detail=credit_holder_detail,
                                                             credit_holderid_details=credit_holderid_details,
                                                             consumer_details_credit_accnt=dict(**credit_holder_phone_detail1,
                                                                                                **credit_holder_phone_detail2),
                                                             account_review=account_review)
                credit_accnt_information_details_list.append(credit_accnt_information_details_dict)
            return credit_summary_details_list, credit_accnt_information_details_list
        except Exception as e:
            print(e.__str__())
            error_at = str('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            print(error_at)

    def get_display_date(self, dob):
        try:
            return datetime.datetime.strptime(dob, "%Y%m%d").strftime('%b %d,%Y')
        except Exception:
            return dob

    def convert_to_html_request(self, json_data):
        """
        Summary line.
        Extended description of json_data.

        Parameters:
        request_data = Description of INProfileResponse.
        Other parameters are taken within INProfileResponse,
        nested dictionaries.

        The variable for caps_credit_account still remains unknown.

        Parameters:
        CAPS_Summary -> Dictionary inside CAPS.
        And ViseVersa for all nested dictionaries inside their particular roles.

        """

        try:
            request_data = json_data.get("INProfileResponse")
            assert request_data is not None, "INProfileResponse field not found"
            # if request_data is None:
            #     raise Exception("INProfileResponse not found")
            score_dict = request_data.get("SCORE")
            assert score_dict is not None, "SCORE field not found"
            segment_dict = request_data.get("Segment")
            income_segment =income_segment_dict.get(segment_dict.get("Income_Segment")) if segment_dict and segment_dict.get("Income_Segment") else None
            credit_score = score_dict.get("BureauScore")
            assert credit_score is not None, "BureauScore field not found"
            credit_confid_level = score_dict.get("BureauScoreConfidLevel")
            credit_profile = request_data.get("CreditProfileHeader")
            experian_reportnum = credit_profile.get("ReportNumber")
            experian_report_created = self.get_display_date(credit_profile.get("ReportDate"))
            unique_transaction_id = credit_profile.get("UniqueID") if credit_profile.get("UniqueID") else ""
            credit_customer = request_data.get("Current_Application")
            current_application_details_v1 = credit_customer.get(
                "Current_Application_Details")
            current_applicant_details = current_application_details_v1.get(
                "Current_Applicant_Details")
            first_name = current_applicant_details.get("First_Name")
            last_name = current_applicant_details.get("Last_Name")
            customer_name = f"{first_name} {last_name}"
            gender = gender_dict.get(current_applicant_details.get("Gender_Code")) if current_applicant_details.get("Gender_Code") else ""
            mobile_number = current_applicant_details.get("MobilePhoneNumber")
            email_id = current_applicant_details.get("EMailId")
            passport = current_applicant_details.get("Passport_Number")
            voterid = current_applicant_details.get("Voter_s_Identity_Card")
            aadharid = current_applicant_details.get("Universal_ID_Number")
            telephone_num = current_applicant_details.get("Telephone_Number_Applicant_1st")
            driving_license = current_applicant_details.get("")
            date_of_birth = self.get_display_date(current_applicant_details.get("Date_Of_Birth_Applicant"))
            panid = current_applicant_details.get("IncomeTaxPan")
            ration_num = current_applicant_details.get("Ration_Card_Number")
            applicant_address_details = current_application_details_v1.get("Current_Applicant_Address_Details")
            city = applicant_address_details.get("City") if applicant_address_details.get("City") else ""
            state = applicant_address_details.get("State") if applicant_address_details.get("State") else ""
            pincode = applicant_address_details.get("PINCode") if applicant_address_details.get("PINCode") else ""
            landmark = applicant_address_details.get("Landmark") if applicant_address_details.get("Landmark") else ""
            country_code = applicant_address_details.get("Country_Code") if applicant_address_details.get("Country_Code") else ""
            society_name = applicant_address_details.get("BldgNoSocietyName") if applicant_address_details.get("BldgNoSocietyName") else ""
            house_no = applicant_address_details.get("FlatNoPlotNoHouseNo") if applicant_address_details.get("FlatNoPlotNoHouseNo") else ""
            locality = applicant_address_details.get("RoadNoNameAreaLocality") if applicant_address_details.get("RoadNoNameAreaLocality") else ""
            address = f"{house_no} {society_name} {locality} {city} {state} {pincode} {landmark}"

            cais_credit_account = request_data.get("CAIS_Account")
            assert cais_credit_account is not None, "CAIS_Account field not found"
            cais_credit_summary = cais_credit_account.get("CAIS_Summary")
            assert cais_credit_summary is not None, "CAIS_Summary field not found"

            credit_account_summary = cais_credit_summary.get("Credit_Account")

            caps_detail = request_data.get("CAPS", dict())
            credit_enquiry_summary = caps_detail.get("CAPS_Summary", dict())
            caps_application_detail = caps_detail.get("CAPS_Application_Details", list())

            cais_noncredit_account = request_data.get("NonCreditCAPS")
            noncredit_account_summary = cais_noncredit_account.get("NonCreditCAPS_Summary")
            current_bal_amt_summary = cais_credit_summary.get("Total_Outstanding_Balance")

            credit_summary_details = cais_credit_account.get("CAIS_Account_DETAILS")
            assert credit_summary_details is not None, "CAIS_Account_DETAILS field not found"

            credit_summary_details_list = list()
            credit_accnt_information_details_list = list()
            if credit_summary_details:
                if isinstance(credit_summary_details, list):
                    credit_summary_details_list, credit_accnt_information_details_list = self.get_cias_detail_data(credit_summary_details)
                else:
                    credit_summary_details_list, credit_accnt_information_details_list = self.get_cias_detail_data([credit_summary_details])

            if caps_application_detail:
                if isinstance(caps_application_detail, list):
                    records_found = len(caps_application_detail)
                    credit_enquiries_data = self.get_caps_details(caps_application_detail)
                else:
                    records_found = 1
                    credit_enquiries_data = self.get_caps_details([caps_application_detail])
            else:
                records_found = ""
                credit_enquiries_data = []

            credit_enquiry_dict = dict(records_found=records_found,
                                       credit_enquiries_data=credit_enquiries_data)

            context = {
                "experian_credit_score": {
                    "credit_score": credit_score,
                    "bureau_score_confid_level": credit_confid_level
                },
                "experian_credit_report": {
                    "experian_credit_ern": experian_reportnum,
                    "report_created": experian_report_created,
                    "unique_transaction_id": unique_transaction_id
                },
                "customer_detail": {
                    "customer_name": customer_name,
                    "mobile_no": mobile_number,
                    "email": email_id,
                    "address": address,
                    "dob": date_of_birth,
                    "pan": panid,
                    "gender": gender,
                    "passport": passport,
                    "voter_id": voterid,
                    "aadhar_id": aadharid,
                    "telephone": telephone_num,
                    "ration_no": ration_num

                },
                "report_summary": {
                    "total_credit": credit_account_summary.get("CreditAccountTotal"),
                    "active_credit": credit_account_summary.get("CreditAccountActive"),
                    "closed_credit": credit_account_summary.get("CreditAccountClosed"),
                    "settled_credit": credit_account_summary.get("CreditAccountDefault"),
                    "settled_current": credit_account_summary.get("CADSuitFiledCurrentBalance"),
                    "secured_current": current_bal_amt_summary.get("Outstanding_Balance_Secured"),
                    "unsecured_current": current_bal_amt_summary.get("Outstanding_Balance_UnSecured"),
                    "total_current": current_bal_amt_summary.get("Outstanding_Balance_All"),
                    "credit_inquiry_7": credit_enquiry_summary.get("CAPSLast7Days"),
                    "credit_inquiry_30": credit_enquiry_summary.get("CAPSLast30Days"),
                    "credit_inquiry_90": credit_enquiry_summary.get("CAPSLast90Days"),
                    "credit_inquiry_180": credit_enquiry_summary.get("CAPSLast180Days"),
                    "noncredit_inquiry_7": noncredit_account_summary.get("NonCreditCAPSLast7Days"),
                    "noncredit_inquiry_30": noncredit_account_summary.get("NonCreditCAPSLast30Days"),
                    "noncredit_inquiry_90": noncredit_account_summary.get("NonCreditCAPSLast90Days"),
                    "noncredit_inquiry_180": noncredit_account_summary.get("NonCreditCAPSLast180Days")

                },
                "summary_credit_accnts_info": credit_summary_details_list,
                "credit_accnt_information_details": credit_accnt_information_details_list,
                "credit_enquiry": credit_enquiry_dict,
                "income_segment": income_segment
            }

            return context
        except (Exception, AssertionError) as e:
            print(e.__str__())
            # print(repr(e))
            # print(e.args[0])
            # print(e)
            error_at = str('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            print(error_at)
            raise
            
            
            
###################################################################################################################################################################################



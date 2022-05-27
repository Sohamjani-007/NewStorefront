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
from store.enum import gender_dict, account_holder_type_code, marital_status_code, phone_type_dict, account_type_code_dict, account_status_code, search_type_dict



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
                month_name = datetime.datetime.strptime(
                    month, "%m").strftime("%b").lower()
                days_past_due = input_dict.get("Days_Past_Due")
                output_dict[str(month_name)] = days_past_due
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
                    output_data_dict[month_short_name] = "0"
            final_output.append(output_data_dict)
        return final_output

    def get_json_data(self):
        json_data = {
          "INProfileResponse": {
    "CAPS": {
      "CAPS_Summary": {
        "CAPSLast7Days": "0",
        "CAPSLast30Days": "0",
        "CAPSLast90Days": "0",
        "CAPSLast180Days": "0"
      }
    },
    "SCORE": {
      "BureauScore": "739",
      "BureauScoreConfidLevel": "H"
    },
    "Header": {
      "ReportDate": "20220520",
      "ReportTime": "192002",
      "SystemCode": "0",
      "MessageText": None
    },
    "Segment": {
      "Income_Segment": "02"
    },
    "UserMessage": {
      "UserMessageText": "Normal Response"
    },
    "CAIS_Account": {
      "CAIS_Summary": {
        "Credit_Account": {
          "CreditAccountTotal": "1",
          "CreditAccountActive": "1",
          "CreditAccountClosed": "0",
          "CreditAccountDefault": "0",
          "CADSuitFiledCurrentBalance": "0"
        },
        "Total_Outstanding_Balance": {
          "Outstanding_Balance_All": "92100",
          "Outstanding_Balance_Secured": "0",
          "Outstanding_Balance_UnSecured": "92100",
          "Outstanding_Balance_Secured_Percentage": "0",
          "Outstanding_Balance_UnSecured_Percentage": "100"
        }
      },
      "CAIS_Account_DETAILS": {
        "Income": None,
        "Open_Date": "20181230",
        "Date_Closed": None,
        "Account_Type": "05",
        "CurrencyCode": "INR",
        "Date_Reported": "20220410",
        "Account_Number": "IPZOD21922",
        "Account_Status": "11",
        "DateOfAddition": "20220210",
        "Payment_Rating": "?",
        "Portfolio_Type": "I",
        "Terms_Duration": None,
        "Amount_Past_Due": "2000",
        "Current_Balance": "92100",
        "Occupation_Code": None,
        "Special_Comment": None,
        "Subscriber_Name": "XXXX",
        "Terms_Frequency": None,
        "Income_Indicator": None,
        "Rate_of_Interest": None,
        "Repayment_Tenure": "0",
        "Consumer_comments": None,
        "DefaultStatusDate": None,
        "Settlement_Amount": None,
        "Type_of_Collateral": None,
        "WriteOffStatusDate": None,
        "Account_Review_Data": [
          {
            "Year": "2022",
            "Month": "4",
            "Cash_Limit": None,
            "EMI_Amount": None,
            "Account_Status": None,
            "Amount_Past_Due": "2000",
            "Current_Balance": "92100",
            "Credit_Limit_Amount": "76000",
            "Actual_Payment_Amount": None
          },
          {
            "Year": "2022",
            "Month": "3",
            "Cash_Limit": None,
            "EMI_Amount": None,
            "Account_Status": None,
            "Amount_Past_Due": "2000",
            "Current_Balance": "92100",
            "Credit_Limit_Amount": "76000",
            "Actual_Payment_Amount": None
          },
          {
            "Year": "2022",
            "Month": "2",
            "Cash_Limit": None,
            "EMI_Amount": None,
            "Account_Status": None,
            "Amount_Past_Due": "2000",
            "Current_Balance": "92100",
            "Credit_Limit_Amount": "76000",
            "Actual_Payment_Amount": None
          }
        ],
        "CAIS_Holder_Details": {
          "Alias": None,
          "Gender_Code": "1",
          "Date_of_birth": "19830321",
          "Income_TAX_PAN": "ABCPS4872K",
          "Passport_Number": None,
          "Voter_ID_Number": None,
          "Surname_Non_Normalized": "RAHUL",
          "First_Name_Non_Normalized": "SANORIA",
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
            "Days_Past_Due": "55",
            "Asset_Classification": "?"
          },
          {
            "Year": "2022",
            "Month": "03",
            "Days_Past_Due": "72",
            "Asset_Classification": "?"
          },
          {
            "Year": "2022",
            "Month": "02",
            "Days_Past_Due": "69",
            "Asset_Classification": "?"
          }
        ],
        "Date_of_Last_Payment": None,
        "LitigationStatusDate": None,
        "AccountHoldertypeCode": "1",
        "Identification_Number": "OTHBP03090011",
        "Promotional_Rate_Flag": None,
        "Written_Off_Amt_Total": None,
        "CAIS_Holder_ID_Details": {
          "EMailId": "RXXXXXXXXXXXA@OXXXXXXXXX.IN",
          "Income_TAX_PAN": "ABCPS4872K",
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
        "Payment_History_Profile": "????????????????????????????????????",
        "CAIS_Holder_Phone_Details": {
          "EMailId": "RXXXXXXXXXXXA@OXXXXXXXXX.IN",
          "FaxNumber": None,
          "Telephone_Type": None,
          "Telephone_Number": "XXXXXX6550",
          "Telephone_Extension": None,
          "Mobile_Telephone_Number": None
        },
        "Date_of_First_Delinquency": None,
        "Written_Off_Amt_Principal": None,
        "Income_Frequency_Indicator": None,
        "Original_Charge_Off_Amount": None,
        "Written_off_Settled_Status": None,
        "CAIS_Holder_Address_Details": {
          "City_non_normalized": "MUMBAI",
          "State_non_normalized": "27",
          "CountryCode_non_normalized": "IB",
          "Residence_code_non_normalized": None,
          "ZIP_Postal_Code_non_normalized": "400066",
          "Address_indicator_non_normalized": None,
          "Fifth_Line_Of_Address_non_normalized": None,
          "First_Line_Of_Address_non_normalized": "ASHOK VAN",
          "Third_Line_Of_Address_non_normalized": None,
          "Second_Line_Of_Address_non_normalized": "S V ROAD"
        },
        "Value_of_Credits_Last_Month": None,
        "Scheduled_Monthly_Payment_Amount": None,
        "Highest_Credit_or_Original_Loan_Amount": "76000",
        "SuitFiledWillfulDefaultWrittenOffStatus": None
      }
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
      "TotalCAPSLast7Days": "0",
      "TotalCAPSLast30Days": "0",
      "TotalCAPSLast90Days": "0",
      "TotalCAPSLast180Days": "0"
    },
    "CreditProfileHeader": {
      "Version": "V2.4",
      "ReportDate": "20220520",
      "ReportTime": "192002",
      "Subscriber": None,
      "ReportNumber": "1653054602458",
      "Subscriber_Name": "Bureau Disclosure Report with Residence Stability Score",
      "Enquiry_Username": "rss2ecv_uat",
      "CustomerReferenceID": None
    },
    "Current_Application": {
      "Current_Application_Details": {
        "Enquiry_Reason": "6",
        "Amount_Financed": "0",
        "Finance_Purpose": "99",
        "Current_Other_Details": {
          "Income": "0",
          "Marital_Status": None,
          "Employment_Status": None,
          "Time_with_Employer": None,
          "Number_of_Major_Credit_Card_Held": None
        },
        "Duration_Of_Agreement": "0",
        "Current_Applicant_Details": {
          "EMailId": "rahul.sanoria@otocapital.in",
          "Last_Name": "sanoria",
          "First_Name": "Rahul",
          "Gender_Code": "1",
          "IncomeTaxPan": "ABCPS4872K",
          "Middle_Name1": None,
          "Middle_Name2": None,
          "Middle_Name3": None,
          "PAN_Issue_Date": None,
          "Telephone_Type": None,
          "MobilePhoneNumber": "9459166550",
          "Ration_Card_Number": None,
          "PAN_Expiration_Date": None,
          "Passport_Issue_Date": None,
          "Telephone_Extension": None,
          "Universal_ID_Number": None,
          "Voter_ID_Issue_Date": None,
          "Driver_License_Number": None,
          "Voter_s_Identity_Card": None,
          "Ration_Card_Issue_Date": None,
          "Date_Of_Birth_Applicant": "19990125",
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
          "City": "MUMBAI",
          "State": "27",
          "PINCode": "400066",
          "Landmark": None,
          "Country_Code": "IB",
          "BldgNoSocietyName": None,
          "FlatNoPlotNoHouseNo": "Ashok Van Nehru Rd",
          "RoadNoNameAreaLocality": None
        },
        "Current_Applicant_Additional_AddressDetails": None
      }
    }
  }
        }
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
                residence_code = CAIS_Holder_Address_Details_dict.get("Residence_code_non_normaized")
                pos = CAIS_Holder_Address_Details.index(CAIS_Holder_Address_Details_dict) # this is index in dictionary  # index()= [list]index('soham') --> output --> 4
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
                      email_address = cias_dolder_phone_detail.get("EMailId"),
                      consumer_mob1 = cias_dolder_phone_detail.get("Mobile_Telephone_Number"),
                      consumer_extent1 = cias_dolder_phone_detail.get("Telephone_Extension"),
                      consumer_ptype1 = phone_type_dict.get(cias_dolder_phone_detail.get("Telephone_Type")),
                      consumer_pnum1=cias_dolder_phone_detail.get("Telephone_Number")
                    )
                else:
                    phone_detail_dict2 = dict(
                      email_address=cias_dolder_phone_detail.get("EMailId"),
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
            
            lname = credit_summary_dict.get("CAIS_Holder_Details").get("Surname_Non_Normalized")
            fname = credit_summary_dict.get("CAIS_Holder_Details").get("First_Name_Non_Normalized")
            CAIS_Holder_Address_Details = credit_summary_dict.get("CAIS_Holder_Address_Details")

            if isinstance(CAIS_Holder_Address_Details, list):
                cais_address1, cais_address2 = self.get_CAIS_Holder_Address_Details_address(CAIS_Holder_Address_Details)
            else:
                cais_address1, cais_address2 = self.get_CAIS_Holder_Address_Details_address([CAIS_Holder_Address_Details])

            credit_holder_details = credit_summary_dict.get("CAIS_Holder_Details")
            credit_holder_id_details = credit_summary_dict.get("CAIS_Holder_ID_Details")
            CAIS_Holder_Phone_Details = credit_summary_dict.get("CAIS_Holder_Phone_Details")

            if isinstance(CAIS_Holder_Phone_Details, list):
                credit_holder_phone_detail1, credit_holder_phone_detail2 = self.get_credit_holder_phone_detail(
                  CAIS_Holder_Phone_Details)
            else:
                credit_holder_phone_detail1, credit_holder_phone_detail2 = self.get_credit_holder_phone_detail(
                  [CAIS_Holder_Phone_Details])

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
                credit_accnt_status=account_status_code.get(account_status_code.get(credit_summary_dict.get("Account_Status"))),
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

            credit_holder_detail = dict(
                consumer_dob=credit_holder_details.get("Date_of_birth"),
                consumer_gender=gender_dict.get(credit_holder_details.get("Gender_Code")),
                consumer_occupation=credit_holder_details.get("Occupation_Code")
            )

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

            credit_accnt_information_details_dict = dict(header=header, credit_account_details=credit_account_details,
                                                         payment_history=payment_history,
                                                         credit_holder_detail=credit_holder_detail,
                                                         credit_holderid_details=credit_holderid_details,
                                                         consumer_details_credit_accnt=dict(**credit_holder_phone_detail1,
                                                                                            **credit_holder_phone_detail2)) # ????
            credit_accnt_information_details_list.append(credit_accnt_information_details_dict)
        return credit_summary_details_list, credit_accnt_information_details_list
              
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
        request_data = json_data.get("INProfileResponse")
        score_dict = request_data.get("SCORE")
        credit_score = score_dict.get("BureauScore")
        credit_confid_level = score_dict.get("BureauScoreConfidLevel")
        credit_profile = request_data.get("CreditProfileHeader")
        experian_reportnum = credit_profile.get("ReportNumber")
        experian_report_created = credit_profile.get("ReportDate")
        unique_transaction_id = credit_profile.get("UniqueID")
        credit_customer = request_data.get("Current_Application")
        current_application_details_v1 = credit_customer.get("Current_Application_Details")
        current_applicant_details = current_application_details_v1.get("Current_Applicant_Details")
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
        date_of_birth = current_applicant_details.get("Date_Of_Birth_Applicant")
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
        cais_credit_summary = cais_credit_account.get("CAIS_Summary")

        credit_account_summary = cais_credit_summary.get("Credit_Account")

        caps_detail = request_data.get("CAPS", dict())
        credit_enquiry_summary = caps_detail.get("CAPS_Summary", dict())
        caps_application_detail = caps_detail.get("CAPS_Application_Details", list())

        cais_noncredit_account = request_data.get("NonCreditCAPS")
        noncredit_account_summary = cais_noncredit_account.get("NonCreditCAPS_Summary")
        current_bal_amt_summary = cais_credit_summary.get("Total_Outstanding_Balance")

        credit_summary_details = cais_credit_account.get("CAIS_Account_DETAILS")
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

        credit_enquiry_dict = dict(records_found=records_found, credit_enquiries_data=credit_enquiries_data)

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
                "settled_credit": credit_account_summary.get("CADSuitFiledCurrentBalance"),
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
            "credit_enquiry": credit_enquiry_dict
        }

        return context



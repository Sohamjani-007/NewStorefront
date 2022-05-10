from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def storage(request):
    context = {
        "experian_credit_report": {
            "experian_credit_ern": "10107",
            "unique_transaction_id": "test_unique_id",
            "report_created": "test_created_report"},
        "customer_detail": {
            "name": "given_name", 
            "address1": "address",
            "dob": "dob",
            "pan": "pan",
            "gender": "gender",
            "email": "email",
            "passport": "passport",
            "voter_id": "voterid",
            "aadhar_id": "aadharid",
            "telephone": "tele",
            "mobile_no": "mobile",
            "driving_license": "driving(license)",
            "ration_no": "ration card"
        },
        "experian_credit_score": {
            "bureau_score_confid_level" : 334,
            "credit_score": 786
        },
        "report_summary": {
            "total_credit": "1000", 
            "active_credit": "200",
            "closed_credit": "11",
            "settled_credit": "12",
            "total_currnt": "13",
            "settled_currnt": "14",
            "secured_currnt": "15",
            "unsecured_currnt": "16",
            "credit_inquiry_7": "inquiry_7",
            "credit_inquiry_30": "credit_30",
            "credit_inquiry_90": "credit_90",
            "credit_inquiry_180": "credit_180",
            "noncredit_inquiry_7": "noncredit_7",
            "noncredit_inquiry_30": "noncredit_30",
            "noncredit_inquiry_90": "noncredit_90",
            "noncredit_inquiry_180": "noncredit_180"
        },
        "summary_credit_accnts_info": [{"accounts": "one", "credit_lender": "Lender Approved", "credit_type": "CREDIT CARD", "credit_acctnum": "XXX234", "credit_ownership": "Individual",
                                        "credit_datereported": "12-2-2022", "credit_accntstatus": "wd/wo/settled", "credit_opendate": "22-1-20",
                                        "credit_sanct_highest": "50,000", "credit_currentbalance": "1,21,000", "credit_ammntoverdue": "2,341"},

                                       {"accounts": "two", "credit_lender": "Pending", "credit_type": "CREDIT CARD", "credit_acctnum": "XXXX987", "credit_ownership": "Individual",
                                        "credit_datereported": "12-3-2022", "credit_accntstatus": "Pending", "credit_opendate": "12-3-2022",
                                        "credit_sanct_highest": "20,000", "credit_currentbalance": "10,000", "credit_ammntoverdue": "0"}],
                                        
        "credit_accnt_information_details": [
            {
            "header": {"credit_accounts": "Acct 1", "bank_name": "Indian Bank", "name": "Jos Butler", "address1": " England"},
            "credit_account_details":   
            {"credit_account_number": "12345", # Account Number	
             "credit_dateopen": "23-12-2019", # Date Opened	
             "credit_dateclose": "12-3-2021",# Date Closed	new_credit_cais_dict
             "credit_ownership": "Individual", # Ownership X FIND IT new_credit_cais_dict
             "credit_roi": "9000",# Rate of Interest	new_credit_cais_dict
             "credit_voc": "None",# Value of Collateral	new_credit_cais_dict
             "credit_toc": "none",# Type of Collateral	new_credit_cais_dict
             "suitfiled_wil_def_writeoff_status": "20000", # SuitFiled Willful Default WrittenOff Status	new_credit_cais_dict
             "credit_date_reported": "21-4-2021",# Date Reported	new_credit_cais_dict
             "credit_loan_type": "CREDIT CARD",# Loan Type	
             "credit_accnt_status": "SD/WO/WD/SETTLED", # Account Status	
             "credit_highest": "50,000", # Highest Credit	
             "credit_current_balance": "12,000", # Current Balance	
             "credit_amt_overdue": "2,450",# Amount Overdue	
             "credit_last_paymt_date": "16-3-2020", # Last Payment Date	new_credit_cais_dict
             "credit_willfull_default": "None", # SuitFiled Willful Default	new_credit_cais_dict
             "credit_limit_amt": "2000", # Credit Limit Amt new_credit_cais_dict
             "credit_emi": "7000", # EMI new_credit_cais_dict
             "credit_repay_tenure": "1200",# Repayment Tenure	new_credit_cais_dict
             "credit_total_writeoff_amt": "4000", # Total Write-off Amt	new_credit_cais_dict
             "credit_principle_writeoff": "500", # Principal Write-off	new_credit_cais_dict
             "credit_settlement_amt": "3000",# Settlement Amt	new_credit_cais_dict
             "credit_written_status": "None" # Written off Settled Status	new_credit_cais_dict
             },
            "payment_history": [{
                "year": "2011",
                "description": "Days Past Due",
                        "dec": "dec1",
                        "nov": "nov1",
                        "oct": "oct1",
                        "sep": "sep1",
                        "aug": "aug1",
                        "jul": "jul1",
                        "jun": "jun1",
                        "may": "may1",
                        "apr": "apr1",
                        "mar": "mar1",
                        "feb": "feb1",
                        "jan": "jan1"
            },
                {
                "year": "2012",
                "description": "Outstanding Amount",
                        "dec": "dec1",
                        "nov": "nov1",
                        "oct": "oct1",
                        "sep": "sep1",
                        "aug": "aug1",
                        "jul": "jul1",
                        "jun": "jun1",
                        "may": "may1",
                        "apr": "apr1",
                        "mar": "mar1",
                        "feb": "feb1",
                        "jan": "jan1"
            }
            ],
            "consumer_details_credit_accnt": {
                "consumer_dob": "test_consum_dob",
                "consumer_gender": "test_consum_gender",
                "consumer_occupation": "test_occ",
                "consumer_address": "test_add",
                "consumer_mob1": "Mobile number 1",
                "consumer_mob2": "Mobile number 2",
                "consumer_ptype1": "Phone",
                "consumer_pnum1": "Phone number 1",
                "consumer_extent1": "Extension +12",
                "consumer_extent2": "Extension +91",
                "consumer_ptype2": "Laptop",
                "consumer_pnum2": "Mails",   
                "consumer_panid": "test_pnid",
                "consumer_pan_doi": "test_pndoi",
                "consumer_pan_doe": "test_pndoe",
                "consumer_passprtid": "test_pasid",
                "consumer_passprt_doi": "test_pasdoi",
                "consumer_passprt_doe": "test_pasdoe",
                "consumer_voterid": "test_vid",
                "consumer_voter_doi": "test_vdoi",
                "consumer_voter_doe": "test_vdoe",
                "consumer_adhrid": "test_adhrid",
                "consumer_adhr_doi": "test_adhrdoi",
                "consumer_adhr_doe": "test_adhrdoe",
                "consumer_drivinid": "test_drivid",
                "consumer_drivin_doi": "test_drivdoi",
                "consumer_drivin_doe": "test_drivdoe",
                "consumer_rationid": "test_ratnid",
                "consumer_ration_doi": "test_ratndoi",
                "consumer_ration_doe": "test_ratndoe"
            }
        }],
        "credit_enquiries": [{
            "cr_enq": "CR ENQ 1",
            "records_found": "No records found",
            "address1": "Chester Road, NY, PIN-909",
            "date_of_birth": "31-10-1988",
            "pan": "GJSJUY75",
            "ern": "5627",
            "telephone": "+1288748920",
            "passport_number": "JTNM542256",
            "search_type": "Mobile",
            "mobile_phone": "+41399377289",
            "voter_id": "124424",
            "credit_institution_name": "ICC",
            "gender": "MALE",
            "driving_license": "YES",
            "application_date": "14-9-2019",
            "marital_status": "MARRIED",
            "ration_card": "YES",
            "amount_applied": "50,000",
            "email": "butler.jos@foxmail.io",
            "duration_of_agreement": "16-12-2022"
        },
            {
            "cr_enq": "CR ENQ 2",
            "records_found": "1122",
            "address1": "test_add22",
            "date_of_birth": "test_dob",
            "pan": "test_pan",
            "ern": "test_ern",
            "telephone": "test_tele",
            "passport_number": "test_passnum",
            "search_type": "test_type",
            "mobile_phone": "test_mobile",
            "voter_id": "test_id",
            "credit_institution_name": "test_institute_name",
            "gender": "test_gender",
            "driving_license": "test_drive_license",
            "application_date": "test_apl_date",
            "marital_status": "test_marital",
            "ration_card": "test_ration_card",
            "amount_applied": "test_amount_applied",
            "email": "test_email",
            "duration_of_agreement": "test_duration"
        }],
        "non_credit_enquiries": [{
            "records_found": "test_records"
        },
            {
            "records_found": "test1212_records"
        }]

    }
    return render(request, 'test.html', context)

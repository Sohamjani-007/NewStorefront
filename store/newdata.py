import json
from multiprocessing import context
from telnetlib import PRAGMA_HEARTBEAT
import xmltodict
from store.views import storage
import datetime
import calendar


def get_json_data():
    xml_data = """<INProfileResponse>
    <Header>
    <SystemCode>0</SystemCode>
    <MessageText/>
    <ReportDate>20210107</ReportDate>
    <ReportTime>174310</ReportTime>
    </Header>
    <UserMessage>
    <UserMessageText>Normal Response</UserMessageText>
    </UserMessage>
    <CreditProfileHeader>
    <Enquiry_Username>cpu2ecv_uat</Enquiry_Username>
    <ReportDate>20210107</ReportDate>
    <ReportTime>174310</ReportTime>
    <Version>V2.4</Version>
    <ReportNumber>1610021590114</ReportNumber>
    <Subscriber/>
    <Subscriber_Name>Bureau Disclosure Report with Income Segmentation</Subscriber_Name>
    <CustomerReferenceID/>
    </CreditProfileHeader>
    <Current_Application>
    <Current_Application_Details>
    <Enquiry_Reason>6</Enquiry_Reason>
    <Finance_Purpose>99</Finance_Purpose>
    <Amount_Financed>0</Amount_Financed>
    <Duration_Of_Agreement>0</Duration_Of_Agreement>
    <Current_Applicant_Details>
    <Last_Name>Raut</Last_Name>
    <First_Name>Darshan</First_Name>
    <Middle_Name1/>
    <Middle_Name2/>
    <Middle_Name3/>
    <Gender_Code>2</Gender_Code>
    <IncomeTaxPan>BQGPM4004M</IncomeTaxPan>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_s_Identity_Card/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <Date_Of_Birth_Applicant>19850910</Date_Of_Birth_Applicant>
    <Telephone_Number_Applicant_1st/>
    <Telephone_Extension/>
    <Telephone_Type/>
    <MobilePhoneNumber>9987217355</MobilePhoneNumber>
    <EMailId>umesh.jawarkar@experian.com</EMailId>
    </Current_Applicant_Details>
    <Current_Other_Details>
    <Income>0</Income>
    <Marital_Status/>
    <Employment_Status/>
    <Time_with_Employer/>
    <Number_of_Major_Credit_Card_Held/>
    </Current_Other_Details>
    <Current_Applicant_Address_Details>
    <FlatNoPlotNoHouseNo>A-1 106</FlatNoPlotNoHouseNo>
    <BldgNoSocietyName/>
    <RoadNoNameAreaLocality/>
    <City>Mumbai</City>
    <Landmark/>
    <State>27</State>
    <PINCode>400075</PINCode>
    <Country_Code>IB</Country_Code>
    </Current_Applicant_Address_Details>
    <Current_Applicant_Additional_AddressDetails/>
    </Current_Application_Details>
    </Current_Application>
    <CAIS_Account>
    <CAIS_Summary>
    <Credit_Account>
    <CreditAccountTotal>8</CreditAccountTotal>
    <CreditAccountActive>7</CreditAccountActive>
    <CreditAccountDefault>0</CreditAccountDefault>
    <CreditAccountClosed>1</CreditAccountClosed>
    <CADSuitFiledCurrentBalance>0</CADSuitFiledCurrentBalance>
    </Credit_Account>
    <Total_Outstanding_Balance>
    <Outstanding_Balance_Secured>195000</Outstanding_Balance_Secured>
    <Outstanding_Balance_Secured_Percentage>53</Outstanding_Balance_Secured_Percentage>
    <Outstanding_Balance_UnSecured>171300</Outstanding_Balance_UnSecured>
    <Outstanding_Balance_UnSecured_Percentage>47</Outstanding_Balance_UnSecured_Percentage>
    <Outstanding_Balance_All>366300</Outstanding_Balance_All>
    </Total_Outstanding_Balance>
    </CAIS_Summary>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHBP03090001</Identification_Number>
    <Subscriber_Name> icicibank</Subscriber_Name>
    <Account_Number>ICICI213220</Account_Number>
    <Portfolio_Type>R</Portfolio_Type>
    <Account_Type>10</Account_Type>
    <Open_Date>19980522</Open_Date>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>53</Account_Status>
    <Payment_Rating>0</Payment_Rating>
    <Payment_History_Profile>N</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>121000</Current_Balance>
    <Amount_Past_Due>2350</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20180315</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status>00</Written_off_Settled_Status>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20180315</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>14</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId/>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId/>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>2500</Actual_Payment_Amount>
    <Current_Balance>121000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>2350</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>FORFORAMEX005</Identification_Number>
    <Subscriber_Name>American Express Banking Corp</Subscriber_Name>
    <Account_Number>AMEX8130496</Account_Number>
    <Portfolio_Type>R</Portfolio_Type>
    <Account_Type>10</Account_Type>
    <Open_Date>19971013</Open_Date>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Highest_Credit_or_Original_Loan_Amount>10000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>53</Account_Status>
    <Payment_Rating>6</Payment_Rating>
    <Payment_History_Profile>6???????????????????????????????????</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>300</Current_Balance>
    <Amount_Past_Due>250000</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20190611</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status>00</Written_off_Settled_Status>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20190511</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>06</Month>
    <Days_Past_Due>450</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>05</Month>
    <Days_Past_Due>450</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId/>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>6</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>9002</Actual_Payment_Amount>
    <Current_Balance>300</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>250000</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>5</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>9002</Actual_Payment_Amount>
    <Current_Balance>301</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>36000</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>FORFORAMEX005</Identification_Number>
    <Subscriber_Name>American Express Banking Corp</Subscriber_Name>
    <Account_Number>AMEX8130497</Account_Number>
    <Portfolio_Type>I</Portfolio_Type>
    <Account_Type>05</Account_Type>
    <Open_Date>19910120</Open_Date>
    <Credit_Limit_Amount/>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>82</Account_Status>
    <Payment_Rating>4</Payment_Rating>
    <Payment_History_Profile>N</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>30000</Current_Balance>
    <Amount_Past_Due>1000</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20180311</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status/>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20180311</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>140</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>82</Account_Status>
    <Actual_Payment_Amount>1800</Actual_Payment_Amount>
    <Current_Balance>30000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>1000</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHNone</Identification_Number>
    <Subscriber_Name>SBI Cards and Payment Services Private Limited</Subscriber_Name>
    <Account_Number>SBIC8130496</Account_Number>
    <Portfolio_Type>R</Portfolio_Type>
    <Account_Type>10</Account_Type>
    <Open_Date>19910314</Open_Date>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>82</Account_Status>
    <Payment_Rating>4</Payment_Rating>
    <Payment_History_Profile>N</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>20000</Current_Balance>
    <Amount_Past_Due>900</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20180311</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status/>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20180311</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>130</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>82</Account_Status>
    <Actual_Payment_Amount>800</Actual_Payment_Amount>
    <Current_Balance>20000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>900</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHNone</Identification_Number>
    <Subscriber_Name>SBI Cards and Payment Services Private Limited</Subscriber_Name>
    <Account_Number>SBIC8130497</Account_Number>
    <Portfolio_Type>I</Portfolio_Type>
    <Account_Type>01</Account_Type>
    <Open_Date>19910120</Open_Date>
    <Credit_Limit_Amount/>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>82</Account_Status>
    <Payment_Rating>4</Payment_Rating>
    <Payment_History_Profile>N</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>30000</Current_Balance>
    <Amount_Past_Due>1000</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20180311</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status/>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20180311</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>140</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>82</Account_Status>
    <Actual_Payment_Amount>1800</Actual_Payment_Amount>
    <Current_Balance>30000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>1000</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHBP03090001</Identification_Number>
    <Subscriber_Name> icicibank</Subscriber_Name>
    <Account_Number>ICICI8131302</Account_Number>
    <Portfolio_Type>I</Portfolio_Type>
    <Account_Type>03</Account_Type>
    <Open_Date>19940712</Open_Date>
    <Credit_Limit_Amount/>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>13</Account_Status>
    <Payment_Rating>2</Payment_Rating>
    <Payment_History_Profile>2222111111111111000000000000000000??</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>60000</Current_Balance>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20200630</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed>20200610</Date_Closed>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status/>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20170830</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>06</Month>
    <Days_Past_Due>80</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>05</Month>
    <Days_Past_Due>80</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>04</Month>
    <Days_Past_Due>75</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>03</Month>
    <Days_Past_Due>70</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>02</Month>
    <Days_Past_Due>65</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>01</Month>
    <Days_Past_Due>54</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>12</Month>
    <Days_Past_Due>52</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>11</Month>
    <Days_Past_Due>50</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>10</Month>
    <Days_Past_Due>48</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>09</Month>
    <Days_Past_Due>44</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>08</Month>
    <Days_Past_Due>42</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>07</Month>
    <Days_Past_Due>40</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>06</Month>
    <Days_Past_Due>38</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>05</Month>
    <Days_Past_Due>36</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>04</Month>
    <Days_Past_Due>34</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>03</Month>
    <Days_Past_Due>32</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>02</Month>
    <Days_Past_Due>30</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>01</Month>
    <Days_Past_Due>28</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>12</Month>
    <Days_Past_Due>28</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>11</Month>
    <Days_Past_Due>26</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>10</Month>
    <Days_Past_Due>24</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>09</Month>
    <Days_Past_Due>22</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>08</Month>
    <Days_Past_Due>19</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>07</Month>
    <Days_Past_Due>18</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>06</Month>
    <Days_Past_Due>17</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>05</Month>
    <Days_Past_Due>16</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>04</Month>
    <Days_Past_Due>15</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>14</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>02</Month>
    <Days_Past_Due>13</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>01</Month>
    <Days_Past_Due>12</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>12</Month>
    <Days_Past_Due>11</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>11</Month>
    <Days_Past_Due>10</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>10</Month>
    <Days_Past_Due>9</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>09</Month>
    <Days_Past_Due>8</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>08</Month>
    <Days_Past_Due>15</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>6</Month>
    <Account_Status>13</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>5</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>4</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>3</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>2</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>1</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>12</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>11</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>10</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>9</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>8</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>7</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>6</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>5</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>4</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>3</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>2</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>1</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>12</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>11</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>10</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>9</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>8</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>7</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>6</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>5</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>4</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>2</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>1</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>12</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>11</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>10</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>9</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>8</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>500</Actual_Payment_Amount>
    <Current_Balance>60000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>700</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHBP03090001</Identification_Number>
    <Subscriber_Name> icicibank</Subscriber_Name>
    <Account_Number>ICICI8131300</Account_Number>
    <Portfolio_Type>I</Portfolio_Type>
    <Account_Type>01</Account_Type>
    <Open_Date>19940710</Open_Date>
    <Credit_Limit_Amount/>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>53</Account_Status>
    <Payment_Rating>2</Payment_Rating>
    <Payment_History_Profile>2221111111111100000000000000000000??</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>50000</Current_Balance>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20200630</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status>00</Written_off_Settled_Status>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20170830</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>06</Month>
    <Days_Past_Due>70</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>05</Month>
    <Days_Past_Due>70</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>04</Month>
    <Days_Past_Due>65</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>03</Month>
    <Days_Past_Due>60</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>02</Month>
    <Days_Past_Due>55</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>01</Month>
    <Days_Past_Due>50</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>12</Month>
    <Days_Past_Due>48</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>11</Month>
    <Days_Past_Due>46</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>10</Month>
    <Days_Past_Due>44</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>09</Month>
    <Days_Past_Due>40</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>08</Month>
    <Days_Past_Due>38</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>07</Month>
    <Days_Past_Due>36</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>06</Month>
    <Days_Past_Due>34</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>05</Month>
    <Days_Past_Due>32</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>04</Month>
    <Days_Past_Due>30</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>03</Month>
    <Days_Past_Due>28</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>02</Month>
    <Days_Past_Due>26</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>01</Month>
    <Days_Past_Due>24</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>12</Month>
    <Days_Past_Due>24</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>11</Month>
    <Days_Past_Due>22</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>10</Month>
    <Days_Past_Due>20</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>09</Month>
    <Days_Past_Due>18</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>08</Month>
    <Days_Past_Due>17</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>07</Month>
    <Days_Past_Due>16</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>06</Month>
    <Days_Past_Due>15</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>05</Month>
    <Days_Past_Due>14</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>04</Month>
    <Days_Past_Due>13</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>12</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>02</Month>
    <Days_Past_Due>11</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>01</Month>
    <Days_Past_Due>10</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>12</Month>
    <Days_Past_Due>9</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>11</Month>
    <Days_Past_Due>8</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>10</Month>
    <Days_Past_Due>7</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>09</Month>
    <Days_Past_Due>6</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>08</Month>
    <Days_Past_Due>5</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>6</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>5</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>4</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>3</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>2</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>1</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>12</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>11</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>10</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>9</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>8</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>7</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>6</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>5</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>4</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>3</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>2</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>1</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>12</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>11</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>10</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>9</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>8</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>7</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>6</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>5</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>4</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>2</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>1</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>12</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>11</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>10</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>9</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>8</Month>
    <Account_Status>53</Account_Status>
    <Actual_Payment_Amount>300</Actual_Payment_Amount>
    <Current_Balance>50000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>500</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    <CAIS_Account_DETAILS>
    <Identification_Number>OTHBP03090001</Identification_Number>
    <Subscriber_Name> icicibank</Subscriber_Name>
    <Account_Number>ICICI8131301</Account_Number>
    <Portfolio_Type>M</Portfolio_Type>
    <Account_Type>02</Account_Type>
    <Open_Date>19940711</Open_Date>
    <Credit_Limit_Amount/>
    <Highest_Credit_or_Original_Loan_Amount>50000</Highest_Credit_or_Original_Loan_Amount>
    <Terms_Duration/>
    <Terms_Frequency/>
    <Scheduled_Monthly_Payment_Amount/>
    <Account_Status>78</Account_Status>
    <Payment_Rating>2</Payment_Rating>
    <Payment_History_Profile>2222111111111110000000000000000000??</Payment_History_Profile>
    <Special_Comment/>
    <Current_Balance>55000</Current_Balance>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Original_Charge_Off_Amount/>
    <Date_Reported>20200630</Date_Reported>
    <Date_of_First_Delinquency/>
    <Date_Closed/>
    <Date_of_Last_Payment/>
    <SuitFiledWillfulDefaultWrittenOffStatus/>
    <Written_off_Settled_Status/>
    <Value_of_Credits_Last_Month/>
    <Occupation_Code/>
    <Settlement_Amount/>
    <Value_of_Collateral/>
    <Type_of_Collateral/>
    <Written_Off_Amt_Total/>
    <Written_Off_Amt_Principal/>
    <Rate_of_Interest/>
    <Repayment_Tenure>0</Repayment_Tenure>
    <Promotional_Rate_Flag/>
    <Income/>
    <Income_Indicator/>
    <Income_Frequency_Indicator/>
    <DefaultStatusDate/>
    <LitigationStatusDate/>
    <WriteOffStatusDate/>
    <DateOfAddition>20170830</DateOfAddition>
    <CurrencyCode>INR</CurrencyCode>
    <Subscriber_comments/>
    <Consumer_comments/>
    <AccountHoldertypeCode>1</AccountHoldertypeCode>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>06</Month>
    <Days_Past_Due>75</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>05</Month>
    <Days_Past_Due>75</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>04</Month>
    <Days_Past_Due>70</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>03</Month>
    <Days_Past_Due>65</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>02</Month>
    <Days_Past_Due>60</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2020</Year>
    <Month>01</Month>
    <Days_Past_Due>52</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>12</Month>
    <Days_Past_Due>50</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>11</Month>
    <Days_Past_Due>48</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>10</Month>
    <Days_Past_Due>46</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>09</Month>
    <Days_Past_Due>42</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>08</Month>
    <Days_Past_Due>40</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>07</Month>
    <Days_Past_Due>38</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>06</Month>
    <Days_Past_Due>36</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>05</Month>
    <Days_Past_Due>34</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>04</Month>
    <Days_Past_Due>32</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>03</Month>
    <Days_Past_Due>30</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>02</Month>
    <Days_Past_Due>28</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2019</Year>
    <Month>01</Month>
    <Days_Past_Due>26</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>12</Month>
    <Days_Past_Due>26</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>11</Month>
    <Days_Past_Due>24</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>10</Month>
    <Days_Past_Due>22</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>09</Month>
    <Days_Past_Due>20</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>08</Month>
    <Days_Past_Due>18</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>07</Month>
    <Days_Past_Due>17</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>06</Month>
    <Days_Past_Due>16</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>05</Month>
    <Days_Past_Due>15</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>04</Month>
    <Days_Past_Due>14</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>03</Month>
    <Days_Past_Due>13</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>02</Month>
    <Days_Past_Due>12</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2018</Year>
    <Month>01</Month>
    <Days_Past_Due>11</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>12</Month>
    <Days_Past_Due>10</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>11</Month>
    <Days_Past_Due>9</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>10</Month>
    <Days_Past_Due>8</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>09</Month>
    <Days_Past_Due>7</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Account_History>
    <Year>2017</Year>
    <Month>08</Month>
    <Days_Past_Due>10</Days_Past_Due>
    <Asset_Classification>?</Asset_Classification>
    </CAIS_Account_History>
    <CAIS_Holder_Details>
    <Surname_Non_Normalized>DARSHAN</Surname_Non_Normalized>
    <First_Name_Non_Normalized>RAUT</First_Name_Non_Normalized>
    <Middle_Name_1_Non_Normalized/>
    <Middle_Name_2_Non_Normalized/>
    <Middle_Name_3_Non_Normalized/>
    <Alias/>
    <Gender_Code>1</Gender_Code>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <Passport_Number/>
    <Voter_ID_Number/>
    <Date_of_birth>19850910</Date_of_birth>
    </CAIS_Holder_Details>
    <CAIS_Holder_Address_Details>
    <First_Line_Of_Address_non_normalized>A-1 106</First_Line_Of_Address_non_normalized>
    <Second_Line_Of_Address_non_normalized>KRUSHNA APT.</Second_Line_Of_Address_non_normalized>
    <Third_Line_Of_Address_non_normalized>KHARGHAR</Third_Line_Of_Address_non_normalized>
    <City_non_normalized/>
    <Fifth_Line_Of_Address_non_normalized/>
    <State_non_normalized>27</State_non_normalized>
    <ZIP_Postal_Code_non_normalized>400075</ZIP_Postal_Code_non_normalized>
    <CountryCode_non_normalized>IB</CountryCode_non_normalized>
    <Address_indicator_non_normalized/>
    <Residence_code_non_normalized/>
    </CAIS_Holder_Address_Details>
    <CAIS_Holder_Phone_Details>
    <Telephone_Number>9987217355</Telephone_Number>
    <Telephone_Type/>
    <Telephone_Extension/>
    <Mobile_Telephone_Number/>
    <FaxNumber/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_Phone_Details>
    <CAIS_Holder_ID_Details>
    <Income_TAX_PAN>BQGPM4004M</Income_TAX_PAN>
    <PAN_Issue_Date/>
    <PAN_Expiration_Date/>
    <Passport_Number/>
    <Passport_Issue_Date/>
    <Passport_Expiration_Date/>
    <Voter_ID_Number/>
    <Voter_ID_Issue_Date/>
    <Voter_ID_Expiration_Date/>
    <Driver_License_Number/>
    <Driver_License_Issue_Date/>
    <Driver_License_Expiration_Date/>
    <Ration_Card_Number/>
    <Ration_Card_Issue_Date/>
    <Ration_Card_Expiration_Date/>
    <Universal_ID_Number/>
    <Universal_ID_Issue_Date/>
    <Universal_ID_Expiration_Date/>
    <EMailId>KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM</EMailId>
    </CAIS_Holder_ID_Details>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>6</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>5</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>4</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>3</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>2</Month>
    <Account_Status>78</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2020</Year>
    <Month>1</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>12</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>11</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>10</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>9</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>8</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>7</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>6</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>5</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>4</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>3</Month>
    <Account_Status>71</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>2</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2019</Year>
    <Month>1</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>12</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>11</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>10</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>9</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>8</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>7</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>6</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>5</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>4</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>3</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>2</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2018</Year>
    <Month>1</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>12</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>11</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>10</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>9</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    <Account_Review_Data>
    <Year>2017</Year>
    <Month>8</Month>
    <Account_Status>11</Account_Status>
    <Actual_Payment_Amount>400</Actual_Payment_Amount>
    <Current_Balance>55000</Current_Balance>
    <Credit_Limit_Amount>50000</Credit_Limit_Amount>
    <Amount_Past_Due>600</Amount_Past_Due>
    <Cash_Limit/>
    <EMI_Amount/>
    </Account_Review_Data>
    </CAIS_Account_DETAILS>
    </CAIS_Account>
    <Match_result>
    <Exact_match>Y</Exact_match>
    </Match_result>
    <TotalCAPS_Summary>
    <TotalCAPSLast7Days>0</TotalCAPSLast7Days>
    <TotalCAPSLast30Days>0</TotalCAPSLast30Days>
    <TotalCAPSLast90Days>0</TotalCAPSLast90Days>
    <TotalCAPSLast180Days>0</TotalCAPSLast180Days>
    </TotalCAPS_Summary>
    <CAPS>
    <CAPS_Summary>
    <CAPSLast7Days>0</CAPSLast7Days>
    <CAPSLast30Days>0</CAPSLast30Days>
    <CAPSLast90Days>0</CAPSLast90Days>
    <CAPSLast180Days>0</CAPSLast180Days>
    </CAPS_Summary>
    </CAPS>
    <NonCreditCAPS>
    <NonCreditCAPS_Summary>
    <NonCreditCAPSLast7Days>0</NonCreditCAPSLast7Days>
    <NonCreditCAPSLast30Days>0</NonCreditCAPSLast30Days>
    <NonCreditCAPSLast90Days>0</NonCreditCAPSLast90Days>
    <NonCreditCAPSLast180Days>0</NonCreditCAPSLast180Days>
    </NonCreditCAPS_Summary>
    </NonCreditCAPS>
    <Segment>
    <Income_Segment>04</Income_Segment>
    </Segment>
    <SCORE>
    <BureauScore>749</BureauScore>
    <BureauScoreConfidLevel>H</BureauScoreConfidLevel>
    </SCORE>
    </INProfileResponse>"""
    json_data = json.loads(json.dumps(xmltodict.parse(xml_input=xml_data)))
    return json_data


sample_response = {
    "INProfileResponse": {
        "Header": {
            "SystemCode": "0",
            "MessageText": None,
            "ReportDate": "20210107",
            "ReportTime": "174310"
        },
        "UserMessage": {
            "UserMessageText": "Normal Response"
        },
        "CreditProfileHeader": {
            "Enquiry_Username": "cpu2ecv_uat",
            "ReportDate": "20210107",
            "ReportTime": "174310",
            "Version": "V2.4",
            "ReportNumber": "1610021590114",
            "Subscriber": None,
            "UniqueID": None,
            "Subscriber_Name": "Bureau Disclosure Report with Income Segmentation",
            "CustomerReferenceID": None
        },
        "Current_Application": {
            "Current_Application_Details": {
                "Enquiry_Reason": "6",
                "Finance_Purpose": "99",
                "Amount_Financed": "0",
                "Duration_Of_Agreement": "0",
                "Current_Applicant_Details": {
                    "Last_Name": "Raut",
                    "First_Name": "Darshan",
                    "Middle_Name1": None,
                    "Middle_Name2": None,
                    "Middle_Name3": None,
                    "Gender_Code": "2",
                    "IncomeTaxPan": "BQGPM4004M",
                    "PAN_Issue_Date": None,
                    "PAN_Expiration_Date": None,
                    "Passport_Issue_Date": None,
                    "Passport_Expiration_Date": None,
                    "Voter_s_Identity_Card": None,
                    "Voter_ID_Issue_Date": None,
                    "Voter_ID_Expiration_Date": None,
                    "Driver_License_Number": None,
                    "Driver_License_Issue_Date": None,
                    "Driver_License_Expiration_Date": None,
                    "Ration_Card_Number": None,
                    "Ration_Card_Issue_Date": None,
                    "Ration_Card_Expiration_Date": None,
                    "Universal_ID_Number": None,
                    "Universal_ID_Issue_Date": None,
                    "Universal_ID_Expiration_Date": None,
                    "Date_Of_Birth_Applicant": "19850910",
                    "Telephone_Number_Applicant_1st": None,
                    "Telephone_Extension": None,
                    "Telephone_Type": None,
                    "MobilePhoneNumber": "9987217355",
                    "EMailId": "umesh.jawarkar@experian.com"
                },
                "Current_Other_Details": {
                    "Income": "0",
                    "Marital_Status": None,
                    "Employment_Status": None,
                    "Time_with_Employer": None,
                    "Number_of_Major_Credit_Card_Held": None
                },
                "Current_Applicant_Address_Details": {
                    "FlatNoPlotNoHouseNo": "A-1 106",
                    "BldgNoSocietyName": None,
                    "RoadNoNameAreaLocality": None,
                    "City": "Mumbai",
                    "Landmark": None,
                    "State": "27",
                    "PINCode": "400075",
                    "Country_Code": "IB"
                },
                "Current_Applicant_Additional_AddressDetails": None
            }
        },
        "CAIS_Account": {
            "CAIS_Summary": {
                "Credit_Account": {
                    "CreditAccountTotal": "8",
                    "CreditAccountActive": "7",
                    "CreditAccountDefault": "0",
                    "CreditAccountClosed": "1",
                    "CADSuitFiledCurrentBalance": "0"
                },
                "Total_Outstanding_Balance": {
                    "Outstanding_Balance_Secured": "195000",  # secured_currnt
                    "Outstanding_Balance_Secured_Percentage": "53",
                    "Outstanding_Balance_UnSecured": "171300",  # unsecured_currnt
                    "Outstanding_Balance_UnSecured_Percentage": "47",
                    "Outstanding_Balance_All": "366300"  # total_currnt
                }
            },
            "CAIS_Account_DETAILS": [
                {
                    "Identification_Number": "OTHBP03090001",
                    "Subscriber_Name": "icicibank",  # credit_lender
                    "Account_Number": "ICICI213220",  # credit_acctnum
                    "Portfolio_Type": "R",
                    "Account_Type": "10",  # credit_type
                    "Open_Date": "19980522",  # credit_opendate
                    "Credit_Limit_Amount": "50000",  # credit_limit_amt
                    "Highest_Credit_or_Original_Loan_Amount": "50000",  # credit_highest
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "53",  # credit_accntstatus
                    "Payment_Rating": "0",
                    "Payment_History_Profile": "N",
                    "Special_Comment": None,
                    "Current_Balance": "121000",  # credit_currentbalance
                    "Amount_Past_Due": "2350",  # credit_ammntoverdue
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20180315",  # credit_datereported
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,  # credit_dateclose
                    "Date_of_Last_Payment": None,
                    # suitfiled_wil_def_writeoff_status
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": "00",  # credit_written_status
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,  # credit_voc
                    "Type_of_Collateral": None,  # credit_toc
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,  # credit_roi
                    "Repayment_Tenure": "0",  # credit_repay_tenure
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20180315",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": {
                        "Year": "2018", # year
                        "Month": "03",
                        "Days_Past_Due": "14", # description
                        "Asset_Classification": "?"
                    },
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",  # name
                        "First_Name_Non_Normalized": "RAUT",  # name
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",  # gender
                        "Income_TAX_PAN": "BQGPM4004M",  # pan
                        "Passport_Number": None,  # passport
                        "Voter_ID_Number": None,  # voter_id
                        "Date_of_birth": "19850910"  # dob
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",  # address1
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",  # address1
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",  # address1
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",  # telephone
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": None  # email
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": None
                    },
                    "Account_Review_Data": {
                        "Year": "2018",  
                        "Month": "3",
                        "Account_Status": "53",
                        "Actual_Payment_Amount": "2500",
                        "Current_Balance": "121000",
                        "Credit_Limit_Amount": "50000",
                        "Amount_Past_Due": "2350",
                        "Cash_Limit": None,
                        "EMI_Amount": None
                    }
                },
                {
                    "Identification_Number": "FORFORAMEX005",
                    "Subscriber_Name": "American Express Banking Corp",
                    "Account_Number": "AMEX8130496",
                    "Portfolio_Type": "R",
                    "Account_Type": "10",
                    "Open_Date": "19971013",
                    "Credit_Limit_Amount": "50000",
                    "Highest_Credit_or_Original_Loan_Amount": "10000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "53",
                    "Payment_Rating": "6",
                    "Payment_History_Profile": "6???????????????????????????????????",
                    "Special_Comment": None,
                    "Current_Balance": "300",
                    "Amount_Past_Due": "250000",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20190611",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": "00",
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20190511",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": [
                        {
                            "Year": "2019",
                            "Month": "06",
                            "Days_Past_Due": "450",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "05",
                            "Days_Past_Due": "450",
                            "Asset_Classification": "?"
                        }
                    ],
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": [
                        {
                            "Income_TAX_PAN": "BQGPM4004M",
                            "PAN_Issue_Date": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Number": None,
                            "Passport_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Number": None,
                            "Driver_License_Issue_Date": None,
                            "Driver_License_Expiration_Date": None,
                            "Ration_Card_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Number": None,
                            "Universal_ID_Issue_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                        },
                        {
                            "Income_TAX_PAN": "BQGPM4004M",
                            "PAN_Issue_Date": None,
                            "PAN_Expiration_Date": None,
                            "Passport_Number": None,
                            "Passport_Issue_Date": None,
                            "Passport_Expiration_Date": None,
                            "Voter_ID_Number": None,
                            "Voter_ID_Issue_Date": None,
                            "Voter_ID_Expiration_Date": None,
                            "Driver_License_Number": None,
                            "Driver_License_Issue_Date": None,
                            "Driver_License_Expiration_Date": None,
                            "Ration_Card_Number": None,
                            "Ration_Card_Issue_Date": None,
                            "Ration_Card_Expiration_Date": None,
                            "Universal_ID_Number": None,
                            "Universal_ID_Issue_Date": None,
                            "Universal_ID_Expiration_Date": None,
                            "EMailId": None
                        }
                    ],
                    "Account_Review_Data": [
                        {
                            "Year": "2019",
                            "Month": "6",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "9002",
                            "Current_Balance": "300",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "250000",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "5",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "9002",
                            "Current_Balance": "301",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "36000",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        }
                    ]
                },
                {
                    "Identification_Number": "FORFORAMEX005",
                    "Subscriber_Name": "American Express Banking Corp",
                    "Account_Number": "AMEX8130497",
                    "Portfolio_Type": "I",
                    "Account_Type": "05",
                    "Open_Date": "19910120",
                    "Credit_Limit_Amount": None,
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "82",
                    "Payment_Rating": "4",
                    "Payment_History_Profile": "N",
                    "Special_Comment": None,
                    "Current_Balance": "30000",
                    "Amount_Past_Due": "1000",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20180311",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": None,
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20180311",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": {
                        "Year": "2018",
                        "Month": "03",
                        "Days_Past_Due": "140",
                        "Asset_Classification": "?"
                    },
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": {
                        "Year": "2018",
                        "Month": "3",
                        "Account_Status": "82",
                        "Actual_Payment_Amount": "1800",
                        "Current_Balance": "30000",
                        "Credit_Limit_Amount": "50000",
                        "Amount_Past_Due": "1000",
                        "Cash_Limit": None,
                        "EMI_Amount": None
                    }
                },
                {
                    "Identification_Number": "OTHNone",
                    "Subscriber_Name": "SBI Cards and Payment Services Private Limited",
                    "Account_Number": "SBIC8130496",
                    "Portfolio_Type": "R",
                    "Account_Type": "10",
                    "Open_Date": "19910314",
                    "Credit_Limit_Amount": "50000",
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "82",
                    "Payment_Rating": "4",
                    "Payment_History_Profile": "N",
                    "Special_Comment": None,
                    "Current_Balance": "20000",
                    "Amount_Past_Due": "900",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20180311",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": None,
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20180311",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": {
                        "Year": "2018",
                        "Month": "03",
                        "Days_Past_Due": "130",
                        "Asset_Classification": "?"
                    },
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": {
                        "Year": "2018",
                        "Month": "3",
                        "Account_Status": "82",
                        "Actual_Payment_Amount": "800",
                        "Current_Balance": "20000",
                        "Credit_Limit_Amount": "50000",
                        "Amount_Past_Due": "900",
                        "Cash_Limit": None,
                        "EMI_Amount": None
                    }
                },
                {
                    "Identification_Number": "OTHNone",
                    "Subscriber_Name": "SBI Cards and Payment Services Private Limited",
                    "Account_Number": "SBIC8130497",
                    "Portfolio_Type": "I",
                    "Account_Type": "01",
                    "Open_Date": "19910120",
                    "Credit_Limit_Amount": None,
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "82",
                    "Payment_Rating": "4",
                    "Payment_History_Profile": "N",
                    "Special_Comment": None,
                    "Current_Balance": "30000",
                    "Amount_Past_Due": "1000",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20180311",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": None,
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20180311",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": {
                        "Year": "2018",
                        "Month": "03",
                        "Days_Past_Due": "140",
                        "Asset_Classification": "?"
                    },
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": {
                        "Year": "2018",
                        "Month": "3",
                        "Account_Status": "82",
                        "Actual_Payment_Amount": "1800",
                        "Current_Balance": "30000",
                        "Credit_Limit_Amount": "50000",
                        "Amount_Past_Due": "1000",
                        "Cash_Limit": None,
                        "EMI_Amount": None
                    }
                },
                {
                    "Identification_Number": "OTHBP03090001",
                    "Subscriber_Name": "icicibank",
                    "Account_Number": "ICICI8131302",
                    "Portfolio_Type": "I",
                    "Account_Type": "03",
                    "Open_Date": "19940712",
                    "Credit_Limit_Amount": None,
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "13",
                    "Payment_Rating": "2",
                    "Payment_History_Profile": "2222111111111111000000000000000000??",
                    "Special_Comment": None,
                    "Current_Balance": "60000",
                    "Amount_Past_Due": "700",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20200630",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": "20200610",
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": None,
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20170830",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": [
                        {
                            "Year": "2020",
                            "Month": "06",
                            "Days_Past_Due": "80",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "05",
                            "Days_Past_Due": "80",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "04",
                            "Days_Past_Due": "75",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "03",
                            "Days_Past_Due": "70",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "02",
                            "Days_Past_Due": "65",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "01",
                            "Days_Past_Due": "54",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Days_Past_Due": "52",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Days_Past_Due": "50",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Days_Past_Due": "48",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "09",
                            "Days_Past_Due": "44",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "08",
                            "Days_Past_Due": "42",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "07",
                            "Days_Past_Due": "40",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "06",
                            "Days_Past_Due": "38",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "05",
                            "Days_Past_Due": "36",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "04",
                            "Days_Past_Due": "34",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "03",
                            "Days_Past_Due": "32",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "02",
                            "Days_Past_Due": "30",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "01",
                            "Days_Past_Due": "28",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Days_Past_Due": "28",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Days_Past_Due": "26",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Days_Past_Due": "24",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "09",
                            "Days_Past_Due": "22",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "08",
                            "Days_Past_Due": "19",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "07",
                            "Days_Past_Due": "18",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "06",
                            "Days_Past_Due": "17",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "05",
                            "Days_Past_Due": "16",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "04",
                            "Days_Past_Due": "15",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "03",
                            "Days_Past_Due": "14",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "02",
                            "Days_Past_Due": "13",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "01",
                            "Days_Past_Due": "12",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Days_Past_Due": "11",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "11",
                            "Days_Past_Due": "10",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "10",
                            "Days_Past_Due": "9",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "09",
                            "Days_Past_Due": "8",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "08",
                            "Days_Past_Due": "15",
                            "Asset_Classification": "?"
                        }
                    ],
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": [
                        {
                            "Year": "2020",
                            "Month": "6",
                            "Account_Status": "13",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "5",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "4",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "3",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "2",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "1",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "9",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "8",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "7",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "6",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "5",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "4",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "3",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "2",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "1",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "9",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "8",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "7",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "6",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "5",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "4",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "3",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "2",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "1",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "11",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "10",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "9",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "8",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "500",
                            "Current_Balance": "60000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "700",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        }
                    ]
                },
                {
                    "Identification_Number": "OTHBP03090001",
                    "Subscriber_Name": "icicibank",
                    "Account_Number": "ICICI8131300",
                    "Portfolio_Type": "I",
                    "Account_Type": "01",
                    "Open_Date": "19940710",
                    "Credit_Limit_Amount": None,
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "53",
                    "Payment_Rating": "2",
                    "Payment_History_Profile": "2221111111111100000000000000000000??",
                    "Special_Comment": None,
                    "Current_Balance": "50000",
                    "Amount_Past_Due": "500",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20200630",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": "00",
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20170830",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": [
                        {
                            "Year": "2020",
                            "Month": "06",
                            "Days_Past_Due": "70",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "05",
                            "Days_Past_Due": "70",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "04",
                            "Days_Past_Due": "65",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "03",
                            "Days_Past_Due": "60",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "02",
                            "Days_Past_Due": "55",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "01",
                            "Days_Past_Due": "50",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Days_Past_Due": "48",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Days_Past_Due": "46",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Days_Past_Due": "44",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "09",
                            "Days_Past_Due": "40",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "08",
                            "Days_Past_Due": "38",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "07",
                            "Days_Past_Due": "36",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "06",
                            "Days_Past_Due": "34",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "05",
                            "Days_Past_Due": "32",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "04",
                            "Days_Past_Due": "30",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "03",
                            "Days_Past_Due": "28",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "02",
                            "Days_Past_Due": "26",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "01",
                            "Days_Past_Due": "24",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Days_Past_Due": "24",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Days_Past_Due": "22",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Days_Past_Due": "20",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "09",
                            "Days_Past_Due": "18",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "08",
                            "Days_Past_Due": "17",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "07",
                            "Days_Past_Due": "16",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "06",
                            "Days_Past_Due": "15",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "05",
                            "Days_Past_Due": "14",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "04",
                            "Days_Past_Due": "13",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "03",
                            "Days_Past_Due": "12",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "02",
                            "Days_Past_Due": "11",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "01",
                            "Days_Past_Due": "10",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Days_Past_Due": "9",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "11",
                            "Days_Past_Due": "8",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "10",
                            "Days_Past_Due": "7",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "09",
                            "Days_Past_Due": "6",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "08",
                            "Days_Past_Due": "5",
                            "Asset_Classification": "?"
                        }
                    ],
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": [
                        {
                            "Year": "2020",
                            "Month": "6",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "5",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "4",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "3",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "2",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "1",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "9",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "8",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "7",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "6",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "5",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "4",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "3",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "2",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "1",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "9",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "8",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "7",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "6",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "5",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "4",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "3",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "2",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "1",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "11",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "10",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "9",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "8",
                            "Account_Status": "53",
                            "Actual_Payment_Amount": "300",
                            "Current_Balance": "50000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "500",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        }
                    ]
                },
                {
                    "Identification_Number": "OTHBP03090001",
                    "Subscriber_Name": "icicibank",
                    "Account_Number": "ICICI8131301",
                    "Portfolio_Type": "M",
                    "Account_Type": "02",
                    "Open_Date": "19940711",
                    "Credit_Limit_Amount": None,
                    "Highest_Credit_or_Original_Loan_Amount": "50000",
                    "Terms_Duration": None,
                    "Terms_Frequency": None,
                    "Scheduled_Monthly_Payment_Amount": None,
                    "Account_Status": "78",
                    "Payment_Rating": "2",
                    "Payment_History_Profile": "2222111111111110000000000000000000??",
                    "Special_Comment": None,
                    "Current_Balance": "55000",
                    "Amount_Past_Due": "600",
                    "Original_Charge_Off_Amount": None,
                    "Date_Reported": "20200630",
                    "Date_of_First_Delinquency": None,
                    "Date_Closed": None,
                    "Date_of_Last_Payment": None,
                    "SuitFiledWillfulDefaultWrittenOffStatus": None,
                    "Written_off_Settled_Status": None,
                    "Value_of_Credits_Last_Month": None,
                    "Occupation_Code": None,
                    "Settlement_Amount": None,
                    "Value_of_Collateral": None,
                    "Type_of_Collateral": None,
                    "Written_Off_Amt_Total": None,
                    "Written_Off_Amt_Principal": None,
                    "Rate_of_Interest": None,
                    "Repayment_Tenure": "0",
                    "Promotional_Rate_Flag": None,
                    "Income": None,
                    "Income_Indicator": None,
                    "Income_Frequency_Indicator": None,
                    "DefaultStatusDate": None,
                    "LitigationStatusDate": None,
                    "WriteOffStatusDate": None,
                    "DateOfAddition": "20170830",
                    "CurrencyCode": "INR",
                    "Subscriber_comments": None,
                    "Consumer_comments": None,
                    "AccountHoldertypeCode": "1",
                    "CAIS_Account_History": [
                        {
                            "Year": "2020",
                            "Month": "06",
                            "Days_Past_Due": "75",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "05",
                            "Days_Past_Due": "75",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "04",
                            "Days_Past_Due": "70",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "03",
                            "Days_Past_Due": "65",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "02",
                            "Days_Past_Due": "60",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2020",
                            "Month": "01",
                            "Days_Past_Due": "52",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Days_Past_Due": "50",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Days_Past_Due": "48",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Days_Past_Due": "46",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "09",
                            "Days_Past_Due": "42",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "08",
                            "Days_Past_Due": "40",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "07",
                            "Days_Past_Due": "38",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "06",
                            "Days_Past_Due": "36",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "05",
                            "Days_Past_Due": "34",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "04",
                            "Days_Past_Due": "32",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "03",
                            "Days_Past_Due": "30",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "02",
                            "Days_Past_Due": "28",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2019",
                            "Month": "01",
                            "Days_Past_Due": "26",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Days_Past_Due": "26",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Days_Past_Due": "24",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Days_Past_Due": "22",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "09",
                            "Days_Past_Due": "20",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "08",
                            "Days_Past_Due": "18",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "07",
                            "Days_Past_Due": "17",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "06",
                            "Days_Past_Due": "16",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "05",
                            "Days_Past_Due": "15",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "04",
                            "Days_Past_Due": "14",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "03",
                            "Days_Past_Due": "13",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "02",
                            "Days_Past_Due": "12",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2018",
                            "Month": "01",
                            "Days_Past_Due": "11",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Days_Past_Due": "10",
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
                            "Days_Past_Due": "8",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "09",
                            "Days_Past_Due": "7",
                            "Asset_Classification": "?"
                        },
                        {
                            "Year": "2017",
                            "Month": "08",
                            "Days_Past_Due": "10",
                            "Asset_Classification": "?"
                        }
                    ],
                    "CAIS_Holder_Details": {
                        "Surname_Non_Normalized": "DARSHAN",
                        "First_Name_Non_Normalized": "RAUT",
                        "Middle_Name_1_Non_Normalized": None,
                        "Middle_Name_2_Non_Normalized": None,
                        "Middle_Name_3_Non_Normalized": None,
                        "Alias": None,
                        "Gender_Code": "1",
                        "Income_TAX_PAN": "BQGPM4004M",
                        "Passport_Number": None,
                        "Voter_ID_Number": None,
                        "Date_of_birth": "19850910"
                    },
                    "CAIS_Holder_Address_Details": {
                        "First_Line_Of_Address_non_normalized": "A-1 106",
                        "Second_Line_Of_Address_non_normalized": "KRUSHNA APT.",
                        "Third_Line_Of_Address_non_normalized": "KHARGHAR",
                        "City_non_normalized": None,
                        "Fifth_Line_Of_Address_non_normalized": None,
                        "State_non_normalized": "27",
                        "ZIP_Postal_Code_non_normalized": "400075",
                        "CountryCode_non_normalized": "IB",
                        "Address_indicator_non_normalized": None,
                        "Residence_code_non_normalized": None
                    },
                    "CAIS_Holder_Phone_Details": {
                        "Telephone_Number": "9987217355",
                        "Telephone_Type": None,
                        "Telephone_Extension": None,
                        "Mobile_Telephone_Number": None,
                        "FaxNumber": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "CAIS_Holder_ID_Details": {
                        "Income_TAX_PAN": "BQGPM4004M",
                        "PAN_Issue_Date": None,
                        "PAN_Expiration_Date": None,
                        "Passport_Number": None,
                        "Passport_Issue_Date": None,
                        "Passport_Expiration_Date": None,
                        "Voter_ID_Number": None,
                        "Voter_ID_Issue_Date": None,
                        "Voter_ID_Expiration_Date": None,
                        "Driver_License_Number": None,
                        "Driver_License_Issue_Date": None,
                        "Driver_License_Expiration_Date": None,
                        "Ration_Card_Number": None,
                        "Ration_Card_Issue_Date": None,
                        "Ration_Card_Expiration_Date": None,
                        "Universal_ID_Number": None,
                        "Universal_ID_Issue_Date": None,
                        "Universal_ID_Expiration_Date": None,
                        "EMailId": "KRISHNAPHRIYA.MOHANRAJ@EXPERIAN.COM"
                    },
                    "Account_Review_Data": [
                        {
                            "Year": "2020",
                            "Month": "6",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "5",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "4",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "3",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "2",
                            "Account_Status": "78",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2020",
                            "Month": "1",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "12",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "11",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "10",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "9",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "8",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "7",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "6",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "5",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "4",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "3",
                            "Account_Status": "71",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "2",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2019",
                            "Month": "1",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "12",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "11",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "10",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "9",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "8",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "7",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "6",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "5",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "4",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "3",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "2",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2018",
                            "Month": "1",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "12",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "11",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "10",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "9",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        },
                        {
                            "Year": "2017",
                            "Month": "8",
                            "Account_Status": "11",
                            "Actual_Payment_Amount": "400",
                            "Current_Balance": "55000",
                            "Credit_Limit_Amount": "50000",
                            "Amount_Past_Due": "600",
                            "Cash_Limit": None,
                            "EMI_Amount": None
                        }
                    ]
                }
            ]
        },

        "Match_result": {
            "Exact_match": "Y"
        },
        "TotalCAPS_Summary": {
            "TotalCAPSLast7Days": "0",
            "TotalCAPSLast30Days": "0",
            "TotalCAPSLast90Days": "0",
            "TotalCAPSLast180Days": "0"
        },
        "CAPS": {
            "CAPS_Summary": {
                "CAPSLast7Days": "0",
                "CAPSLast30Days": "0",
                "CAPSLast90Days": "0",
                "CAPSLast180Days": "0"
            }
        },
        "NonCreditCAPS": {
            "NonCreditCAPS_Summary": {
                "NonCreditCAPSLast7Days": "0",
                "NonCreditCAPSLast30Days": "0",
                "NonCreditCAPSLast90Days": "0",
                "NonCreditCAPSLast180Days": "0"
            }
        },
        "Segment": {
            "Income_Segment": "04"
        },
        "SCORE": {
            "BureauScore": "749",
            "BureauScoreConfidLevel": "H"
        }
    }
}


def convert_to_html_request():
    json_data = get_json_data()
    request_data = json_data.get("INProfileResponse")
    score_dict = request_data.get("SCORE")
    credit_score = score_dict.get("BureauScore")
    credit_confid_level = score_dict.get("BureauScoreConfidLevel")

    credit_profile = request_data.get("CreditProfileHeader")
    experian_reportnum = credit_profile.get("ReportNumber")
    experian_report_created = credit_profile.get("ReportDate")
    unique_transaction_id = credit_profile.get("UniqueID")

    credit_customer = request_data.get("Current_Application")
    current_application_details = credit_customer.get(
        "Current_Application_Details")
    current_applicant_details = current_application_details.get(
        "Current_Applicant_Details")
    first_name = current_applicant_details.get("First_Name")
    last_name = current_applicant_details.get("Last_Name")
    gender = current_applicant_details.get("Gender_Code")
    mobile_number = current_applicant_details.get("MobilePhoneNumber")
    email_id = current_applicant_details.get("EMailId")
    passport = current_applicant_details.get("Passport_Number")
    voterid = current_applicant_details.get("Voter_ID_Number")
    aadharid = current_applicant_details.get("")
    telephone_num = current_applicant_details.get("Telephone_Number")
    driving_license = current_applicant_details.get("")
    date_of_birth = current_applicant_details.get("Date_Of_Birth_Applicant")
    panid = current_applicant_details.get("IncomeTaxPan")
    ration_num = current_applicant_details.get("")
    address2 = current_applicant_details.get(
        "Second_Line_Of_Address_non_normalized"),
    address3 = current_applicant_details.get(
        "Third_Line_Of_Address_non_normalized"),

    cais_credit_account = request_data.get("CAIS_Account")
    cais_credit_summary = cais_credit_account.get("CAIS_Summary")
    credit_account = cais_credit_summary.get("Credit_Account")
    credit_total = credit_account.get("CreditAccountTotal")
    credit_active = credit_account.get("CreditAccountActive")
    credit_closed = credit_account.get("CreditAccountClosed")
    credit_suitfiled_current_balance = credit_account.get("CADSuitFiledCurrentBalance")

    credit_account = cais_credit_summary.get("Total_Outstanding_Balance")
    credit_secured_current = credit_account.get("Outstanding_Balance_Secured")
    credit_unsecured_current = credit_account.get(
        "Outstanding_Balance_UnSecured")
    credit_total_current = credit_account.get("Outstanding_Balance_All")



    credit_cais_details = cais_credit_account.get("CAIS_Account_DETAILS")
    credit_cais_details_list = []
    for credit_cais_dict in credit_cais_details:
        new_credit_cais_dict = {
            "credit_lender": credit_cais_dict.get("Subscriber_Name"),
            "credit_acctnum": credit_cais_dict.get("Account_Number"),
            "credit_type": credit_cais_dict.get("Account_Type"),
            "credit_dateopen": credit_cais_dict.get("Open_Date"),
            "credit_limit_amt": credit_cais_dict.get("Credit_Limit_Amount"),
            "credit_highest": credit_cais_dict.get("Highest_Credit_or_Original_Loan_Amount"),
            "credit_accnt_status": credit_cais_dict.get("Account_Status"),
            "credit_current_balance": credit_cais_dict.get("Current_Balance"),
            "credit_amt_overdue": credit_cais_dict.get("Amount_Past_Due"),
            "credit_date_reported": credit_cais_dict.get("Date_Reported"),
            "credit_dateclose": credit_cais_dict.get("Date_Closed"),
            "suitfiled_wil_def_writeoff_status": credit_cais_dict.get("SuitFiledWillfulDefaultWrittenOffStatus"),
            "credit_written_status": credit_cais_dict.get("Written_off_Settled_Status"),
            "credit_voc": credit_cais_dict.get("Value_of_Collateral"),
            "credit_toc": credit_cais_dict.get("Type_of_Collateral"),
            "credit_roi": credit_cais_dict.get("Rate_of_Interest"),
            "credit_repay_tenure": credit_cais_dict.get("Repayment_Tenure"),

        },
    cais_account_history = credit_cais_details[4]
    # cais_account_year = cais_account_history.get("Year")
    cais_account_month = cais_account_history.get("Month")
    month = datetime.datetime.now()
    currentmonth = month.strftime("%m")
    
    # days_past_due = cais_account_history.get("Days_Past_Due")
    cais_account_month_list = []



    


    
    

    # january = "jan"
    # datetime_object = datetime.datetime.strptime(january, "%b")
    # january_month = datetime_object.month

    # febuary = "feb"
    # datetime_object = datetime.datetime.strptime(febuary, "%b")
    # febuary_month = datetime_object.month

    # march = "mar"
    # datetime_object = datetime.datetime.strptime(march, "%b")
    # march_month = datetime_object.month

    # april = "apr"
    # datetime_object = datetime.datetime.strptime(april, "%b")
    # april_month = datetime_object.month

    # may = "may"
    # datetime_object = datetime.datetime.strptime(may, "%b")
    # may_month = datetime_object.month

    # june = "jun"
    # datetime_object = datetime.datetime.strptime(june, "%b")
    # june_month = datetime_object.month

    # july = "jul"
    # datetime_object = datetime.datetime.strptime(july, "%b")
    # july_month = datetime_object.month

    # august = "aug"
    # datetime_object = datetime.datetime.strptime(august, "%b")
    # august_month = datetime_object.month

    # september = "sep"
    # datetime_object = datetime.datetime.strptime(september, "%b")
    # september_month = datetime_object.month

    # october = "oct"
    # datetime_object = datetime.datetime.strptime(october, "%b")
    # october_month = datetime_object.month

    # november = "nov"
    # datetime_object = datetime.datetime.strptime(november, "%b")
    # november_month = datetime_object.month

    # december = "dec"
    # datetime_object = datetime.datetime.strptime(december, "%b")
    # december_month = datetime_object.month
    


    # month_list = [january_month,febuary_month, march_month, april_month, may_month, june_month, july_month, august_month, september_month, october_month, november_month, december_month]
    # months_dict = {"Months": month_list}
    

    cais_noncredit_account = request_data.get("NonCreditCAPS")
    noncredit_account_summary = cais_noncredit_account.get("NonCreditCAPS_Summary")
    noncredit_7days_caps = noncredit_account_summary.get("NonCreditCAPSLast7Days")
    noncredit_30days_caps = noncredit_account_summary.get("NonCreditCAPSLast30Days")
    noncredit_90days_caps = noncredit_account_summary.get("NonCreditCAPSLast90Days")
    noncredit_180days_caps = noncredit_account_summary.get("NonCreditCAPSLast180Days")





    credit_cais_details_list.append(new_credit_cais_dict)
    cais_account_month_list.append(currentmonth)
    # account_review_list.append(new_review_data_dict)

    html_request = [{


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
            "fname": first_name,
            "lname": last_name,
            "mobile_no": mobile_number,
            "email": email_id,
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
            "total_credit": credit_total,
            "active_credit": credit_active,
            "closed_credit": credit_closed,
            "settled_credit": credit_suitfiled_current_balance,
            "secured_current":  credit_secured_current,
            "unsecured_current": credit_unsecured_current,
            "total_current": credit_total_current,
            "noncredit_inquiry_7": noncredit_7days_caps,
            "noncredit_inquiry_30": noncredit_30days_caps,
            "noncredit_inquiry_90": noncredit_90days_caps,
            "noncredit_inquiry_180": noncredit_180days_caps 
        },


        "credit_accnt_information_details": credit_cais_details_list,
        "payment_history" : cais_account_month_list
        






       
    }]

    print(html_request, "Well done")

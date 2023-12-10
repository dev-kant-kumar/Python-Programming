# Bank Management System 
import time 
#Support 
support=''' 
📞  0123456789

📠  020 - 27218081

📧  help@uquaonbank

🌐  www.uquaonbank.com

🗾   (Uquaon  Bank ) 
4th Floor, Mantri Sterling, Plot No. 340, Survey No. 907/8, Model Colony, xyz Chowk, xxx-411 016.
'''
notice='''

IMPORTANT:Beware of the fraudulent messages asking to you call any number for verification/download any app to update your KYC/Aadhaar details. Uquaon Bank never asks you to download any third party app for such activities. Please stay alert from such SMS/calls as this may result in financial loss. Stay safe. Team Uquaon  Bank
'''
# Main Menu 
menu=''' How can I help you today ? 

1. Banking services 🏦
2. Credit card services 💳
3. Uquaon Bank FASTag services 🛣️
4. Loan Services 💸
5. Fixed Deposit services 🔒
6. Block/Unblock card 🚫
7. Offers around me 🎁
8. Other services 🔎
9. 🆕 Gold Loan Services ⚖️

Please type the option number (Ex: 3)
''' 
# Banking Services
banking=''' We're always here to help you with the *Banking services*. What would you like to do? ☺

1. Check Account Balance 💸 
2. Check last 5 transactions 📃 
3. Current Account services 💰
4. View/Update Nominee Status 👤
5. Issue New Cheque Book ✍🏻
6. Tax Payment 🗂️
7. Open a new  account ⚡'''

#Banking- Check Account Balance #

account_balance='''

You don’t seem to have an Uquaon Bank account.

*Open an account* in less than 4 mins, using your Aadhaar.

*Select option 7 to open a new InstaSave account



Please choose an *option* to proceed (Ex: 4)
''' 
# Banking- last5 transaction.  #
last_5_transactions='''
You don’t seem to have an Uquaon Bank account.

*Open an account* in less than 4 mins, using your Aadhaar.

*Select option 7 to get open a Savings account* 

'''
# Banking- Current Account Services # 
current_account='''

''' 

# Banking- View/update nominee status #
nominee= '''
To *view/update* your *nominee status*, tap below 👇
'''

# Banking- Issue new cheque book #
cheque_book= '''
I'll help you issue a cheque book! 😌

Sorry, I'm unable to recall your account(s). Please try checking this later.  😕
'''
# Banking- Tax payment #
tax_payment= '''
Pay your tax securely and safely with Uquaon Bank !

Tap below to fill in details and pay now
'''

# Banking- open new InstaSave account#
open_account= '''
ACCOUNT
  
An expansive ATM network, best-in-class channels of digital banking, instant and digital solutions for your investment and protection needs, customised loan products and a wide range of accounts and deposits, personalised banking with Uquaon  Bank offers you a one-of-its-kind, seamless and hassle-free experience.

Here’s a look at the savings accounts that you can open with Uquaon Bank.

1.Savings Accounts
2.Online Trading & Demat Account
3.Salary Account
4.PayLater by Uquaon Bank
5.Pension Accounts
6.Defence Salary Account
7.Other Accounts

Please type the option number (Ex: 3)

''' 
savings_accounts='''
Savings Account

Here’s a range of savings accounts from Uquaon Bank to suit your needs. You unlock a world of possibilities when you open a savings account with Uquaon Bank. Our savings account helps you do so much more than just saving for your future.

CHOOSE THE AUTO ACCOUNT THAT SUITS YOUR NEEDS 

1.Insta Save Account
2.‘The ONE’ Savings Account
3.Advantage Woman Aura Savings Account
4.Advantage Woman Savings Account
5.Seniors Club Savings Account
6.Young Stars Savings Account


'''
# Main Menu
def main_menu():
    mm_response=int(input("Enter the option number: "))
    if mm_response==1:
        print(banking)
        print()
        banking_menu()
    elif mm_response==2:
        print("Credit Card Services")
    elif mm_response==3:
        print("UP FASTag Services")
    elif mm_response==4:
          print("Loan Services")
    elif mm_response==5:
        print("Fixed Deposit Services")
    elif mm_response==6:
        print("Block/Unblock Card")
    elif mm_response==7:
          print("Offers around me")
    elif mm_response==8:
         print("Other Services")
    elif mm_response==9:
          print("Gold loan services")
    
    
#  Banking  Services
def banking_menu():
    bmenu_response=int(input("Enter the option number: "))
    if bmenu_response==1:
        print(account_balance)
    elif bmenu_response==2:
        print(last_5_transactions)
    elif bmenu_response==3:
        print(current_account)
    elif bmenu_response==4:
        print(nominee)
    elif bmenu_response==5:
        print(cheque_book)
    elif bmenu_response==6:
        print(tax_payment)
    elif bmenu_response==7:
        print(open_account)
        open_account_menu()
     
def open_account_menu():
     oam_response=int(input("Enter the option: "))
     if oam_response==1:
          print(savings_accounts)
     elif oam_response==2 :
         print()
     elif oam_response==3:
         print()
     elif oam_response==4:
          print()
     elif oam_response==5:
          print()
     elif oam_response==6:
          print()
     elif oam_response==7:
       print()
      
      
      
      

# User Interface 
print(" " *20 ,"Uquaon Payment Bank", " "*25)
print("\v"*1)
#
print(time.ctime())
print("="*60)
print(support)
print("="*60)
print("\v"*1)
print(notice)
print("\n"*2)
name=input("Enter Your Name: ")
print()
print("Good Morning,",name,",Welcome to Uquaon Payment Bank")
print()
print("\v"*2)
print(menu)
print("\v"*2)
main_menu()

print("Hello")

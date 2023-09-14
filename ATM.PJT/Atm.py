import mysql.connector
import smtplib
import random
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Atm_db"
    )
mycursor=mydb.cursor()
#user_section
#INSERT_DATA
def insert_data():
   sql ="insert into Atm_details(no,Name,Age,Gender,Account_no,Phone_no,Bank_name,Branch_name,Amount,Withdraw_amt,Balance) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   no=int(input("Enter your no:"))
   Name=input("Enter your full name:")
   Age=int(input("Enter your age:"))
   Gender=input("Enter your gender:")
   Account_no=input("Enter your account num:")
   Phone_no=input("Enter your phone num:")
   Bank_name=input("Enter your bank name:")
   Branch_name=input("Enter your branch name:")
   Amount=int(input("Enter your amount:"))
   Withdraw_amt=int(input("Enter your withdraw amount:")) 
   Balance=Amount-Withdraw_amt
   val=(no,Name,Age,Gender,Account_no,Phone_no,Bank_name,Branch_name,Amount,Withdraw_amt,Balance)
   mycursor.execute(sql,val)
   mydb.commit()
   print("DATA SAVED SUCCESSFULLY")
   check_balance=input("Do you want to check  balance:").lower()
   if check_balance=="yes":
     print(f"Your Balance Amount is {Balance}")
   else:
     print("THANK U!")
   next=input("Do you want to continue:").lower()
   if next=="yes":
      main()
   else:("****THANK YOU!**")

def create_Atm():
   sql ="insert into Atm_details(no,Name,Age,Gender,Account_no,Phone_no,Bank_name,Branch_name,Amount,Withdraw_amt,Balance) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   no=int(input("Enter your no:"))
   Name=input("Enter your full name:")
   Age=int(input("Enter your age:"))
   Gender=input("Enter your gender:")
   Account_no=input("Enter your account num:")
   Phone_no=input("Enter your phone num:")
   Bank_name=input("Enter your bank name:")
   Branch_name=input("Enter your branch name:")
   Amount=int(input("Enter your amount:"))
   Withdraw_amt=int(input("Enter your withdraw amount:")) 
   Balance=Amount-Withdraw_amt
   val=(no,Name,Age,Gender,Account_no,Phone_no,Bank_name,Branch_name,Amount,Withdraw_amt,Balance)
   mycursor.execute(sql,val)
   mydb.commit()
   print("DATA SAVED SUCCESSFULLY")
   #mail
   try:
     E_mail=input("Enter your mail id ")
     s=smtplib.SMTP('smtp.gmail.com',587)
     s.starttls()
     s.login("ferdinsteffi04@gmail.com","rqmhqwbtjqopadog")
     otp_number=random.randint(0000,9999)
     message=(f"Your OTP mumber is {otp_number}")
     s.sendmail("ferdinsteffi04@gmail.com",E_mail,message)
     s.quit()
     print("MAIL SEND SUCCESSFULLY")
   except:
     print("SORRY YOUR MAIL CANNOT SEND")

   verification=input("Do u recived a Otp in your mail:").lower()
   if verification=="yes":
     print("YOUR ACCOUNT CREATED SUCCESSFULLY!")
   else:
     print("SORRY!, PLEASE TRY AGAIN")

   next=input("Do you want to continue:").lower()
   if next=="yes":
     main()
   else:
     ("****THANK YOU!**")







def main():
  print("INSERT DATA PRESS---->1")
  print("CREATE ATM PRESS----->2")
  user=int(input("Enter your number:"))
  if user==1:
    insert_data()
  elif user==2:
    create_Atm()
  else:
    print("PLS PRESS 1 OR 2")

main()










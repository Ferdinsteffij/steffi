import smtplib
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid"
)
#connect db
mycursor=mydb.cursor()
#USER SECTION
def user_section():
  print("******USER SECTION******")
  def insert_data():
    sql="insert into covid_details(id,Name,Age,Gender,Aadar_num,Phone_num,E_mail,City,Dose_num,Vaccination_center,Doctor_name,Date,Time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    id=int(input("Enter your id:"))
    Name=input("Enter your full name:")
    Age=int(input("Enter your age:"))
    Gender=input("Enter your gender:")
    Aadar_num=input("Enter your aadar number:")
    Phone_num=input("Enter your phone number:")
    E_mail=input("Enter your email id:")
    City=input("Enter your current city:")
    Dose_num=input("Enter your dose num(1/2):")
    Vaccination_center=input("Enter the vaccination center:")
    Doctor_name=input("Enter the allocated doctor name:")
    Date=input("Enter the vaccination date:")
    Time=input("Enter the current time:")
    val=(id,Name,Age,Gender,Aadar_num,Phone_num,E_mail,City,Dose_num,Vaccination_center,Doctor_name,Date,Time)
    mycursor.execute(sql,val)
    mydb.commit()
    print("DATA SAVED SUCCESSFULLY!")
    #mail
    try:
      s=smtplib.SMTP('smtp.gmail.com',587)
      s.starttls()
      s.login("ferdinsteffi04@gmail.com", "nptfiaycagtcggds")
      message=(f"{Name} YOUR DATA ADDED SUCCESSFULLY!")
      s.sendmail("ferdinsteffi04@gmail.com",E_mail,message)
      s.quit()
      print("MAIL SEND SUCCESSFULLY")
    except:
      print("SORRY YOUR MAIL CANNOT SEND")
    next=input("Do you want to continue:").lower()
    if next=="yes":
      main()
    else:
      ("****THANK YOU!****")
  insert_data()

#ADMIN SECTION
def admin_section():
  print("******ADMIN SECTION******")
  #INSERT DATA
  def insert_data():
    sql="insert into covid_details(id,Name,Age,Gender,Aadar_num,Phone_num,E_mail,City,Dose_num,Vaccination_center,Doctor_name,Date,Time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    id=int(input("Enter your id:"))
    Name=input("Enter your full name:")
    Age=int(input("Enter your age:"))
    Gender=input("Enter your gender:")
    Aadar_num=input("Enter your aadar number:")
    Phone_num=input("Enter your phone number:")
    E_mail=input("Enter your email id:")
    City=input("Enter your current city:")
    Dose_num=input("Enter your dose num(1/2):")
    Vaccination_center=input("Enter the vaccination center:")
    Doctor_name=input("Enter the allocated doctor name:")
    Date=input("Enter the vaccination date:")
    Time=input("Enter the current time:")
    val=(id,Name,Age,Gender,Aadar_num,Phone_num,E_mail,City,Dose_num,Vaccination_center,Doctor_name,Date,Time)
    mycursor.execute(sql,val)
    mydb.commit()  
    #mail
    try:
      s=smtplib.SMTP('smtp.gmail.com',587)
      s.starttls()
      s.login("ferdinsteffi04@gmail.com", "nptfiaycagtcggds")
      message=(f"{Name} YOUR DATA ADDED SUCCESSFULLY!")
      s.sendmail("ferdinsteffi04@gmail.com",E_mail,message)
      s.quit()
      print("MAIL SEND SUCCESSFULLY")
    except:
      print("SORRY YOUR MAIL CANNOT SEND")
    next=input("Do you want to continue:").lower()
    if next=="yes":
      main()
    else:
      ("****THANK YOU!****")
  def view_data():
    print("****VIEW DATA*****")
    mycursor.execute("select * from covid_details")
    myresult=mycursor.fetchall()
    for i in myresult:
      print(i)
    next=input("Do you want to continue:").lower()
    if next=="yes":
      main()
    else:("****THANK YOU!****")
  def update_data():
    print("****UPDATE DATA****")
    change_data=input("What you want to change pls type like this ie. coloum name='update name':")
    FULLName=input("Enter your full name in single quotes:")
    sql=(f"update covid_details set {change_data} where Name={FULLName}")
    mycursor.execute(sql)
    mydb.commit()
    print("DATA UPDATED SUCCESSFULLY")
    next=input("Do you want to continue:").lower()
    if next=="yes":
      main()
    else:("****THANK YOU!****")
  def delete_data():
    colum_name=input("Which coloum u want to delete:")
    delete=input(f"Which data u want to delete in this {colum_name}:")
    sql=f"delete from covid_details where {colum_name}=%s"
    mycursor.execute(sql,(delete,))
    mydb.commit()
    print("DATA DELETED SUCCESSFULLY")
    next=input("Do you want to continue:").lower()
    if next=="yes":
      main()
    else:("****THANK YOU!****")

  print("INSERT DATA PRESS---->1")
  print("VIEW DATA PRESS------>2")
  print("UPDATE DATA PRESS----->3")
  print("DELETE DATA PRESS----->4")
  admin=int(input("Enter the number"))
  if admin==1:
    insert_data()
  elif admin==2:
    view_data()
  elif admin==3:
    update_data()
  elif admin==4:
    delete_data()
  else:
    print("ADMIN THANK YOU!")






  


def main(): 
  print("FOR USER SECTION PRESS---->1 ") 
  print("FOR ADMIN SECTION PRESS----->2")
  user=int(input("Enter your number:"))
  if user==1:
    user_section()
  elif user==2:
    admin_section()
  else:
    print("PLS TYPE 1 OR 2 ONLY")
main() 

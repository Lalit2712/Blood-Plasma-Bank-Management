#CODING
#PLASMA BANK MANAGEMENT SYSTEM
#About Project
#Plasma Bank Management System is the practice of collecting Plasma From Donor, Storing It Blood Group Wise & Giving It To Patients In Need.
#Plasma Bank Management System applies to every Blood Group Plasma, Keeps A Track Of Every Blood Group Plasma Received From Donors (Whether Received From COVID Recovered Patient or Non COVID Patient)
#From Collecting It From Donor, Storage Categorically Wise Of Plasma, Blood Group Wise Storage Of The Same. 

#SOFTWARE SPECIFICATION:-
#Operating System : Windows 10
#Platform : Python IDLE 3.9.4
#Database : MySQL 8.0
#Languages : Python
#NOTE :- Password For Storing Data :- "admin"
#Note: For Python-MySQL connectivity, following data have been used:-
#Host- localhost, user- root, password- ‘123456‘, database- Plasma_LNJP

# MODULES NEED TO BE IMPORTED
#BUILT_IN
import os   #OPERATING SYSTEM
import mysql.connector   # PYTHON - MYSQL- CONNECTOR
import datetime          # DATE & TIME EXTRACTED FROM YOUR COMPUTER
import random            # RANDOM VALUES WILL BE CREATED MAINLY FOR REFERENCE IDS
import time              # TIME MODULE IS DIFFERENT FROM DATE-TIME MODULE. USES FOR SLEEPING THE PROGRAM OR TO FIND TOTAL EXECUION TIME OF THE WHOLE PROJECT.
import matplotlib.pyplot as plt  # MOST IMPORTANT :- USES FOR PLOTTING OF GRAPHS,CHARTS, HISTOGRAMS OR STATISTICAL & VISUAL REPRESENTATION OF DATA.
now = datetime.datetime.now()  # IT ALWAYS PRINTS CURRENT TIME IN 24- HOURS FORMAT.
import webbrowser #FOR OPENING OUR LOGO AS IMAGE FILE. MODULE nAME IS WEBBROWSER.
#WEBBROWSER MODULE IS USED IN OPENING WEBSITES, TRIGGER APPS SUCH AS CHROME TO OPEN CERTAIN WEBSITES & CAN OPEN OTHER EXTENSION FILES.
# ORDER OF ENTERING DATE IN MYSQL OR DATE-TIME MODULE :- YYYY-MM-DD (HH:MM:SS) 

# MAIN MENU OF BLOOD PLASMA DETAILS MANAGEMENT SYSTEM
def blood_mgmt():
    clrscr()
    while True:
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t|BLOOD PLASMA DETAILS MANAGEMENT SYSTEM|")
        print("\t\t\t\t\t|************************************* |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t|S.NO| \t   OPTIONS AVAILABLE           |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 1. | \t   Add BLOOD GROUP DETAILS     |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 2. | \t   List BLOOD GROUP DETAILS    |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 3. | \t   Update DETAILS              |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 4. | \t   Delete DETAILS              |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 5. | \t  KNOW BLOOD GROUP CODES       |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 6. | \t   INVENTORY STATISTICS        |")
        print("\t\t\t\t\t========================================")
        print("\t\t\t\t\t| 7. | \t   Back (Main Menu)            |")
        print("\t\t\t\t\t========================================")
        print("\n"*7)
        print("=" * 121)
        p = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        #print("\n"*3)
        if p == 1:
            add_blood_details()
        if p == 2:
            search_blood_details()
        if p == 3:
            update_qty()
        if p == 4:
            delete_blood_details()
        if p==5:
            bloodgp_details()
        if p == 6:
            stats_blood()
        if p==7:
            break


def stats_blood():
    bloodgp=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    print("PLEASE VISIT OPTION  2 --> List BLOOD GROUP DETAILS IN BLOOD PLASMA DETAILS MANAGEMENT SYSTEM ")
    print("Order Of Entering Blood Quantity In Hand = 'A+','A-','B+','B-','O+','O-','AB+','AB-'")
    count=eval(input("Enter Number Of Units Separated By Space in a List ONLY For Each Blood Group ="))
    plt.axis("equal") #CIRCLE
    plt.pie(count,labels=bloodgp,autopct="%1.2f%%")
    plt.title("BLOOD UNITS REGISTERED WITH LNJP HOSPITAL")
    plt.show()
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()

#BLOOD GROUP CODES
def bloodgp_details():
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t|        BLOOD GROUP CODES           |")
    print("\t\t\t\t\t|*********************************** |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 101. |    A - POSITIVE (A+)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 102. |    A - NEGATIVE (A-)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 103. |    B - POSITIVE (B+)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 104. |    B - NEGATIVE (B-)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 105. |    O - POSITIVE (O+)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 106. |    O - NEGATIVE (O-)        |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 107. |    AB - POSITIVE (AB+)      |")
    print("\t\t\t\t\t======================================")
    print("\t\t\t\t\t| 108. |    AB - NEGATIVE (AB-)      |")
    print("\t\t\t\t\t======================================")
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()
    
# MAIN MENU OF BLOOD DONATION MANAGEMENT
def donation_mgmt():
    while True:
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|BLOOD PLASMA DONATION MANAGEMENT SYSTEM|")
        print("\t\t\t\t\t|************************************ |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 1. | \t   ADD NEW DONATION DETAILS  |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 2. | \t   LIST DONATIONS DETAILS    |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
        print("\t\t\t\t\t=======================================")
        print("\n"*12)
        print("=" * 121)
        o = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        print("\n"*5)
        if o == 1:
            add_donation_details()
        if o == 2:
            clrscr()
            list_donation_details()
        if o == 3:
            break


#MAIN MENU OF SALES MANAGEMENT
def request_mgmt( ):
    while True:
        print("\t\t\t\t\t============================================")
        print("\t\t\t\t\t| BLOOD PLASMA REQUEST MANAGEMENT SYSTEM   |")
        print("\t\t\t\t\t| **************************************** |")
        print("\t\t\t\t\t============================================")
        print("\t\t\t\t\t|S.NO| \t     OPTIONS AVAILABLE             |")
        print("\t\t\t\t\t============================================")
        print("\t\t\t\t\t| 1. | \t     ADD REQUEST DETAILS           |")
        print("\t\t\t\t\t============================================")
        print("\t\t\t\t\t| 2. | \t     LIST REQUESTS DETAILS         |")
        print("\t\t\t\t\t============================================")
        print("\t\t\t\t\t| 3. | \t      Back (Main Menu)             |")
        print("\t\t\t\t\t============================================")
        print("\n"*12)
        print("=" * 121)
        s = int (input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        if s == 1:
            request_blood()
        if s == 2:
            clrscr()
            list_request_details()
        if s == 3:
            break


#MAIN MENU OF USER MANAGEMENT
def user_mgmt():
    while True:
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|   DONATING USER MANAGEMENT SYSTEM   |")
        print("\t\t\t\t\t| *********************************** |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 1. | \t   REGISTER DONOR DETAILS     |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 2. | \t   LIST DONORS DETAILS        |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 3. | STATISTICS OF DONORS REGISTERED|")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 4. | \t   Back (Main Menu)           |")
        print("\t\t\t\t\t=======================================")
        print("\n"*12)
        print("=" * 121)
        u = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        if u == 1:
            add_user()
        if u == 2:
            list_user()
        if u == 3:
            statsuser()
        if u == 4:
            break
        

#Note: For Python-MySQL connectivity, following data have been used:-
#Host- "localhost", user- "root", password- ‘123456‘, database- PLASMA_LNJP
#Database setup MANAGEMENT: This module is used to setup the database in the system for the first time.
def create_database():
    mydb = mysql.connector.connect(host="localhost",user="root",password="123456")
    # mydb is variable name, mysql.connector is module --> Connect is the function of mysql.connector module
    mycursor = mydb.cursor() #TO CREATE MY SQL CURSOR VIRTUALLY IN PYTHON
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating DATABASE PLASMA_LNJP **")
    print(("=")*121)
    sql="CREATE DATABASE PLASMA_LNJP" #SQL CODE PYTHON WILL SEND THIS LINE TO SQL.
    mycursor.execute(sql) # EXECUTE FUNCTION = TO RUN MYSQL COMMANDS FROM PYTHON
    print("\t\t\t\t\t\t** DATABASE PLASMA_LNJP CREATED ** ")
    print(("=")*121)
    
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="PLASMA_LNJP")
    # WE ARE MAKING A NEW CONNECTION WITH MYSQL & CLOSING CURRENT CONNECTION
    mycursor = mydb.cursor() #TO CREATE MY SQL CURSOR VIRTUALLY IN PYTHON
    print("\t\t\t\t\t\t** Creating BLOOD_DETAILS table** ")
    print(("=")*121)
    sql = "CREATE TABLE if not exists BLOOD_DETAILS(pcode int(4) PRIMARY KEY, Blood_name varchar(30) NOT NULL,qty int(4) NOT NULL);"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** BLOOD_DETAILS Table Created** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating DONATION_DETAILS table** ")
    print(("=")*121)
    sql = "CREATE TABLE if not exists DONATION_DETAILS(Donation_id int(4)PRIMARY KEY,Donation_date DATE,pcode varchar(30) NOT NULL ,pqty int(4),DONOR_NAME varchar(50),BLOOD_GROUP char(30));"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** DONATION_DETAILS table created** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating REQUESTS table** ")
    print(("=")*121)
    sql=  "CREATE TABLE if not exists Requests(request_id int(4) PRIMARY KEY,request_date DATE,pcode varchar(30) references BLOOD_DETAILS(pcode),pqty int(4),Patient_name varchar(50) NOT NULL,DOC_NAME varchar(40) NOT NULL);"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** REQUESTS table created** ")
    sql = "CREATE TABLE if not exists user (uid varchar(100) PRIMARY KEY,uname varchar(30) NOT NULL, DOB DATE NOT NULL, BLOOD_GROUP varchar(30) NOT NULL, MOBILE varchar(25));"
    mycursor.execute(sql)
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating USER Table** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** USER Table Created** ")
    print("=" * 121)
    print("\t\t\t\t\tROLLING BACK TO PREVIOUS MENU AFTER SUCCESSFULL CREATION")
    print(("=")*121)
    time.sleep(5)
    print("\n"*5)


#TO LIST DATABASE TABLES PRESENT IN PLASMA_LNJP
def list_database():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "show tables;"  #SQL COMMAND
    print("=" * 121)
    print("=" * 121)
    print("\t\t\t\t\t===================================")
    print("\t\t\t\t\t|     DATABASE - PLASMA LNJP      |")
    print("\t\t\t\t\t| ******************************* |")
    print("\t\t\t\t\t|           TABLES LIST           |")
    print("\t\t\t\t\t| ******************************* |")
    print("\t\t\t\t\t===================================")
    mycursor.execute(sql) #SQL RETURNS ALWAYS COMES IN FORM OF LIST
    for i in mycursor:      
        print("\t\t\t\t\t|\t",i,"\t\t  |")
        print("\t\t\t\t       ","-" * 35)
    print("="*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print("=" * 121)
    time.sleep(5)
    print("\n"*10)
    

# TO CREATE A NEW ORDER FOR THE TABLE ORDER
def add_donation_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    sql = "INSERT INTO DONATION_DETAILS (Donation_id, Donation_date, pcode, pqty, Donor_name, Blood_group) values(%s,%s,%s,%s,%s,%s)"
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter Blood Group Code :"))
    print(("=")*121)
    rid = now.year+now.month+now.day+now.hour+now.minute+now.second  #2021+07+18+13+16+40 = REFERENCE ID
    qty = int(input("\t\t\t\t\t\tEnter Donated Blood Quantity (in Units) : "))
    print(("=")*121)
    cat = input("\t\t\t\t\t\tEnter Blood Group : ")
    print(("=")*121)
    donor_name = input("\t\t\t\t\t\tEnter Donor Name : ")
    print(("=")*121)
    val = (rid, now, code, qty, donor_name, cat)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t\t\t\t  DONATION SUCCESSFULLY CREATED WITH Reference ID-->",rid)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO DISPLAY DETAILS OF THE ORDER ENTERED
def list_donation_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "SELECT * from DONATION_DETAILS" # (*) Means Everything In MYSQL.
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  ORDERS DETAILS           **********************************************")
    print(("=")*121)
    print(("=")*121)
    print("-" * 121)
    print(" REFERENCE ID |\t  DATE      \t| BLOOD GROUP CODE  |   QUANTITY   |  \t DONOR NAME\t   |\t BLOOD GROUP\t|")
    print("-" * 121)
    print(("=")*121)
    for i in mycursor:
        print("  ",i[0], "\t", i[1], "\t  ","\t",i[2], "\t   \t ", i[3], "\t\t", i[4], "\t\t ", i[5], "\t\t   ")
    print("-" * 121)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# MAIN MENU FOR DATABASE MANAGEMENT SETUP
def db_mgmt( ):
    password="admin"
    print(("=")*121)
    passwd=input("\t\t\t\tENTER PASSWORD TO GET ACCESS TO DATABASE ADMINISTRATION=")
    print(("=")*121)
    if passwd== password:
        while True:
            clrscr()
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| LNJP DATABASE ADMINISTRATION SYSTEM |")
            print("\t\t\t\t\t| *********************************** |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 1. | \t   DATABASE CREATION          |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 2. | \tLIST BLOOD BANK DATA TABLES   |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
            print("\t\t\t\t\t=======================================")
            print("\n"*12)
            print("=" * 121)
            p = int(input("\t\t\t\t\t\t Enter Your Choice :"))
            print("=" * 121)
            clrscr()
            if p == 1:
                create_database()
            if p == 2:
                list_database()
            if p == 3:
                break
    else:
        print("\t\t\t\t\tWRONG PASSWORD OR PASSWORD NOT ENTERED")
        print(("=")*121)
        time.sleep(5)
        return


# TO ADD A NEW PRODUCT DETAILS
# IN PRODUCT TABLE
def add_blood_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "INSERT INTO BLOOD_DETAILS(pcode,blood_name,qty) values(%s,%s,%s)"
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter BLOOD_GROUP Code :"))
    print(("=")*121)
    search = "SELECT count(*) FROM BLOOD_DETAILS WHERE pcode=%s;" 
    val = (code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt = x[0]
    if cnt == 0:
        name = input("\t\t\t\t\t\tEnter BLOOD GROUP NAME :")
        print(("=")*121)
        qty = int(input("\t\t\t\t\t\tEnter TOTAL QUANTITY RECEIVED BY CAMP :"))
        print(("=")*121)
        val = (code,name,qty)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\t\t\t\t\t\tPRODUCT DETAILS SUCCESSFULLY ADDED")
        print("="*121)
        time.sleep(3)
        print("\n"*10)
    else:
        print("\t\t\t\t\t\tProduct Already Exists. USE UPDATE DETAILS OPTION.")
        print(("=")*121)
        print("\t\t\t\t\t\tROLLING BACK TO MAIN MENU----->")
        print(("=")*121)
        time.sleep(3)
        clrscr()


# TO UPDATE PRODUCT DETAILS
#MAINLY QUANTITY
# IN PRODUCT TABLE
def update_qty():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter the BLOOD_GROUP Code :"))
    print(("=")*121)
    qty = int(input("\t\t\t\t\t\tEnter the quantity :"))
    print(("=")*121)
    sql = "UPDATE BLOOD_DETAILS SET qty=qty+%s WHERE pcode=%s;"
    val = (qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t\t\t\t\tConsignment Details Updated")
    print(("=")*121)
    time.sleep(2)
    print("\n"*5)


# TO REMOVE COMPLETE PRODUCT DETAILS
# FROM PRODUCT TABLE
def delete_blood_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor=mydb.cursor()
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter the BLOOD_GROUP Code :"))
    print(("=")*121)
    sql = "DELETE FROM BLOOD_DETAILS WHERE pcode = %s;" 
    val = (code,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(("=")*121)
    print("\t\t\t\t\t\t",mycursor.rowcount,"record(s) deleted")
    print(("=")*121)
    time.sleep(2)
    print("\n"*10)


# TO SEARCH PRODUCT DETAILS
# IN PRODUCT TABLE
def search_blood_details():
    while True:
        print("=" * 121)
        print("|\t\t\t\t\t       OPTIONS AVAILABLE  \t\t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     1. List All Blood Group Details \t\t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     2. List Blood Group Code Wise  \t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     3. Back To Previous Menu \t\t\t\t\t\t\t|")
        print(("=")*121)
        s = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        if s == 1:
            clrscr()
            list_blood_details()
        if s == 2:
            print(("=")*121)
            code=int(input("\t\t\t\t\t\tEnter Blood Group code :"))
            clrscr()
            list_bloodprcode(code)
        if s == 3:
            clrscr()
            break


# TO LIST PRODUCT DETAILS
# IN PRODUCT TABLE
def list_blood_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "SELECT * from Blood_Details" # (*) here means all (everything)
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  PRODUCT DETAILS           *********************************************")
    print("-" * 121)
    print("\t\t BLOOD GROUP CODE |\t    BLOOD GROUP NAME     \t\t\t|\t      QUANTITY ")  # [101 ,"A+",5]
    print("-" * 121)
    
    for i in mycursor:
        print("\t\t", i[0]," |    ",i[1],"\t\t\t|", i[2],"\t|")
        print("-" * 121)
    print(("=")*121)
    sql = "SELECT qty from blood_details where pcode = '101';"   #[A+]
    mycursor.execute(sql)
    for x in mycursor:
        a_pos=x[0]
        print("TOTAL NUMBER OF A+ BLOOD GROUP UNITS IN HAND = ",a_pos)
    print("=" * 121)
    
    sql = "SELECT qty from blood_details where pcode = '102';"
    mycursor.execute(sql)
    for x in mycursor:
        a_neg=x[0]
    print("TOTAL NUMBER OF A- BLOOD GROUP UNITS IN HAND = ",a_neg)
    print("=" * 121)
    
    sql = "SELECT qty from blood_details where pcode = '103'"
    mycursor.execute(sql)
    for x in mycursor:
        b_pos=x[0]
    print("TOTAL NUMBER OF B+ BLOOD GROUP UNITS IN HAND = ",b_pos)
    print("=" * 121)

    sql = "SELECT qty from blood_details where pcode = '104'"
    mycursor.execute(sql)
    for x in mycursor:
        b_neg=x[0]
    print("TOTAL NUMBER OF B- BLOOD GROUP UNITS IN HAND = ",b_neg)
    print("=" * 121)

    sql = "SELECT qty from blood_details where pcode = '105';"
    mycursor.execute(sql)
    for x in mycursor:
        o_pos=x[0]
    print("TOTAL NUMBER OF O+ BLOOD GROUP UNITS IN HAND = ",o_pos)
    print("=" * 121)

    sql = "SELECT qty from blood_details where pcode = '106';"
    mycursor.execute(sql)
    for x in mycursor:
        o_neg=x[0]
    print("TOTAL NUMBER OF O- BLOOD GROUP UNITS IN HAND = ",o_neg)
    print("=" * 121)

    sql = "SELECT qty from blood_details where pcode = '107'"
    mycursor.execute(sql)
    for x in mycursor:
        ab_pos=x[0]
    print("TOTAL NUMBER OF AB+ BLOOD GROUP USERS REGISTERED = ",ab_pos)
    print("=" * 121)

    sql = "SELECT qty from blood_details where pcode = '108'"
    mycursor.execute(sql)
    for x in mycursor:
        ab_neg=x[0]
    print("TOTAL NUMBER OF AB- BLOOD GROUP USERS REGISTERED = ",ab_neg)
    time.sleep(5)
    clrscr()


# TO LIST PRODUCT DETAILS CODE WISE
# IN PRODUCT TABLE
def list_bloodprcode(code):
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "SELECT * from BLOOD_DETAILS WHERE pcode=%s"
    val = (code,)
    mycursor.execute(sql, val)
    print(("=")*121)
    print(("=")*121)
    print("--------------------------------------\t\t  PRODUCT DETAILS           ---------------------------------------------")
    print("-" * 121)
    print("\t\t BLOOD GROUP CODE |\t\t  BLOOD GROUP NAME         \t\t|\t      QUANTITY \t")
    print("-" * 121)
    for i in mycursor:
        print("\t\t", i[0]," |", " \t",i[1], " \t\t|", i[2],"\t|")
        print("-" * 121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO ADD DETAILS OF THE SALE PRODUCTS
# IN SALE TABLE
def request_blood():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    print(("=")*121)
    pname= input("\t\t\t\t\t\tEnter Patient Name: ")
    print(("=")*121)
    doc_name= input("\t\t\t\t\t\tEnter Doctor's Name: ")
    print(("=")*121)
    pcode = input("\t\t\t\t\t\tEnter BLOOD GROUP Code: ")
    print(("=")*121)
    sql = "SELECT count(*) from BLOOD_DETAILS WHERE pcode=%s;" 
    val = (pcode,)
    mycursor.execute(sql,val)
    for x in mycursor:
        cnt = x[0] # INDEX ALWAYS STARTS FROM 0.
    if cnt != 0 :
        sql = "SELECT * from BLOOD_DETAILS WHERE pcode=%s;"
        val = (pcode,)
        mycursor.execute(sql, val)
        for x in mycursor:
            print("\t\t\t\tDETAILS OF BLOOD WITH BLOOD GROUP CODE",pcode,"ARE AS FOLLOWS-->")
            print(("=")*121)
            print(("-")*121)
            print("\t\t\t\t\t\tBLOOD GROUP CODE =",x[0])
            print(("-")*121)
            print("\t\t\t\t\t\tBLOOD GROUP NAME =",x[1])
            print(("-")*121)
            print("\t\t\t\t\t\tQUANTITY IN HAND=",x[2]) #3
            print(("-")*121)
            pqty = int(x[2])
            print(("=")*121)
            qty = int(input("\t\t\t\t\t\tEnter Quantity To Be Sanctioned To Patient :")) #3
            if qty <= pqty:  
                print(("=")*121)
                request_id = random.randint(1000,99999) # Randint = GIVES ONLY INTEGRAL RANDOM NUMBER IN PARTICULAR RANGE.
                print("\t\t\t\t\tREQUEST CREATED SUCCESSFULLY WITH REQUEST ID=",request_id)
                sql = "INSERT into REQUESTS values(%s,%s,%s,%s,%s,%s)"
                val = (request_id,datetime.datetime.now(),pcode,qty,pname,doc_name)
                mycursor.execute(sql,val)
                sql = "UPDATE BLOOD_DETAILS SET qty=qty-%s WHERE pcode=%s"
                val = (qty, pcode)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                print(("=")*121)
                print("\t\t\t\t\t\tREQUESTED QUANTITY NOT AVAILABLE.")
                print(("=")*121)
                print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
                print(("=")*121)
                time.sleep(5)
                clrscr()
                return
        else:
            print(("=")*121)
            print("\t\t\t\t\t\tTHANK YOU. MAY YOU GET WELL SOON.")
            print(("=")*121)
            print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
            print(("=")*121)
            time.sleep(5)
            clrscr()


# TO LIST DETAILS OF THE SALE PRODUCTS
# FROM SALE TABLES
def list_request_details():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM REQUESTS"
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  BLOOD PLASMA REQUESTS DETAILS         *************************************************")
    print(("=")*121)
    print(("=")*121)
    print("-" * 121)
    print("  REQUEST ID  |\t   DATE       \t|   BLOOD GROUP CODE    |    QUANTITY    | PATIENT'S NAME |  DOCTOR'S NAME  | ")
    print("-" * 121)
    print(("=")*121)
    for x in mycursor:
        print("  ",x[0], "\t", x[1], "\t\t ", x[2], "\t\t\t", x[3], "\t\t", x[4], "\t\t   ", x[5])
        print("-"*121)
    print("-" * 121)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()




# TO ADD DETAILS OF ANY NEW USER
# TABLE- USER
def add_user():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    passwd="admin"
    print("=" * 121)
    uid = input("\t\t\t\t\t\tENTER EMAIL ID OF DONOR :")
    print("=" * 121)
    name =input("\t\t\t\t\t\tENTER NAME OF DONOR :")
    print("=" * 121)
    dob = input("\t\t\t\t\t\tENTER DOB OF DONOR (yyyy-mm-dd) :")
    print("=" * 121)
    bloodgp=input("\t\t\t\t\t\tENTER BLOOD GROUP OF DONOR  :")
    print("=" * 121)
    mobile= input("\t\t\t\t\t\tENTER CONTACT NUMBER OF DONOR  :")
    print("=" * 121)
    password = input("\t\t\t\t\tENTER PASSWORD TO REGISTER & SAVE DONOR DETAILS :")
    print("=" * 121)
    if passwd==password:
        print("\t\t\t\t\t\tSTORING DATA AND REGISTERING USER")
        sql = "INSERT INTO user values (%s,%s,%s,%s,%s);"  #SQL COMMAND
        val = (uid, name,dob,bloodgp,mobile)
        mycursor.execute(sql, val)
        mydb.commit() #IMPORTANT -- TO STORE DATA IN MYSQL PERMANANTLY  #AUTOMATICALLY ON IN MYSQL
        print(("=")*121)
        print("\t\t\t\t\t\t",mycursor.rowcount, "DONOR REGISTERED.")
        print("=" * 121)
        print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
        print("=" * 121)
        time.sleep(5)
        clrscr()
    else:
        print("=" * 121)
        print("\t\t\t\t\t\tWRONG PASSWORD OR PASSWORD NOT ENTERED")
        print("=" * 121)
        print("\t\t\t\t\t\tDONOR NOT REGISTERED")
        print("=" * 121)
        print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
        print("=" * 121)
        time.sleep(5)
        clrscr()

# LIST ALL THE DETAILS OF THE USER.
def list_user():
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="PLASMA_LNJP")
    mycursor = mydb.cursor()
    sql = "SELECT uid, uname, dob,BLOOD_GROUP,mobile  from user" #SQL COMMAND 
    mycursor.execute(sql)
    clrscr()
    print(("=")*121)
    print(("=")*121)
    print("--------------------------------------\t\t     USER DETAILS           ---------------------------------------------")
    print("-" * 121)
    print("|\tEMAIL ID\t\t|\tDONOR NAME\t\t|   DATE OF BIRTH\t|BLOOD GROUP|\t\t\t\tMOBILE\t|")
    print("-" * 121)
    for i in mycursor:
        print("|",i[0],"\t|","\t",i[1],"\t|","\t",i[2],"  |","\t",i[3],"  |","\t\t",i[4])
        print("-" * 121)
    print("=" * 121)
    
    sql = "SELECT count(*) from user where blood_group = 'A+';"
    mycursor.execute(sql)
    for x in mycursor:
        a_pos=x[0]
        print("TOTAL NUMBER OF A+ BLOOD GROUP USERS REGISTERED = ",a_pos)
    print("=" * 121)
    
    sql = "SELECT count(*) from user where blood_group = 'A-'"
    mycursor.execute(sql)
    for x in mycursor:
        a_neg=x[0]
    print("TOTAL NUMBER OF A- BLOOD GROUP USERS REGISTERED = ",a_neg)
    print("=" * 121)
    
    sql = "SELECT count(*) from user where blood_group = 'B+'"
    mycursor.execute(sql)
    for x in mycursor:
        b_pos=x[0]
    print("TOTAL NUMBER OF B+ BLOOD GROUP USERS REGISTERED = ",b_pos)
    print("=" * 121)

    sql = "SELECT count(*) from user where blood_group = 'B-'"
    mycursor.execute(sql)
    for x in mycursor:
        b_neg=x[0]
    print("TOTAL NUMBER OF B- BLOOD GROUP USERS REGISTERED = ",b_neg)
    print("=" * 121)

    sql = "SELECT count(*) from user where blood_group = 'O+';"
    mycursor.execute(sql)
    for x in mycursor:
        o_pos=x[0]
    print("TOTAL NUMBER OF O+ BLOOD GROUP USERS REGISTERED = ",o_pos)
    print("=" * 121)

    sql = "SELECT count(*) from user where blood_group = 'O-';"
    mycursor.execute(sql)
    for x in mycursor:
        o_neg=x[0]
    print("TOTAL NUMBER OF O- BLOOD GROUP USERS REGISTERED = ",o_neg)
    print("=" * 121)

    sql = "SELECT count(*) from user where blood_group = 'AB+'"
    mycursor.execute(sql)
    for x in mycursor:
        ab_pos=x[0]
    print("TOTAL NUMBER OF AB+ BLOOD GROUP USERS REGISTERED = ",ab_pos)
    print("=" * 121)

    sql = "SELECT count(*) from user where blood_group = 'AB-'"
    mycursor.execute(sql)
    for x in mycursor:
        ab_neg=x[0]
    print("TOTAL NUMBER OF AB- BLOOD GROUP USERS REGISTERED = ",ab_neg)
    
    print("=" * 121)
    print("\n"*2)
    print("=" * 121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print("=" * 121)
    time.sleep(5)
    clrscr()

def statsuser():
    bloodgp=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    print("FOR NUMBER OF DONORS PLEASE VISIT OPTION 2 FIRST IN BLOOD DONORS USER MANAGEMENT ")
    print("Order Of Entering Blood Donors = 'A+','A-','B+','B-','O+','O-','AB+','AB-'")
    count=eval(input("Enter Number Of Donors Separated By Space in a List ONLY For Each Blood Group ="))
    plt.axis("equal")   #THIS WILL MAKE A CIRCLE 
    plt.pie(count,labels=bloodgp,autopct="%1.2f%%")  #MAKE THE PIE CHART (LABELS=BLOODGP WILL MAP THE VALUES)
    plt.title("DONORS REGISTERED WITH LNJP HOSPITAL")
    plt.show()
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()

# CLEAR THE SCREEN
def clrscr():  #def is the keyword "clrscr" is function name.
    print("\n"*49)

# MAIN FUNCTION = PARENT FUNCTION
webbrowser.open(r'C:\Users\s\Desktop\SEMESTER 2\PPS PROJECT & THEORY\solutions.png')
# WE ARE USING WEBBROWSER MODULE OPEN FUNCTION TO OPEN OUR IMAGE FILE.
time.sleep(6)
while True:  # MOST IMPORTANT
    clrscr()
    print("\t\t\t\t==============================================================")  
    print("\t\t\t\t|                  PLASMA BANK MANAGEMENT SYSTEM             |")
    print("\t\t\t\t|                *********************************           |")
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|S.NO|               AVAILABLE CHOICES                       |")
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  1.| BLOOD PLASMA CENTRALIZED STORAGE FACILITY             |")# IT REFERS TO DETAILS OF CENTRALIZED WHERE ALL BLOOD BANK CAMPS NEED TO SUBMIT BLOOD AND UPDATE QUANTITY FOR SAME.
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  2.| BLOOD PLASMA DONATION SYSTEM (FOR CAMPS)              |")# IT REFERS TO DETAILS OF BLOOD RECEIVED BY BLOOD CAMPS
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  3.| BLOOD PLASMA REQUEST MANGEMENT (FOR PATIENTS)         |")# IT REFERS TO DETAILS OF TRANSACTIONS IN WHICH BLOOD UNITS ARE SANCTIONED TO PATIENTS
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  4.| BLOOD DONORS USER MANAGEMENT                          |")# IT REFERS TO THE DONORS PERSONAL DETAILS
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  5.| LNJP'S BLOOD BANK DATABASE ADMINISTRATION             |")# IT REFERS TO THE MAIN FUNCTIONING DATABASE IN WHICH ALL DETAILS ARE STORED.
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  6.| EXIT                                                  |")# IT Will Close The Function 
    print("\t\t\t\t==============================================================")
    print(("=")*121)
    print("    |NOTE| IF YOU ARE USING THIS PROGRAM FOR FIRST TIME THEN PLEASE FIRSTLY SELECT OPTION '5' 'LNJP'S BLOOD BANK DATABASE ADMINISTRATION'")
    print(("=")*121)
    print("\n"*5) # IT LEAVES 5 LINES BLANK AND THEN PRINT OUTPUT
    print("=" * 121)
    n = int(input("\t\t\t\t\t\tEnter your choice :"))  #INPUT CHOICE OF n
    print("=" * 121)
    if n == 1:
        clrscr()
        blood_mgmt()
    if n == 2:
        clrscr()
        os.system('cls') # OPERATING SYSTEM MODULE --> 'SYSTEM' NAME KA FUNCTION --> CLS SUB-FUNCTION OF SYSTEM --> CLS WILL ASK OS TO RELEASE MEMORY FOR ONGOING PROGRAM
        donation_mgmt()
    if n == 3:
        clrscr()
        request_mgmt()
    if n == 4:
        clrscr()
        user_mgmt()
    if n == 5:
        clrscr()
        db_mgmt()
    if n == 6:
        clrscr()
        print(" \t\t                    THANK YOU FOR USING LNJP BLOOD PLASMA BANK MANAGEMENT SYSTEM")
        print("=" * 121)
        print(" \t\t                              PROGRAMMED & DESIGNED BY ---> ")
        print("=" * 121)
        print("\t\t                        ==================================================== ")
        print("\t\t                                  NAME           BATCH            PRN       ")
        print("\t\t                        ==================================================== ")
        print(" \t\t                            LALIT SHROTRIYA  --  CS-A3   --   20070122067   ")
        print(" \t\t                            OJAS INAMDAR     --  CS-A3   --   20070122055   ")
        print(" \t\t                            JINISHA BADALA   --  CS-A3   --   20070122060   ")
        print(" \t\t                            KANISHK GUPTA    --  CS-A3   --   20070122061   ")
        print(" \t\t                            HARSH PAGARE     --  CS-A3   --   20070122048   ")
        print("\t\t                        ==================================================== ")
        print("=" * 121)
        print(" \t\t                        PPSL PROJECT WORK - (SEMESTER = 2) (Batch - 2020-24) FIRST YEAR")
        print("=" * 121)
        print("=" * 121)
        print(" \t\t                                SYMBIOSIS INSTITUTE OF TECHNOLOGY           ")
        print(" \t\t\t   UNDER CONSTITUENT OF SYMBIOSIS INTERNATIONAL (DEEMED UNIVERSITY),PUNE - MAHARASHTRA.")
        print("=" * 121)
        print(" \t\t                                     SUPERVISED BY-")
        print("\t\t                                    DR. SUDHANSHU GONGE")
        print("\t\t                     Assistant Professor, Department of Computer Science & IT")
        print("=" * 121)
        print("\n"*3)
        time.sleep(15)  #TIME IS THE MODULE --> SLEEP IS THE FUNCTION --> (15--SECONDS THE PROGRAM WILL STOP FOR 15 SECONDS)
        break           # STOP LOOP IN DELIBERATE MANNER & COME OUT OF THE LOOP.
#PROGRAM OVER.......

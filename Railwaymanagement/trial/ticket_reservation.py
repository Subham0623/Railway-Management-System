from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import os
import datetime
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='', db='trs', port='3306')


def pnr():
    num = str(input("Enter the PNR number  :  "))
    if (num.isdigit()):
        sql = "SELECT * FROM user WHERE pnr =" + num
        myc = mydb.cursor(buffered=True, dictionary=True)
        myc.execute(sql)
        myresult = myc.fetchall()
        if myresult:
            for x in myresult:
                data = str(x)
                data = data.replace("'", "")
                data = data.replace("{", "")
                data = data.replace("}", "")
                data = data.replace(",", "\n")
                print("\nYour PNR status is : \n", data, "\n")
        else:
            print("Sorry no status found with PNR number : ", num)

    else:
        print("Please input numbers only")

    rtry = int(input("1. for try again\n2. for main menu\n"))
    if rtry == 1:
        pnr()
    elif rtry == 2:
        pass


def ticketGenrate():
    os.system("Title ID CARD")
    list1 = ["Gomti Exp.", "Lichhwi Exp.", "Hamsafar Exp.", "Poorva Exp,.", "Janta Exp.", "Durnto Exp.",
             "Shatabdi Exp."]

    print('\n\nWe Require Some Details of you')

    title = 'Indian Railways Wishing You A Happy Journey'

    subtitle = 'This is online generated ticket'

    idno = random.randint(1000, 9000)
    message = str('19220' + str(idno))

    rdate = str(date.strftime("  %d-%m-%Y %I:%M:%S %p"))
    name = input('Enter Your Full Name: ')

    jfrom = 'Ghaziabad'

    Gender = input('Enter Your Gender: ')

    jto = input('Enter your destination : ')

    dob = input('Enter Your age: ')
    price = str(len(jto) * 35);

    bg = input('Enter Your Blood Group: ')
    tno = str(len(jto) * 35 + idno);
    mob = input('Enter Your Mobile Number: ')
    tn = str(random.choice(list1));
    cn = str(random.randint(11000, 91000))
    sn = str(random.randint(10, 100)
             )
    doj = datetime.datetime.today() + datetime.timedelta(days=random.randint(5, 30))
    doj = str(doj.strftime("%d/%m/%Y  %I:%M %p"))

    Address = input('Enter Your Address: ')

    myc = mydb.cursor(buffered=True)
    query = "INSERT INTO user(pnr,name,gender,age,bg,mobile,cn,address,rdate,jf,jto,fare,tno,tna,sn,doj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (message, name, Gender, dob, bg, mob, cn, Address, rdate, jfrom, jto, price, tno, tn, sn, doj)
    sql = myc.execute(query, data)
    c = mydb.commit()
    di = (sql, c)
    if (di):
        print("DAta INserted SUccessfully\n")
    else:
        print("no Data INserTEd\n")
    input('\nPress any key to main menu')  # use input yo hold the screen


date = datetime.datetime.now()
formatdate = date.strftime("%d/%m/%Y\t\t\t\t\tTicket Reservation System\t\t\t\t\t%I:%M:%S%p")
print(
    '**************************************************************************************************************************')
print(formatdate)
print(
    '**************************************************************************************************************************')

restart = ('Y')
while restart != ('N', 'NO', 'n', 'no'):

    print("\n\n1.Check pnr status")
    print("2.Ticket Reservation")
    print("3.Exit")
    option = int(input("\nEnter your option : "))

    if option == 1:
        pnr()

    elif option == 2:
        ticketGenrate()

    elif option == 0:
        exit()
from binhex import openrsrc

from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import os
import datetime
import mysql.connector


mydb=mysql.connector.connect(host='localhost',user='root',password='',db='crop',port='3306')



def pnr():
    num = str(input("Enter the PNR number  :  "))
    if (num.isdigit()):
        sql = "SELECT * FROM user WHERE pnr ="+num
        myc = mydb.cursor(buffered=True,dictionary=True)
        myc.execute(sql)
        myresult = myc.fetchall()
        if myresult:
            for x in myresult:
                data = str(x)
                data=data.replace("'","")
                data=data.replace("{","")
                data=data.replace("}","")
                data=data.replace(",","\n")
                print("\nYour PNR status is : \n",data,"\n")
        else:
            print("Sorry no status found with PNR number : ",num)

    else:
        print("Please input numbers only")

    rtry = int(input("1. for try again\n2. for main menu\n"))
    if rtry ==1:
        pnr()
    elif rtry==2:
        pass




def ticketGenrate():
    image = Image.new('RGB', (1920, 720), (255, 255, 255))  # properties of new image to be saved
    draw = ImageDraw.Draw(image)  # saving a new blank image to work it on

    # Change arial  to any other like Calibri, Its up to you
    font = ImageFont.truetype('arial', size=45)

    os.system("Title ID CARD")
    list1 = ["Gomti Exp.", "Lichhwi Exp.", "Hamsafar Exp.", "Poorva Exp,.", "Janta Exp.", "Durnto Exp.", "Shatabdi Exp."]


    print('\n\nWe Require Some Details of you')

    # to store information of college
    (x, y) = (560, 50)
    # college = input('\nEnter Your College Name: ')
    title = 'Indian Railways Wishing You A Happy Journey'
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial', size=42)
    draw.text((x, y), title, fill=color, font=font)

    # to store information of college address
    (x, y) = (700, 95)
    # college = input('\nEnter Your College Address: ')
    subtitle = 'This is online generated ticket'
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial', size=38)
    draw.text((x, y), subtitle, fill=color, font=font)

    # adding an unique id number using random finction and concatinating string
    (x, y) = (50, 250)
    idno = random.randint(1000, 9000)
    message = str('19220' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial', size=30)
    draw.text((x, y), 'PNR No. ' + message, fill=color, font=font)

    (x, y) = (500, 250)
    rdate = str(date.strftime("  %d-%m-%Y %I:%M:%S %p"))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Reservation date  -  ' + date.strftime("  %d-%m-%Y %I:%M:%S %p"), fill=color, font=font)

    # to get user enterd information
    (x, y) = (50, 300)
    name = input('Enter Your Full Name: ')
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial', size=30)
    draw.text((x, y), 'Name - ' + name, fill=color, font=font)

    (x, y) = (500, 300)
    jfrom = 'Ghaziabad'
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), "Journey from  -  "+jfrom, fill=color, font=font)

    (x, y) = (50, 350)
    Gender = input('Enter Your Gender: ')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Gender  -  ' + Gender, fill=color, font=font)

    (x, y) = (500, 350)
    jto = input('Enter your destination : ')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Journey to  -  ' +jto, fill=color, font=font)

    (x, y) = (50, 400)
    dob = input('Enter Your age: ')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Age  -  ' + dob, fill=color, font=font)

    (x, y) = (500, 400)
    price = str(len(jto) * 35);
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Fare  -  ' + price, fill=color, font=font)

    (x, y) = (50, 450)
    bg = input('Enter Your Blood Group: ')
    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), 'Blood Group  -  ' + bg, fill=color, font=font)

    (x, y) = (500, 450)
    tno = str(len(jto) * 35 + idno);
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Train No.  -  ' + tno, fill=color, font=font)

    (x, y) = (50, 500)
    mob = input('Enter Your Mobile Number: ')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Mobile  -  ' + mob, fill=color, font=font)

    (x, y) = (500, 500)
    tn = str(random.choice(list1));
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Train Name.  -  ' + tn, fill=color, font=font)

    (x, y) = (50, 550)
    cn = str(random.randint(11000, 91000))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Coach No.  -  ' + cn, fill=color, font=font)

    (x, y) = (500, 550)
    sn = str(random.randint(10, 100))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Seat No.  -  ' + sn, fill=color, font=font)

    (x, y) = (500, 600)
    doj = datetime.datetime.today() + datetime.timedelta(days=random.randint(5, 30))
    doj = str(doj.strftime("%d/%m/%Y  %I:%M %p"))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Date & time of Journey.  -  ' + doj, fill=color, font=font)

    (x, y) = (50, 600)
    Address = input('Enter Your Address: ')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'Address  -  ' + Address, fill=color, font=font)

    # save the edited image in current directory.
    image.save(str(name) + '.png')

    # this info. is added in QR code, also add other things in str function
    img = qrcode.make(str('PNR No. ' + message) + str('\nName - ' + name) + str('\nCoach No.  -  ' + cn, ) +
                      str('\nSeat No.  -  ' + sn) + str('\nTrain No.  -  ' + tno) + str('\nTrain Name.  -  ' + tn) + str('\nDate & time of Journey.  -  ' + doj))
    img.save(str(idno) + '.bmp')

    # open saved named file and save it to final image
    til = Image.open(name + '.png')

    # open saved qr code to save it on final image
    im = Image.open(str(idno) + '.bmp')

    # ph=Image.open('ds.jpg')#to open ds named photo


    til.paste(im, (1300, 100))  # pasted image on named file
    til.save(name + message + '.png')  # saving name image with Qr as final image


    # #to insert data in DB
    myc = mydb.cursor(buffered=True)
    query ="INSERT INTO user(pnr,name,gender,age,bg,mobile,cn,address,rdate,jf,jto,fare,tno,tna,sn,doj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (message,name,Gender,dob,bg,mob,cn,Address,rdate,jfrom,jto,price,tno,tn,sn,doj)
    sql=myc.execute(query,data)
    c=mydb.commit()
    di=(sql,c)
    if (di):
        print("DAta INserted SUccessfully\n")
    else:
        print("no Data INserTEd\n")



    print('\nYour Ticket Successfully generated in a PNG file ' + name + message + '.png')
    img = Image.open(name + message + '.png')
    img.show()
    input('\nPress any key to main menu')  # use input yo hold the screen


print("\n\nWelcome! To Ticket Booking System\n")
date = datetime.datetime.now()
formatdate = date.strftime("  %d-%m-%Y\t\t\tTicket Reservation System\t\t\t%I:%M:%S %p")
print(
    '***********************************************************************************')
print(formatdate)
print(
    '********************************BY DANISH MCA**************************************')

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
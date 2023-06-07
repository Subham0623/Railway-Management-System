import tkinter
import tkinter.messagebox
from tkinter import *
import mysql.connector
bgcolor="#5aa7a7"
font1 = ("Courier", 14)
fontcolor="white"

class Information:
    def __int__(self, time,trainid,stationname,trainname):
        self.time = time
        self.trainid = trainid
        self.stationname = stationname
        self.trainname = trainname

# admin delete pages
class Admin_delete_scheduleoftrain(Information):
    def __int__(self, time, trainid, stationname, trainname,departure,destination):
        super().__int__(self, time,trainid,stationname,trainname)
        self.destination = destination
        self.departure = departure
    def display(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Delete Schedule of train")
        window.config(bg=bgcolor)

        l = Label(window, text="Train Id")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=1, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        l = Label(window, text="Train Name")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=3, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=4, sticky='w')
        l = Label(window, text="Destination")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=5, sticky='w', pady=2)
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=6, sticky='w')
        l = Label(window, text="Departure")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=7, sticky='w', pady=2)

        def check():
            self.trainid = traid.get()


            if ( not (self.trainid and self.trainid.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a = Admin_delete_scheduleoftrain()

                a.display()

            else:
                connection = mysql.connector.connect(host='localhost',
                                                     database='railway',
                                                     user='root',
                                                     password='')

                mycursor = connection.cursor()
                sql = """SELECT * FROM `scheduleoftrain`
                             WHERE `trainid` = %s
                  """
                self.trainid = self.trainid.strip('\n')

                adr = (self.trainid, )
                mycursor.execute(sql, adr)
                # fetch result
                record = mycursor.fetchall()
                a = mycursor.rowcount

                if(a>0):
                    connection = mysql.connector.connect(host='localhost',
                                                         database='railway',
                                                         user='root',
                                                         password='')

                    mycursor = connection.cursor()
                    sql = "DELETE FROM scheduleoftrain WHERE trainid =%s"
                    adr = (f"{self.trainid}",)

                    mycursor.execute(sql,adr)

                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "Successfully deleted")
                    window.destroy()

                    a = Admin_delete_scheduleoftrain()

                    a.display()

                else:
                    tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                    window.destroy()

                    a = Admin_delete_scheduleoftrain()

                    a.display()
        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        sql = """SELECT * FROM `scheduleoftrain`
                                      """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a = 0

        for row in record:
            self.trainid = row[0]
            l = Label(window, text=f"{self.trainid}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=1, sticky='w', pady=2)
            self.trainname = row[1]
            l = Label(window, text=f"{self.trainname}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=3, sticky='w', pady=2)
            self.destination = row[2]
            l = Label(window, text=f"{self.destination}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=5, sticky='w', pady=2)
            self.departure = row[3]
            l = Label(window, text=f"{self.departure}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=7, sticky='w', pady=2)
            a += 1
        label=tkinter.Label(window, text="Enter the train id to delete", font=("Courier", 10))
        label.config(bg=bgcolor,foreground=fontcolor)
        label.grid(row=0, column=3)
        traid = tkinter.Entry(window, font=font1, fg=bgcolor)
        traid.grid(row=1, column=3, sticky="e")
        btn = Button(window, text='Delete', bd='5', fg=bgcolor,
                     command=lambda: [check()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=1, column=5, sticky="w")
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=7, sticky="e", pady=5)
        window.mainloop()




class Admin_delete_traininfo(Information):
    def __int__(self, time, trainid, stationname, trainname,travel):
        super().__int__(self, time,trainid,stationname,trainname)
        self.travel=travel

    def display(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Delete Schedule of train")
        window.config(bg=bgcolor)

        l = Label(window, text="Train Id")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=1, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        l = Label(window, text="Train Name")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=3, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=4, sticky='w')
        l = Label(window, text="Travelling route")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=5, sticky='w', pady=2)
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=6, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=7, sticky='w')


        def check():
            self.trainid = traid.get()


            if ( not (self.trainid and self.trainid.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a = Admin_delete_traininfo()

                a.display()

            else:
                connection = mysql.connector.connect(host='localhost',
                                                     database='railway',
                                                     user='root',
                                                     password='')

                mycursor = connection.cursor()
                sql = """SELECT * FROM `traininfo`
                             WHERE `trainid` = %s
                  """
                self.trainid = self.trainid.strip('\n')

                adr = (self.trainid, )
                mycursor.execute(sql, adr)
                # fetch result
                record = mycursor.fetchall()
                a = mycursor.rowcount

                if(a>0):
                    connection = mysql.connector.connect(host='localhost',
                                                         database='railway',
                                                         user='root',
                                                         password='')

                    mycursor = connection.cursor()
                    sql = "DELETE FROM traininfo WHERE trainid =%s"
                    adr = (f"{self.trainid}",)

                    mycursor.execute(sql,adr)

                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "Successfully deleted")
                    window.destroy()

                    a = Admin_delete_traininfo()

                    a.display()

                else:
                    tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                    window.destroy()

                    a = Admin_delete_traininfo()

                    a.display()
        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        sql = """SELECT * FROM `traininfo`
                                      """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a = 0

        for row in record:
            self.trainid = row[0]
            l = Label(window, text=f"{self.trainid}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=1, sticky='w', pady=2)
            self.trainname = row[1]
            l = Label(window, text=f"{self.trainname}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=3, sticky='w', pady=2)
            self.travel = row[2]
            l = Label(window, text=f"{self.travel}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=5, sticky='w', pady=2)

            a += 1
        label=tkinter.Label(window, text="Enter the train id to delete", font=("Courier", 10))
        label.config(bg=bgcolor,foreground=fontcolor)
        label.grid(row=0, column=3)
        traid = tkinter.Entry(window, font=font1, fg=bgcolor)
        traid.grid(row=1, column=3, sticky="e")
        btn = Button(window, text='Delete', bd='5', fg=bgcolor,
                     command=lambda: [check()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=1, column=5, sticky="w")
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=5, sticky="e", pady=5)
        window.mainloop()
class Admin_delete_stationinfo(Information):
    def __int__(self, time, trainid, stationname, trainname,stationid):
        super().__int__(self, time,trainid,stationname,trainname)
        self.stationid=stationid
    def display(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Delete Schedule of train")
        window.config(bg=bgcolor)

        l = Label(window, text="Station Id")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=1, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        l = Label(window, text="Station Name")
        l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=3, sticky='w')
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=4, sticky='w')
        l = Label(window, text="Train Id")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=5, sticky='w', pady=2)
        l = Label(window, text=" ")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=6, sticky='w')
        l = Label(window, text="Train Name")
        l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=7, sticky='w', pady=2)

        def check():
            self.stationid = staid.get()


            if ( not (self.stationid and self.stationid.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a = Admin_delete_stationinfo()

                a.display()

            else:
                connection = mysql.connector.connect(host='localhost',
                                                     database='railway',
                                                     user='root',
                                                     password='')

                mycursor = connection.cursor()
                sql = """SELECT * FROM `stationinfo`
                             WHERE `stationid` = %s
                  """
                self.stationid = self.stationid.strip('\n')

                adr = (self.stationid, )
                mycursor.execute(sql, adr)
                # fetch result
                record = mycursor.fetchall()
                a = mycursor.rowcount

                if(a>0):
                    connection = mysql.connector.connect(host='localhost',
                                                         database='railway',
                                                         user='root',
                                                         password='')

                    mycursor = connection.cursor()
                    sql = "DELETE FROM stationinfo WHERE stationid =%s"
                    adr = (f"{self.stationid}",)

                    mycursor.execute(sql,adr)

                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "Successfully deleted")
                    window.destroy()

                    a = Admin_delete_stationinfo()

                    a.display()

                else:
                    tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                    window.destroy()

                    a = Admin_delete_stationinfo()

                    a.display()
        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        sql = """SELECT * FROM `stationinfo`
                                      """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a = 0

        for row in record:
            self.stationid = row[0]
            l = Label(window, text=f"{self.stationid}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=1, sticky='w', pady=2)
            self.stationname = row[1]
            l = Label(window, text=f"{self.stationname}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=3, sticky='w', pady=2)
            self.trainid = row[2]
            l = Label(window, text=f"{self.trainid}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=5, sticky='w', pady=2)
            self.trainname = row[3]
            l = Label(window, text=f"{self.trainname}")
            l.config(font=font1, bg=bgcolor, foreground=fontcolor)
            l.grid(row=3 + a, column=7, sticky='w', pady=2)
            a += 1
        label=tkinter.Label(window, text="Enter the Station id to delete", font=("Courier", 10))
        label.config(bg=bgcolor,foreground=fontcolor)
        label.grid(row=0, column=3)
        staid = tkinter.Entry(window, font=font1, fg=bgcolor)
        staid.grid(row=1, column=3, sticky="e")
        btn = Button(window, text='Delete', bd='5', fg=bgcolor,
                     command=lambda: [check()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=1, column=5, sticky="w")
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=7, sticky="e", pady=5)
        window.mainloop()
# viewer page
class Scheduleoftrain(Information):

    def __int__(self, time, trainid, stationname, trainname):
        super().__int__(self, time,trainid,stationname,trainname)
    def display(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Schedule if train")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Schedule of trains", font=("Courier", 20))
        label.config(bg=bgcolor,foreground=fontcolor)
        label.grid(row=0, column=1, padx=20,sticky=W, pady=50)


        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')


        mycursor = connection.cursor()
        sql = """SELECT * FROM `scheduleoftrain`
                          """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a=0
        b=0
        for row in record:
            a+=1

            if a<3:
                l = Label(window, text=f"")
                l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
                l.grid(row=0 + b, column=2, sticky='w', pady=2)

                l = Label(window, text=f"Train {a}:")
                l.config(font= ("Courier", 18,"bold"), height=1, width=9, bg=bgcolor,foreground=fontcolor)
                l.grid(row=1 + b, column=2, sticky='w', pady=2)

                l = Label(window, text="Train ID:")
                self.trainid=row[0]
                l.config(font=font1,  bg=bgcolor,foreground=fontcolor)
                l.grid(row=2+b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainid}")
                l.config(font=font1, bg=bgcolor,foreground=fontcolor)
                l.grid(row=2+b, column=3, sticky='w', pady=2)

                l = Label(window, text="Train Name:")
                self.trainname= row[1]
                l.config(font=font1, bg=bgcolor,foreground=fontcolor)
                l.grid(row=3+b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainname}")
                l.config(font=font1,  bg=bgcolor,foreground=fontcolor)
                l.grid(row=3+b, column=3,sticky='w', pady=2)

                l = Label(window, text="Destination:")
                l.config(font=font1,  bg=bgcolor,foreground=fontcolor)
                l.grid(row=4+b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{row[2]}")
                l.config(font=font1, bg=bgcolor,foreground=fontcolor)
                l.grid(row=4+b, column=3, sticky='w', pady=2)
                self.time=row[3]
                l = Label(window, text="Depature Time:")
                l.config(font=font1, bg=bgcolor,foreground=fontcolor)
                l.grid(row=5+b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{self.time}")
                l.config(font=font1,   bg=bgcolor,foreground=fontcolor)
                l.grid(row=5+b, column=3, sticky='w', pady=2)

            b+=6
        btn = Button(window, text='Back', bd='5',fg=bgcolor,
                     command=lambda :[window.destroy(),homepage()])
        btn.config(font=("Courier", 8), height=-1, width=5, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
        btn.grid(row=0, column=4, sticky="e", pady=5)
        window.mainloop()

# admin page
class Admin_add_scheduleoftrain(Information):
    def __int__(self, time, trainid, stationname, trainname, destination,departure):
        super().__int__(self, time, trainid, stationname, trainname)
        self.destination = destination
        self.departure = departure

    def display(self):
        window = tkinter.Tk()
        window.geometry('800x540')
        window.title("Add Train information")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Add Train information", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)

        def check():
            self.departure = departure.get()
            self.destination = destination.get()
            self.trainid = traid.get()
            self.trainname = traname.get()

            if (not (self.departure and self.departure.strip())
                    or not (self.destination and self.destination.strip())
                    or not (self.trainid and self.trainid.strip())
                    or not (self.trainname and self.trainname.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a = Admin_add_scheduleoftrain()

                a.display()

            else:
                insert()
                tkinter.messagebox.showinfo("Success", "Data successfully added")
                window.destroy()
                a = Admin_add_scheduleoftrain()
                a.display()

        def insert():
            connection = mysql.connector.connect(host='localhost',
                                                 database='railway',
                                                 user='root',
                                                 password='')

            mycursor = connection.cursor()
            sql = "INSERT INTO scheduleoftrain (trainid, trainname,destination,departuretime) VALUES (%s, %s,%s,%s)"
            val = (f"{self.trainid}", f"{self.trainname}", f"{self.destination}",f"{self.departure}")
            mycursor.execute(sql, val)
            connection.commit()
            print("Done")

        l = Label(window, text=""
                               "Enter the Travelling Train Name:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        traname = tkinter.Entry(window, font=font1, fg=bgcolor, width=30)
        traname.grid(row=3, column=2, sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=4, column=2, sticky='w')

        l = Label(window, text="Enter the Travelling Train ID:")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=5, column=2, sticky='w')
        traid = tkinter.Entry(window, font=font1, fg=bgcolor, width=30)
        traid.grid(row=6, column=2, sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=7, column=2, sticky='w')

        l = Label(window, text="Enter the Travelling Route:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=8, column=2, sticky='w')
        destination = tkinter.Entry(window, font=font1, width=30, fg=bgcolor)
        destination.grid(row=9, column=2, sticky="w")
        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=10, column=2, sticky='w')
        l = Label(window, text="Enter the Departure time:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=11, column=2, sticky='w')
        departure = tkinter.Entry(window, font=font1, width=30, fg=bgcolor)
        departure.grid(row=12, column=2, sticky="w")
        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=13, column=2, sticky='w')

        btn = Button(window, text='Confirm', bd='5', fg=bgcolor,
                     command=lambda: check())
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=14, column=2, pady=5)
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=3, sticky="e", pady=5)
        window.mainloop()

# viewer page
class Traininfornamtion(Information):
    def __int__(self, time, trainid, stationname, trainname):
        super().__int__(self, time,trainid,stationname,trainname)


    def display(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Train Information")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Train Information", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)

        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        sql = """SELECT * FROM `traininfo`
                          """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a = 0
        b = 0
        for row in record:
            a += 1

            if a < 3:
                l = Label(window, text=f"")
                l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
                l.grid(row=0 + b, column=2, sticky='w', pady=2)

                l = Label(window, text=f"Train {a}:")
                l.config(font=("Courier", 18, "bold"), height=1, width=9, bg=bgcolor, foreground=fontcolor)
                l.grid(row=1 + b, column=2, sticky='w', pady=2)

                l = Label(window, text="Train ID:")
                self.trainid = row[0]
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=2 + b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainid}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=2 + b, column=3, sticky='w', pady=2)

                l = Label(window, text="Train Name:")
                self.trainname = row[1]
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=3 + b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainname}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=3 + b, column=3, sticky='w', pady=2)

                l = Label(window, text="Travelling Route:")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=4 + b, column=2, sticky='w', pady=2)
                l = Label(window, text=f"{row[2]}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=4 + b, column=3, sticky='w', pady=2)

            b += 6
        btn = Button(window, text='Back', bd='5',fg=bgcolor,
                     command=lambda: [window.destroy(), homepage()])
        btn.config(font=("Courier", 8), height=-1, width=5, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
        btn.grid(row=0, column=4, sticky="e", pady=5)
        window.mainloop()

# admin page
class Admin_add_traininformation(Information):
    def __int__(self, time, trainid, stationname, trainname, travellingroute):
        super().__int__(self, time, trainid, stationname, trainname)
        self.travellingroute = travellingroute

    def display(self):
        window = tkinter.Tk()
        window.geometry('800x540')
        window.title("Add Train information")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Add Train information", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)

        def check():
            self.travellingroute = travel.get()
            self.trainid = traid.get()
            self.trainname = traname.get()

            if (not (self.travellingroute and self.travellingroute.strip())
                    or not (self.trainid and self.trainid.strip()) or not (
                            self.trainname and self.trainname.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a = Admin_add_traininformation()

                a.display()

            else:
                insert()
                tkinter.messagebox.showinfo("Success", "Data successfully added")
                window.destroy()
                a = Admin_add_traininformation()
                a.display()

        def insert():
            connection = mysql.connector.connect(host='localhost',
                                                 database='railway',
                                                 user='root',
                                                 password='')

            mycursor = connection.cursor()
            sql = "INSERT INTO traininfo (trainid, trainname,travellingroute) VALUES (%s, %s,%s)"
            val = (f"{self.trainid}", f"{self.trainname}", f"{self.travellingroute}")
            mycursor.execute(sql, val)
            connection.commit()
            print("Done")

        l = Label(window, text=""
                               "Enter the Travelling Train Name:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        traname = tkinter.Entry(window, font=font1, fg=bgcolor, width=30)
        traname.grid(row=3, column=2, sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=4, column=2, sticky='w')

        l = Label(window, text="Enter the Travelling Train ID:")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=5, column=2, sticky='w')
        traid = tkinter.Entry(window, font=font1, fg=bgcolor, width=30)
        traid.grid(row=6, column=2, sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=7, column=2, sticky='w')

        l = Label(window, text="Enter the Travelling Route:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=8, column=2, sticky='w')
        travel = tkinter.Entry(window, font=font1, width=30, fg=bgcolor)
        travel.grid(row=9, column=2, sticky="w")
        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=10, column=2, sticky='w')

        btn = Button(window, text='Confirm', bd='5', fg=bgcolor,
                     command=lambda: check())
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=11, column=2, pady=5)
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=3, sticky="e", pady=5)
        window.mainloop()
# viewer page
class Stationinformation(Information):
    def __int__(self, time, trainid, stationname, trainname,stationid):
        super().__int__(self, time,trainid,stationname,trainname)
        self.stationid = stationid
    def display(self):
        window = tkinter.Tk()
        window.geometry('1200x540')
        window.title("Station information")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Station information", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)

        connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        sql = """SELECT * FROM `stationinfo`
                          """
        mycursor.execute(sql)
        record = mycursor.fetchall()
        a = 0
        b = 0

        for row in record:
            a += 1

            if a < 3:
                l = Label(window, text=f" ")
                l.config(font=("Courier", 18, "bold"), bg=bgcolor, foreground=fontcolor)
                l.grid(row=1, column=0 + 4, sticky='w', pady=2)


                l = Label(window, text=f"Station {a}:")
                l.config(font=("Courier", 18, "bold"),  bg=bgcolor, foreground=fontcolor)
                l.grid(row=1 , column=2+ b, sticky='w', pady=2)

                l = Label(window, text="Station ID:")
                self.stationid = row[0]
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=2 , column=2+ b, sticky='w', pady=2)
                l = Label(window, text=f"{self.stationid}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=2 , column=3+ b, sticky='w', pady=2)

                l = Label(window, text="Station Name:")
                self.stationname = row[1]
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=3 , column=2+ b, sticky='w', pady=2)
                l = Label(window, text=f"{self.stationname}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=3 , column=3+ b, sticky='w', pady=2)

                self.trainname = row[2]
                l = Label(window, text="Travelling Train Name:")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=4, column=2+ b, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainname}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=4 , column=3+ b, sticky='w', pady=2)

                self.trainid = row[3]
                l = Label(window, text="Travelling Train ID:")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=5 , column=2+ b, sticky='w', pady=2)
                l = Label(window, text=f"{self.trainid}")
                l.config(font=font1, bg=bgcolor, foreground=fontcolor)
                l.grid(row=5, column=3+ b, sticky='w', pady=2)

            b += 3
        btn = Button(window, text='Back', bd='5',fg=bgcolor,
                     command=lambda: [window.destroy(), homepage()])
        btn.config(font=("Courier", 8), height=-1, width=5, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
        btn.grid(row=0, column=6, sticky="e", pady=5)
        window.mainloop()
# admin page
class Admin_add_stationinformation(Information):
    def __int__(self, time, trainid, stationname, trainname,stationid):
        super().__int__(self, time,trainid,stationname,trainname)
        self.stationid = stationid
    def display(self):
        window = tkinter.Tk()
        window.geometry('800x540')
        window.title("Station information")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Station information", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)
        def check():
            self.stationid = staid.get()
            self.stationname = staname.get()
            self.trainid = traid.get()
            self.trainname = traname.get()

            if (not (self.stationid and self.stationid.strip()) or not (self.stationname and self.stationname.strip())
                    or not (self.trainid and self.trainid.strip())or not (self.trainname and self.trainname.strip())):
                tkinter.messagebox.showinfo("Error", "Invalid input enter properly")
                window.destroy()

                a=Admin_add_stationinformation()

                a.display()

            else:
                insert()
                tkinter.messagebox.showinfo("Success", "Data successfully added")
                window.destroy()
                a = Admin_add_stationinformation()
                a.display()

        def insert():
            connection = mysql.connector.connect(host='localhost',
                                             database='railway',
                                             user='root',
                                             password='')

            mycursor = connection.cursor()
            sql = "INSERT INTO stationinfo (stationid, stationname, trainid, trainname) VALUES (%s, %s,%s, %s)"
            val = (f"{self.stationid}", f"{self.stationname}", f"{self.trainid}", f"{self.trainname}")
            mycursor.execute(sql, val)
            connection.commit()
            print("Done")

        l = Label(window, text="Enter the Station ID:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=2, column=2, sticky='w')
        staid = tkinter.Entry(window, font=font1, width=30, fg=bgcolor)
        staid.grid(row=3, column=2,sticky="w")

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=4, column=2, sticky='w')

        l = Label(window, text=""
                               "Enter the Station Name:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=5, column=2, sticky='w')
        staname = tkinter.Entry(window, font=font1, fg=bgcolor,width=30)
        staname.grid(row=6, column=2,sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=7, column=2, sticky='w')

        l = Label(window, text=""
                               "Enter the Travelling Train Name:"
                               "")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=8, column=2, sticky='w')
        traname = tkinter.Entry(window, font=font1, fg=bgcolor,width=30)
        traname.grid(row=9, column=2,sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=10, column=2, sticky='w')

        l = Label(window, text="Enter the Travelling Train ID:")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=11, column=2, sticky='w')
        traid = tkinter.Entry(window, font=font1, fg=bgcolor,width=30)
        traid.grid(row=12, column=2,sticky='w')

        l = Label(window, text="")
        l.config(font=font1, bg=bgcolor, foreground=fontcolor)
        l.grid(row=13, column=2, sticky='w')

        btn = Button(window, text='Confirm', bd='5', fg=bgcolor,
                     command=lambda: check())
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=14, column=2, pady=5)
        btn = Button(window, text='Back', bd='5', fg=bgcolor,
                     command=lambda: [window.destroy(), adminhomepage()])
        btn.config(font=("Courier", 8), bg=fontcolor, activebackground=bgcolor,
                   activeforeground=fontcolor)
        btn.grid(row=0, column=3, sticky="e", pady=5)
        window.mainloop()

# viewer page
def homepage():
    window = tkinter.Tk()
    window.geometry('720x540')
    window.title("Railway Homepage")
    window.config(bg=bgcolor)
    label = tkinter.Label(window, text="Welcome to Railway Management System", font=("Courier", 20))
    label.config(bg=bgcolor, foreground=fontcolor)
    label.grid(row=0, column=1, padx=20, sticky=W, pady=50)


    a=Scheduleoftrain()
    btn = Button(window, text='Schedule of train', bd='5',fg=bgcolor,
                command=lambda:[window.destroy(),a.display()])
    btn.config(font=font1, height=2, width=20, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=1, column=1, padx=50, pady=10)
    b = Stationinformation()
    btn = Button(window, text='Station Information', bd='5',fg=bgcolor,
                 command=lambda:[window.destroy(),b.display()])
    btn.config(font=font1, height=2, width=20,bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=2, column=1, padx=50, pady=10)
    c=Traininfornamtion()
    btn = Button(window, text='Train Information', bd='5',fg=bgcolor,
                 command=lambda:[window.destroy(),c.display()])
    btn.config(font=font1, height=2, width=20,bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=3, column=1, padx=50, pady=10)
    window.mainloop()
# admin page
def adminhomepage():
    window = tkinter.Tk()
    window.geometry('720x540')
    window.title("Railway Homepage")
    window.config(bg=bgcolor)
    label = tkinter.Label(window, text="Welcome to Railway Management System", font=("Courier", 20))
    label.config(bg=bgcolor, foreground=fontcolor)
    label.grid(row=0, column=1, padx=20, sticky=W, pady=50)


    a=Admin_add_scheduleoftrain()
    btn = Button(window, text='Add Schedule of train', bd='5',fg=bgcolor,
                command=lambda:[window.destroy(),a.display()])
    btn.config(font=font1,  bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=1, column=1, padx=50, pady=10)
    b = Admin_add_stationinformation()
    btn = Button(window, text='Add Station Information', bd='5',fg=bgcolor,
                 command=lambda:[window.destroy(),b.display()])
    btn.config(font=font1, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=2, column=1, padx=50, pady=10)
    c=Admin_add_traininformation()
    btn = Button(window, text='Add Train Information', bd='5',fg=bgcolor,
                 command=lambda:[window.destroy(),c.display()])
    btn.config(font=font1, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
    btn.grid(row=3, column=1, padx=50, pady=10)
    d = Admin_delete_scheduleoftrain()
    btn = Button(window, text='Delete Schedule of train', bd='5', fg=bgcolor,
                 command=lambda: [window.destroy(), d.display()])
    btn.config(font=font1, bg=fontcolor, activebackground=bgcolor, activeforeground=fontcolor)
    btn.grid(row=4, column=1, padx=50, pady=10)
    e = Admin_delete_stationinfo()
    btn = Button(window, text='Delete Station Information', bd='5', fg=bgcolor,
                 command=lambda: [window.destroy(), e.display()])
    btn.config(font=font1, bg=fontcolor, activebackground=bgcolor, activeforeground=fontcolor)
    btn.grid(row=5, column=1, padx=50, pady=10)
    f = Admin_delete_traininfo()
    btn = Button(window, text='Delete Train Information', bd='5', fg=bgcolor,
                 command=lambda: [window.destroy(), f.display()])
    btn.config(font=font1, bg=fontcolor, activebackground=bgcolor, activeforeground=fontcolor)
    btn.grid(row=6, column=1, padx=50, pady=10)
    window.mainloop()

class Privacy:
    def __int__(self, password):
        self._password = password

    def set_pass(self, password):
        self._password = password

    def get_pass(self):
        return self._password


class Login(Privacy):
    def __int__(self, password):
        super().__int__(self, password)

    def login(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Railway Login")
        window.config(bg=bgcolor)

        label = tkinter.Label(window, text="Welcome to Railway Management System", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)
        lo = Privacy()

        def logindatabase():
            username = T.get()
            lo.set_pass(password.get())
            connection = mysql.connector.connect(host='localhost',
                                                 database='railway',
                                                 user='root',
                                                 password='')
            mycursor = connection.cursor()
            sql = """SELECT * FROM `loginusers`
                     WHERE `username` = %s
                     AND `password` = %s
                  """
            username = username.strip('\n')
            passw = lo.get_pass().strip('\n')
            adr = (username, passw,)
            mycursor.execute(sql, adr)
            # fetch result
            record = mycursor.fetchall()
            a = mycursor.rowcount

            if (a > 0):
                window.destroy()
                if username.lower() == "admin":
                    adminhomepage()
                else:
                    homepage()

            else:
                window.destroy()
                err = ErrorLogin()
                err.errorlogin()
        T =  tkinter.Entry(window,font=font1, width=38,fg=bgcolor)
        T.grid(row=3, column=1, padx=50, pady=10)

        # Create label
        l = Label(window, text="Username")
        l.config(font=font1, bg=bgcolor,fg=fontcolor)
        l.grid(row=2, column=1, padx=50, pady=10)

        str = tkinter.StringVar()  # string variable
        password = tkinter.Entry(window, font=font1, fg=bgcolor,width=38, show='*', textvariable=str)
        password.grid(row=5, column=1, padx=50, pady=10)
        val = IntVar(value=0)
        la = Label(window, text="Password")
        la.config(font=font1,bg=bgcolor,fg=fontcolor)
        la.grid(row=4, column=1, padx=50, pady=10)
        # Create a Button
        btn = Button(window, text='Login', bd='5',fg=bgcolor,
                     command=logindatabase)
        btn.config(font=font1, height=1, width=7, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
        btn.grid(row=7, column=1, padx=50, pady=10)

        # show check box
        def my_show():
            if (val.get() == 1):
                password.config(show='')
            else:
                password.config(show='*')

        c1 = tkinter.Checkbutton(window, text='Show Password', variable=val,bg=bgcolor,fg=fontcolor,
                                 onvalue=1, offvalue=0, command=my_show)
        c1.grid(row=6, column=1, padx=50, pady=10)
        window.mainloop()


class ErrorLogin(Privacy):
    def errorlogin(self):
        window = tkinter.Tk()
        window.geometry('720x540')
        window.title("Railway Login")
        window.config(bg=bgcolor)
        label = tkinter.Label(window, text="Welcome to Railway Management System", font=("Courier", 20))
        label.config(bg=bgcolor, foreground=fontcolor)
        label.grid(row=0, column=1, padx=20, sticky=W, pady=50)

        def logindatabase():
            username = T.get()
            passw = password.get()
            connection = mysql.connector.connect(host='localhost',
                                                 database='railway',
                                                 user='root',
                                                 password='')
            mycursor = connection.cursor()
            sql = """SELECT * FROM `loginusers`
                         WHERE `username` = %s
                         AND `password` = %s
                      """
            username = username.strip('\n')
            passw = passw.strip('\n')
            adr = (username, passw,)
            mycursor.execute(sql, adr)
            record = mycursor.fetchall()
            a = mycursor.rowcount
            if (a > 0):
                window.destroy()
                if username.lower()=="admin":
                    adminhomepage()
                else:
                    homepage()
            else:
                window.destroy()
                err = ErrorLogin()
                err.errorlogin()

        T = tkinter.Entry(window, font=font1, width=38, fg=bgcolor)
        T.grid(row=4, column=1, padx=50, pady=10)
        # Create label
        la = Label(window, text="Invalid Detail Please try again")
        la.config(font=font1, fg="Red", bg=bgcolor,height=1, width=52)
        la.grid(row=2, column=1, padx=50, pady=10)
        l = Label(window, text="Username")
        l.config(font=font1,bg=bgcolor,fg=fontcolor)
        l.grid(row=3, column=1, padx=50, pady=10)
        str = tkinter.StringVar()  # string variable
        password = tkinter.Entry(window, font=font1, fg=bgcolor,width=38, show='*', textvariable=str)
        password.grid(row=6, column=1, padx=50, pady=10)
        val = IntVar(value=0)
        la = Label(window, text="Password")
        la.config(font=font1,bg=bgcolor,fg=fontcolor)
        la.grid(row=5, column=1, padx=50, pady=10)
        # Create a Button

        btn = Button(window, text='Login', bd='5',fg=bgcolor,
                     command=logindatabase)
        btn.config(font=font1, height=1, width=7, bg=fontcolor, activebackground=bgcolor,activeforeground=fontcolor)
        btn.grid(row=8, column=1, padx=50, pady=10)

        def my_show():
            if (val.get() == 1):
                password.config(show='')
            else:
                password.config(show='*')

        c1 = tkinter.Checkbutton(window, text='Show Password', variable=val,bg=bgcolor,fg=fontcolor,
                                 onvalue=1, offvalue=0, command=my_show)
        c1.grid(row=7, column=1, padx=50, pady=10)
        window.mainloop()


a = Login()
a.login()

from tkinter import *
import sqlite3
from tkinter import messagebox
# Author : Lorent Kosumi
#   Type: Library System Manager
#   Created in 2018
#   
#
# konektohemi ne databaze

conn = sqlite3.connect('database.db')
# kursori per te levizur ne db
c = conn.cursor()

# id
ids = []

class Window(Frame):

    def __init__(self, master=None):
                 
        self.master = master
       
        #krijimi i main frame
        self.main = Frame(master, width=800, height=720, bg='steelblue')
        
        
         # labels/text per dritaret
        self.heading = Label(master, text="Sistemi i menaxhimit te biblotekes", font=('arial 30'), fg='steelblue')
        self.heading.place(x=290, y=0)

        #   emri i librit
        self.titulli = Label(master, text="Titulli i Librit", font=('arial 10'), fg='steelblue')
        self.titulli.place(x=10, y=110)

        #   Autori i librit
        self.autori = Label(master, text="Autori i librit", font='arial 10', fg='steelblue')
        self.autori.place(x=10, y=160)
        
        #   Viti i botimit 
        self.viti = Label(master, text="Viti i botimit", font='arial 10', fg='steelblue')
        self.viti.place(x=10, y=210)
        
        #   vendndodhja
        self.vendi = Label(master, text="Ku gjendet libri", font='arial 10', fg='steelblue')
        self.vendi.place(x=10, y=260)
        
        #   permbajtja
        self.tirazhi = Label(master, text="Tirazhi", font='arial 10', fg='steelblue')
        self.tirazhi.place(x=10, y=315)
        
        #   hyrjet-----------------------
        
        # hyrja per emrin e librit
        self.titulli_ent = Entry(width=30)
        self.titulli_ent.place(x=10, y=135)
        
        #   hyrja per autorin e librit
        self.autori_ent = Entry(width=30)
        self.autori_ent.place(x=10, y=185)
        
        #   hyrja per vitin e botimit 
        self.viti_ent = Entry(width=30)
        self.viti_ent.place(x=10, y=235)
        
        #   hyrja per vendin e ndodhjes se librit
        self.vendi_ent = Entry(width=30)
        self.vendi_ent.place(x=10, y=285)
        
        #   hyrja per permbajtjen
       # self.permbajtja_ent = Entry(width=30)
        #self.permbajtja_ent.place(x=10, y=335)
        
        #self.permbajtja_ent = Checkbutton(master, text="Shkenca Natyrore")
        #self.permbajtja_ent.place(x=5, y=345)
        
        #self.permbajtja_ent = Checkbutton(master, text="Shkenca Shoqerore")
        #self.permbajtja_ent.place(x=5, y=365)
        
        #self.permbajtja_ent = Checkbutton(master, text="Tjera...")
        #self.permbajtja_ent.place(x=5, y=385)
        
        self.tirazhi_ent = Spinbox(master, from_=1, to=100)
        self.tirazhi_ent.place(x=10, y=335)
       
      
        # butoni per performimin e komandave
        self.submit = Button(master, text="Shto", width=10, height=1, bg='steelblue', fg='white', command=self.add_librat)
        self.submit.place(x=10, y=415)
        
       
        # i shfaq nx ne anen e djatht te dritares
       # self.logs = Label(master, text="Librat", font=('arial 28 bold'), fg='steelblue')
        #self.logs.place(x=1000, y=0)

        #self.box = Text(master, width=50, height=40)
        #self.box.place(x=870, y=60)
       
    
        #   merret nr i id prej table 'librat'
        sql3 = "SELECT titulli AND autori FROM librat"
        self.result = c.execute(sql3)
        for self.row in self.result:
            self.titulli = self.row[0]
            ids.append(self.titulli)

        # i merr id
       # self.new = sorted("ids")
        #self.final_titulli = self.new[len(ids)]
       

       # self.box = Text(master, width=50, height=40)
        #self.box.place(x=720, y=60)
        #self.box.insert(END, "Librat:  " + str(self.final_titulli))
        
        #   fun per veprim kur klikohet butoni submit
    def add_librat(self):
        # inputs t'userit

        self.val1 = self.titulli_ent.get()
        self.val2 = self.autori_ent.get()
        self.val3 = self.viti_ent.get()
        self.val4 = self.vendi_ent.get()
        self.val5 = self.tirazhi_ent.get()
            
        #   nese fushat lihen null shfaqet message
        if self.val1 == "" or self.val2 == "" or self.val3 == "" or self.val4 == "" or self.val5 == "":
            messagebox.showinfo("Verejtje!", "Ju lutemi mbushini te gjitha fushat")
        #   tash nese krejt eshte n'rregull at'her i shtojme t'dhanat n'db
        else:
            sql = ("INSERT INTO 'librat' (titulli, autori, viti, vendi, tirazhi) VALUES(?, ?, ?, ?, ?)")
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5))
            conn.commit()
            messagebox.showinfo("Perfundoi", "Libri " + str(self.val1) + " u shtua ne bazen e te dhenave")
                 
        

root = Tk()

root.title("Sistemi i menaxhimit te biblotekes")
root.resizable(1, 1)
root.geometry("1200x700")
app = Window(root)

root.mainloop()

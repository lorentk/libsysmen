from tkinter import *
import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()


class records():
     #class created to see records that have been previously inputted#
    def __init__(self,master):
        self.master=master
        self.master.geometry('1200x700')
        self.master.title('Records')
        self.connection = sqlite3.connect('database.db')
        self.cur = self.connection.cursor()
       
        self.dateLabel = Label(self.master, text="ID", width=10)
        self.dateLabel.grid(row=0, column=1)
        
        self.BMILabel = Label(self.master, text="Titulli", width=15)
        self.BMILabel.grid(row=0, column=2)
        
        self.stateLabel = Label(self.master, text="Autori", width=15)
        self.stateLabel.grid(row=0, column=3)
        
        self.stateLabel = Label(self.master, text="Viti i botimit", width=15)
        self.stateLabel.grid(row=0, column=4)
        
        self.stateLabel = Label(self.master, text="Vendndodhja", width=15)
        self.stateLabel.grid(row=0, column=5)
        
        self.stateLabel = Label(self.master, text="Tirazhi", width=15)
        self.stateLabel.grid(row=0, column=6)
        
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=index+1, column=1)
            Label(self.master, text=dat[1]).grid(row=index+1, column=2)
            Label(self.master, text=dat[2]).grid(row=index+1, column=3)
            Label(self.master, text=dat[3]).grid(row=index+1, column=4)
            Label(self.master, text=dat[4]).grid(row=index+1, column=5)
            Label(self.master, text=dat[5]).grid(row=index+1, column=6)
    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM librat")
        return self.cur.fetchall()
    
    

root = Tk()
root.title("Te gjithe librat")
root.resizable(1, 1)
root.geometry("1200x700")
app = records(root)
root.mainloop()






   
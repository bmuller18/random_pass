import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime


#Actual date time and format time
date = datetime.datetime.now()
format_date = date.strftime("%H:%M:%S")
show_date = str(format_date)

#######################################DELETE#######################################
print("La fecha y hora actual es:", format_date)


root = tk.Tk()

root.title("Random Password")
root.geometry("500x500")
root.config(bg="white")



root.mainloop()


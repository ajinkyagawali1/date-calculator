from tkinter import *
import tkinter.messagebox
from datetime import datetime, timedelta


#function to calculate difference between two dates
def calc1():
	d1 = datetime.strptime(date1.get(), "%d/%m/%Y")
	d2 = datetime.strptime(date2.get(), "%d/%m/%Y")

	# difference between dates in timedelta
	delta = d2 - d1
	ans = delta.days
	print(f'The difference is {delta.days} days')
	tkinter.messagebox.showinfo('Answer', f"The difference is {ans} days")

def add():
	d3 = datetime.strptime(date.get(), "%d/%m/%Y")
	days = year.get()*365+month.get()*31+day.get()
	sum = d3 + timedelta(days=days)

	print(f'The required date is: {sum}')
	tkinter.messagebox.showinfo('Answer', f"The required date is: {sum}")

def sub():
	d3 = datetime.strptime(date.get(), "%d/%m/%Y")
	days = year.get()*365+month.get()*31+day.get()
	diff = d3 - timedelta(days=days)

	print(f"The required date is: {diff}")
	tkinter.messagebox.showinfo('Answer', f"The required date is: {diff}")




#create window
win = Tk()
win.geometry("325x485+475+100")
win.configure(bg='cyan')
win.title("Date Calculator")
win.resizable(height = None, width = None)


frame1 = Frame(win, bg='cyan')
frame1.pack(side=TOP,padx=20,pady=20)

#Difference in dates program

#header1
Label(frame1, text="Difference in dates", font='Comicsansms 13 bold', pady=15, bg='cyan').grid(row=1,column=2,columnspan=4)


label1 = Label(frame1, text="Enter first date: ", pady=5, padx=5, bg='cyan')
label2 = Label(frame1, text="Enter second date: ", pady=5, padx=5, bg='cyan')

date1 = StringVar()
date2 = StringVar()

label1.grid(row=2, column=2)
label2.grid(row=3, column=2)

date1entr = Entry(frame1, textvariable=date1, bg='khaki')
date2entr = Entry(frame1, textvariable=date2, bg='khaki')

date1entr.grid(row=2, column= 3)
date2entr.grid(row=3, column= 3)

submit1 = Button(frame1, text="Calculate", command=calc1, bg='DeepSkyBlue2')
submit1.grid(row=4, column=1, columnspan=3)

label3 = Label(frame1, text = "The dates in both programs should be in format", bg='turquoise').grid(row=5, column=0, columnspan=4)
label4 = Label(frame1, text = " dd/mm/yyyy", bg='turquoise').grid(row=6, column=0, columnspan=4)


frame2 = Frame(win, bg='cyan')
frame2.pack(padx=20,pady=20)


#Difference in dates programs

#header2
Label(frame2, text="Operations on Dates", font='Comicsansms 13 bold', pady=15, bg='cyan').grid(row=1,column=1,columnspan=3)

l1 = Label(frame2, text="Enter a Date: ", bg='cyan').grid(row=3,column=1)
l2 = Label(frame2, text="Enter no. of years to add or subtract: ", bg='cyan').grid(row=4,column=1)
l3 = Label(frame2, text="Enter no. of months to add or subtract: ", bg='cyan').grid(row=5,column=1)
l4 = Label(frame2, text="Enter no. of days to add or subtract: ", bg='cyan').grid(row=6,column=1)


date = StringVar()
year = IntVar()
month = IntVar()
day = IntVar()

dateentry = Entry(frame2, textvariable=date, bg='khaki').grid(row=3,column=2,columnspan=4)
yearentry = Entry(frame2, textvariable=year, bg='khaki').grid(row=4,column=2,columnspan=4)
monthentry = Entry(frame2, textvariable=month, bg='khaki').grid(row=5,column=2,columnspan=4)
dayentry = Entry(frame2, textvariable=day, bg='khaki').grid(row=6,column=2,columnspan=4)


submit2 = Button(frame2, text="Add", command=add, bg='DeepSkyBlue2').grid(row=7,column=0, columnspan=2)
submit2 = Button(frame2, text="Subtract", command=sub, bg='DeepSkyBlue2').grid(row=7,column=2, columnspan=2)

frame3 = Frame(win, bg='turquoise')
frame3.pack(padx=20,pady=20)


l5 = Label(frame2, text="Above it is assumed that 1 year consists ", bg='turquoise').grid(row=8,column=0,columnspan=4)
l6 = Label(frame2, text="of 365 days and 1 month consists of 31 days.", bg='turquoise').grid(row=9,column=0,columnspan=4)
l7 = Label(frame2, text="-Ajinkya Gawali",bg='steel blue').grid(row=10,column=0,columnspan=4)

win.mainloop()



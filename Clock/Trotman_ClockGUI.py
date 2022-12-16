#Keontae Trotman
#This program creates a GUI that emulates a clock using a custom datetime module.
import tkinter as tk
import Trotman_DateTime
#Function that increases the day once the button is pushed.
def incDay_button():
    #Calls the dt function
    datetime.increaseDay()
    #New date overlaps the previous date.
    dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
    dtime.place(relx=.35, rely= .14)
#Function that decreases the day once the button is pushed
def decDay_button():
    #Calls the dt function
    datetime.decreaseDay()
    #New date overlaps the previous date.
    dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
    dtime.place(relx=.35, rely= .14)
#Function that increases the second once the button is pushed
def incSec_button():
    #calls the dt function
    datetime.increaseSecond()
    #New date overlaps the previous date.
    dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
    dtime.place(relx=.35, rely= .14)
#Function that decreases the second once the button is pushed
def decSec_button():
    #Calls the dt function
    datetime.decreaseSecond()
    #New date overlaps the previous date.
    dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
    dtime.place(relx=.35, rely= .14)
#Function that sets the time and date
def setClock_button():
    #Calls the dt function. Uses list box selections for the parameters.
    if datetime.setClock(hourbox.curselection()[0],minutebox.curselection()[0],secondbox.curselection()[0],monthbox.curselection()[0]+1,daybox.curselection()[0]+1,yearbox.curselection()[0]+1980):
        #New date overlaps the previous date.
        dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
        dtime.place(relx=.35, rely= .14)
    else:
        #Error message overlaps the previous date.
        dtime=tk.Label(screen,bg="lime", text='Invalid Date/Time',width=18)
        dtime.place(relx=.35, rely= .14)
#Screen variable represents the Tk class in the tk module.
screen=tk.Tk()
#datetime variable represents the Clock class in the datetime module
datetime=Trotman_DateTime.Clock()
#Window title
screen.title("Keontae's clock")
#Window dimensions
screen.geometry("550x700")
#Sets background color
tk.Canvas.configure(screen,bg='purple')
#Months
months=['January','February','March','April','May','June','July','August','September','October','November','December']
#Number of days in a month
days=list(range(1,32))
#Range of years
years=list(range(1980,2101))
#up to 23 hours
hours=list(range(0,24))
#up to 60 mins and secs
minsec=list(range(0,60))
#Current time label at the very top
ct=tk.Label(screen,bg="lime", text="Current Time")
ct.place(relx=.4, rely= .1)
#Date time printed below the ct label
dtime=tk.Label(screen,bg="lime", text=datetime.__str__())
dtime.place(relx=.35, rely= .14)
#Month label
mon=tk.Label(screen,bg="lime", text='Month')
mon.place(relx=.01, rely= .25)
#Day label
dy=tk.Label(screen,bg="lime", text='day')
dy.place(relx=.25, rely= .25)
#Year label
yr=tk.Label(screen,bg="lime", text='Year')
yr.place(relx=.35, rely= .25)
#Hour(s) label
hr=tk.Label(screen,bg="lime", text='Hour')
hr.place(relx=.5, rely= .25)
#Mintue(s) label
min=tk.Label(screen,bg="lime", text='Minute')
min.place(relx=.6, rely= .25)
#Second(s) label
sec=tk.Label(screen,bg="lime", text='Second')
sec.place(relx=.72, rely= .25)
#Monthbox + scrollbar
month_sb = tk.Scrollbar(screen,orient="vertical")
monthbox=tk.Listbox(screen,width=14,exportselection=0,selectmode="single",yscrollcommand = month_sb.set)
#Daybox + scrollbar
day_sb=tk.Scrollbar(screen,orient="vertical")
daybox=tk.Listbox(screen,width=3,exportselection=0,selectmode="single",yscrollcommand = day_sb.set)
#Yearbox + scrollbar
year_sb=tk.Scrollbar(screen,orient="vertical")
yearbox=tk.Listbox(screen,width=7,exportselection=0,selectmode="single",yscrollcommand = day_sb.set)
#Hourbox + scrollbar
hour_sb=tk.Scrollbar(screen,orient="vertical")
hourbox=tk.Listbox(screen,width=3,exportselection=0,selectmode="single",yscrollcommand = day_sb.set)
#Minutebox + scrollbar
minute_sb=tk.Scrollbar(screen,orient="vertical")
minutebox=tk.Listbox(screen,width=3,exportselection=0,selectmode="single",yscrollcommand = day_sb.set)
#Secondbox + scrollbar
second_sb=tk.Scrollbar(screen,orient="vertical")
secondbox=tk.Listbox(screen,width=3,exportselection=0,selectmode="single",yscrollcommand = day_sb.set)
#Month listbox                   
for x in range(len(months)):
    monthbox.insert("end",months[x])
monthbox.select_set(0)
month_sb.config(command=monthbox.yview)
monthbox.place(relx=.01, rely=.3)
month_sb.place(relx=.165, rely=.33)
#Day listbox
for x in range(len(days)):
    daybox.insert("end",days[x])
daybox.select_set(0)
day_sb.config(command=daybox.yview)
daybox.place(relx=.25, rely=.3)
day_sb.place(relx=.29, rely=.33)
#Year listbox
for x in range(len(years)):
    yearbox.insert("end",years[x])
yearbox.select_set(0)
year_sb.config(command=yearbox.yview)
yearbox.place(relx=.35, rely=.3)
year_sb.place(relx=.43, rely=.33)
#Hour listbox
for x in range(len(hours)):
    hourbox.insert("end",hours[x])
hourbox.select_set(0)
hour_sb.config(command=hourbox.yview)
hourbox.place(relx=.5, rely=.3)
hour_sb.place(relx=.535, rely=.33)
#Min listbox
for x in range(len(minsec)):
    minutebox.insert("end",minsec[x])
minutebox.select_set(0)
minute_sb.config(command=minutebox.yview)
minutebox.place(relx=.6, rely=.3)
minute_sb.place(relx=.635, rely=.33)
#Sec Listbox
for x in range(len(minsec)):
    secondbox.insert("end",minsec[x])
secondbox.select_set(0)
second_sb.config(command=secondbox.yview)
secondbox.place(relx=.72, rely=.3)
second_sb.place(relx=.755, rely=.33)
#Quit button terminates the program
quitButton=tk.Button(screen,text="Quit",command=screen.destroy)
quitButton.place(relx=.45, rely=.7)
#Settime button sets the clock.
setButton=tk.Button(screen,text="Set Time",command=setClock_button)
setButton.place(relx=.0, rely=.6)
#IncDay button increases the day
incDay=tk.Button(screen,text="Increase Day",command=incDay_button)
incDay.place(relx=.15, rely=.6)
#DecDay button  increases the day
decDay=tk.Button(screen,text="Decrease Day",command=decDay_button)
decDay.place(relx=.35, rely=.6)
#IncSec button increases the second
incSec=tk.Button(screen,text="Increase Second",command=incSec_button)
incSec.place(relx=.55, rely=.6)
#DecSec button decreases the second
decSec=tk.Button(screen,text="Decrease Second",command=decSec_button)
decSec.place(relx=.77, rely=.6)
#Calls the tk function and starts the main program.
screen.mainloop()

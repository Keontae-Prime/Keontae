import tkinter as tk

def button_press():
    item=sportsbox.curselection()
    print(item)
    label3["text"]="Item Selected "+str(item[0])

sports=["Hockey","Tennis","Football","Baseball","Skiing","Swimming",
        "Rowing","Archery","Volley Ball","Track","Cross Country",
        "Field Hockey"]

screen=tk.Tk()
screen.title("My GUI")
screen.geometry("500x500")
label1=tk.Label(screen,bg="blue", text="First Label")
label1.place(relx=.1, rely= .1)
label2=tk.Label(screen,bg="red")
label2["text"]= "Second Label"
label2.place(relx=.3, rely= .1)
label3=tk.Label(screen,bg="green", text="This is the Third Label")
label3.place(relx=.5, rely= .1)
label4=tk.Label(screen,bg="orange")
label4["text"]= "Fourth Label"
label4.place(relx=.8, rely= .1)
button1=tk.Button(screen, text="Press Me",command=button_press)
button1.place(relx=.45, rely=.8)
quitbutton=tk.Button(screen,text="Quit",command=screen.destroy)
quitbutton.place(relx=.58, rely=.8)

scroll_bar = tk.Scrollbar(screen,orient="vertical")
sportsbox=tk.Listbox(screen,width=14,exportselection=0,selectmode="single",
                     yscrollcommand = scroll_bar.set)
for x in range(len(sports)):
    sportsbox.insert("end",sports[x])
sportsbox.select_set(0)


scroll_bar.config(command=sportsbox.yview)

sportsbox.place(relx=.45, rely=.3)
scroll_bar.place(relx=.62, rely=.42)

screen.mainloop()
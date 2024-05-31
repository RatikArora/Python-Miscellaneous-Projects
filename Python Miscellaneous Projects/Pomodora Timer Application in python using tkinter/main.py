import tkinter
import math
import os

os.system('cls')
print("\nThis is a pomodora application its main logic is to provide you with work and rest timers so \nThere are 4 work cycles \n3 short break cycles and \n1 long break cycle \nIts motive is to bring out the bst productivity from you\n")

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

canvas_text=None
ticker =None
timer = None
ticks = ""
reps = 0

# basic functions
def addtick():
    global ticks,ticker
    tick = "✔"
    ticks = ticks+tick
    # print(ticks)
    ticker.config(text=ticks)

def starttimer():    
    global reps
    reps += 1
    # print(reps)
    if reps % 8 == 0 :
        lable.config(text = "LONG REST",fg=GREEN,bg=YELLOW)
        countdown(20*60)
        addtick()
        
    elif reps%2==1:
        lable.config(text = "WORK",fg=RED,bg=YELLOW)
        countdown(25*60)     

    else:
        lable.config(text = "REST",fg=PINK,bg=YELLOW)
        countdown(5*60)
        addtick()
        
def resettimer():
    global reps,ticker
    reps = 0

    window.after_cancel(timer)
    lable.config(text = "TIMER",fg=GREEN,bg=YELLOW)
    canvas.itemconfig(canvas_text,text="00:00")
    ticker.config(text="")
    
    
    
    
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(canvas_text,text=f"{minutes}:{seconds}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        starttimer()
    

# making a window in the tkinter 
window = tkinter.Tk()  
window.title("POMODORA CLOCK ~ Ratik Arora")
window.config(padx=100,pady=50,bg=YELLOW) 

# adding the main image and setting the background color in the canvas and in tkinter
canvas = tkinter.Canvas(width=400,height=300,bg=YELLOW,highlightthickness=0)
tomimg = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200,150,image=tomimg)

# text over the image
canvas_text = canvas.create_text(200,165,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

# lables
lable = tkinter.Label(text="TIMER",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW)
# button
startbutton = tkinter.Button(text="Start",command=starttimer)
resetbutton = tkinter.Button(text="reset",command=resettimer)
ticker = tkinter.Label(text=ticks,fg=PINK,font=(10),bg=YELLOW)

# grids management 
startbutton.grid(column=1,row=3)
canvas.grid(column=2,row=2)
lable.grid(column=2,row=1)
resetbutton.grid(column=3,row=3)
ticker.grid(column=2,row=4)


window.mainloop()
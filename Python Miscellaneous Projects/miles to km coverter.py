import tkinter

window = tkinter.Tk()
window.title("Mile to kilometer converter")
window.minsize(width = 250 ,height = 125)
window.config(padx=25,pady=25)

# button is pressed function
def pressed():
    # print("button is pressed")
    noofmiles = float(mile.get())
    # print(noofmiles)
    noofkms = noofmiles*1.6093
    noofkms = ("%.4f" % noofkms)
    lable3.config(text=noofkms)


# lables
mile = tkinter.Entry(text=0,width=10)
lable1 = tkinter.Label(text="Miles",font=('arial',12))
lable2 = tkinter.Label(text="is equals to",font=('arial',12))
noofkms = 0.0
lable3 = tkinter.Label(text=noofkms,font=('arial',12))
lable4 = tkinter.Label(text="Km",font=('arial',12))
button = tkinter.Button(text="Calculate",command=pressed)


# grids
button.grid(column=2,row=3)
mile.grid(column=2,row=1)
lable1.grid(column=3,row=1)
lable2.grid(column=1,row=2)
lable3.grid(padx=4,pady=4)
lable3.grid(column=2,row=2)
lable4.grid(column=3,row=2)


window.mainloop()
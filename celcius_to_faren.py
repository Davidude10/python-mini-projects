import tkinter as tk
clr1='#daf4b9'
def convert():
    c = float(entry.get())
    f = (c * 9/5) + 32
    result.config(text=f"{f:.2f} °F")

a = tk.Tk()
a.configure(background="light yellow")
a.title("celcius to farenhiet Converter")
labelhead=tk.Label(a,text="CELCIUS TO FARENHIET",font=("poppins",16),foreground="Red")
labelhead.place(x=70,y=30)
label = tk.Label(a, text="Enter celcius value:",background=clr1)
label.place(x=30,y=100)

entry = tk.Entry(a,background="yellow",foreground="blue")
entry.place(x=200,y=100)

convert_button = tk.Button(a, text="Convert", command=convert,background="light blue",foreground="red")
convert_button.place(x=150,y=200)

result = tk.Label(a, text="",background="light yellow",font=("poppins",14),foreground="Red")
result.place(x=150,y=300)
a.geometry("400x400")

a.mainloop()

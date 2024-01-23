import tkinter as tk

rate = {"RUP": 1.0,"USD": 0.012,"EUR": 0.011,"JPY": 1.81}


a = tk.Tk()
a.title("Currency Converter")

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = optionfrom.get()
        to_currency = optionto.get()
        
        result = amount * rate[to_currency] / rate[from_currency]
        label_result.config(text=f"Converted: {result:.3f} {to_currency}")
    except ValueError:
        label_result.config(text="Invalid input. Enter a valid number.")

label_amount = tk.Label(a, text="Amount to Convert:",background="light blue")
label_amount.place(x=20,y=20)
entry_amount = tk.Entry(a)
entry_amount.place(x=200,y=20)

labelfrom = tk.Label(a, text="From Currency:",background="light blue")
labelfrom.place(x=20,y=85)
optionfrom = tk.StringVar()
optionfrom.set("RUP")  
optionfrombox = tk.OptionMenu(a, optionfrom, *rate.keys())
optionfrombox.place(x=200,y=80)

labelto = tk.Label(a, text="To Currency:",background="lightblue")
labelto.place(x=20,y=165)
optionto = tk.StringVar()
optionto.set("USD") 
optiontobox = tk.OptionMenu(a, optionto, *rate.keys())
optiontobox.place(x=200,y=160)


convert_button = tk.Button(a, text="Convert", command=convert,background="white",foreground="Black")
convert_button.place(x=170,y=240)


label_result = tk.Label(a, text="",background="light green",foreground="Red")
label_result.place(x=140,y=300)
a.geometry("400x400")
a.configure(background="light green")
a.mainloop()

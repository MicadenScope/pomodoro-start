import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

# Miles
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to"
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Ergebnis
result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

# Km
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# Funktion
def miles_to_km():
    miles = float(user_input.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=km)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()



import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    Kilometer_result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

Kilometer_result_label = tkinter.Label(text="0")
Kilometer_result_label.grid(column=1, row=1)

Kilometer_label = tkinter.Label(text="Km")
Kilometer_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=2)

window.mainloop()
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Trivia App")
# window.geometry('350x200')

selected = StringVar()
rad1 = Radiobutton(window, text='True', value="True", variable=selected)
rad2 = Radiobutton(window, text='False', value="False", variable=selected)


# Functions
def clicked():
    print(selected.get())


ques_txt = Label(window, wraplength=300, text="Question Question Question Question Question Question Question")
ques_txt.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

# Submit Button
btn = Button(window, text="Submit", command=clicked)
btn.grid(column=0, row=2)

# Quit Button
quit_btn = Button(window, text="Quit", command=window.destroy)
quit_btn.grid(column=1, row=2)

# Radio Buttons
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)

# Launch Window
window.mainloop()
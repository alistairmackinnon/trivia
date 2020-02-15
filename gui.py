from tkinter import *
from tkinter.ttk import *
import trivia

window = Tk()
window.title("Trivia App")

frame = Frame(window)
frame.pack()


# Functions
def validate_answer():
    global submit_txt
    user_answer = selected.get()
    if user_answer == answer:
        print('Correct')
    else:
        print('Incorrect')


# Set question context
question_tup = trivia.get_questions(1)
question = question_tup[0]
answer = question_tup[1]

# Set Gui
ques_txt = Label(frame, wraplength=300, text=question)
ques_txt.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

# Radio Buttons
selected = StringVar()
rad1 = Radiobutton(frame, text='True', value="True", variable=selected)
rad2 = Radiobutton(frame, text='False', value="False", variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)

# Submit Button
submit_txt = StringVar()
submit_txt = 'Submit'
btn = Button(frame, text=submit_txt, command=validate_answer)
btn.grid(column=0, row=2)

# Quit Button
quit_btn = Button(frame, text="Quit", command=window.destroy)
quit_btn.grid(column=1, row=2)


# Launch Window
window.mainloop()

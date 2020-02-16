from tkinter import *
import trivia


class Window(Frame):
    def __init__(self, master=None):
        self.answer = StringVar()
        self.user_answer = StringVar()
        self.selected = StringVar()

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def validate_answer(self):
        user_answer = self.selected.get()
        if user_answer == self.answer:
            print('Correct')
        else:
            print('Incorrect')

    def client_exit(self):
        exit()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # Set question context
        question_tup = trivia.get_questions(1)
        question = question_tup[0]
        self.answer = question_tup[1]

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quit_button = Button(self, text="Quit", command=self.client_exit)

        # placing the button on my window
        quit_button.grid(column=1, row=2)

        ques_txt = Label(self, wraplength=300, text=question)
        ques_txt.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

        # Radio Buttons
        rad1 = Radiobutton(self, text='True', value="True", variable=self.selected)
        rad2 = Radiobutton(self, text='False', value="False", variable=self.selected)
        rad1.grid(column=0, row=1)
        rad2.grid(column=1, row=1)

        # Submit Button
        submit_txt = 'Submit'
        btn = Button(self, text=submit_txt, command=self.validate_answer)
        btn.grid(column=0, row=2)


root = Tk()

# size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()

from tkinter import *

THEME_COLOR = "#375362"

class Quiz_UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0, borderwidth=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150,125,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,"italic"))



        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img,highlightthickness=0,borderwidth=0)
        self.true_btn.grid(row=2,column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img,highlightthickness=0,borderwidth=0)
        self.false_btn.grid(row=2,column=1)



        self.window.mainloop()
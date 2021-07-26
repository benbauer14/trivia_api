THEME_COLOR = "#375362"
from tkinter import Canvas, Label, PhotoImage, Tk

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title(("Trivia!"))
        self.window.config(bg=THEME_COLOR, width=360, height=500)
        self.window.config(padx=20, pady=20)

        self.label = Label()
        self.label.config(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.true_img = Canvas(width=100, height=100)
        img = PhotoImage("images/true.png")
        self.true_img.create_image(0,0, image=img)
        self.true_img.grid(row=2,column=0)

        self.false_img = Canvas(width=100, height=100)
        img = PhotoImage("images/false.png")
        self.true_img.create_image(0,0, image=img)
        self.true_img.grid(row=2,column=1)


        self.window.mainloop()
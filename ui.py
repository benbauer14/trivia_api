THEME_COLOR = "#375362"
from tkinter import Canvas, Label, PhotoImage, Tk, Button
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(("Trivia!"))
        self.window.config(bg=THEME_COLOR, width=360, height=500)
        self.window.config(padx=20, pady=20)

        self.label = Label()
        self.label.config(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125, text="Some Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=275)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file="images/true.png")
        self.true_img = Button(image=img_true, highlightthickness=0)
        self.true_img.grid(row=2,column=0)


        img_false = PhotoImage(file="images/false.png")
        self.false_img = Button(image=img_false, highlightthickness=0)
        self.false_img.grid(row=2,column=1)

        self.getNextQuestion()
        self.window.mainloop()

    def getNextQuestion(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#350b40"

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Home")
        self.quiz_btn = Button(self.master, text="Open Quiz", command=self.open_quiz_window)
        self.quiz_btn.grid(row=0, column=0)

    def open_quiz_window(self):
        quiz_window = Toplevel(self.master)
        app = QuizUI(quiz_window)

class QuizUI:
    def __init__(self, master):
        self.quiz_brain = quiz

        self.master = master
        self.master.title("QUIZ APP")
        self.master.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(self.master, text="Score: 0", bg=THEME_COLOR, fg='#ffffff', font=("Arial", 14))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.master, width=300, height=250, bg='#ffffff')
        self.question_text = self.canvas.create_text(150, 125, text="Question text", fill=THEME_COLOR,
                                                     width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_btn_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(self.master, image=self.right_btn_img, highlightthickness=0, command=self.right_answer, bd=0)
        self.right_btn.grid(row=2, column=0)

        self.wrong_btn_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(self.master, image=self.wrong_btn_img, highlightthickness=0, command=self.wrong_answer, bd=0)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()


    def get_next_question(self):
        """Retrieve the next question from the quiz brain class and modify canvas text"""
        self.canvas.configure(bg='white')
        if self.quiz_brain.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz_brain.score}")
            qst_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=qst_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz")
            self.right_btn.configure(state='disabled')
            self.wrong_btn.configure(state='disabled')

    def right_answer(self):
        answer = self.quiz_brain.check_answer("True")
        self.give_feedback(answer)

    def wrong_answer(self):
        answer = self.quiz_brain.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.master.after(1000, self.get_next_question)


root = Tk()
app = HomePage(root)
root.mainloop()
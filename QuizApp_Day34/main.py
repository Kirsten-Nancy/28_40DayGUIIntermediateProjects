from tkinter import *
import data

THEME_COLOR = "#350b40"

class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Home")
        self.master.configure(padx=100, pady=100)
        self.choice_label = Label(text="Choose a label")
        self.choice_label.grid(row=0, column=0)
        self.selected = None

        self.OPTIONS = data.list_names
        self.selected_category = StringVar(self.master)
        self.selected_category.set(self.OPTIONS[0])

        self.drop_down = OptionMenu(self.master, self.selected_category, *self.OPTIONS)
        self.drop_down.grid(row=1, column=0)

        self.quiz_btn = Button(self.master, text="Open Quiz", command=self.open_quiz_window)
        self.quiz_btn.grid(row=2, column=0)

    def show(self):
        self.selected = self.selected_category.get()
        my_label = Label(self.master, text=self.selected).grid(row=3, column=0)
        data.get_category(self.selected)

    def open_quiz_window(self):
        self.show()
        quiz_window = Toplevel(self.master)
        app = QuizUI(quiz_window)



class QuizUI:
    def __init__(self, master):
        self.quiz_brain = data.quiz

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
        self.right_btn = Button(self.master, image=self.right_btn_img, highlightthickness=0,
                                command=self.right_answer, bd=0)
        self.right_btn.grid(row=2, column=0)

        self.wrong_btn_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(self.master, image=self.wrong_btn_img, highlightthickness=0,
                                command=self.wrong_answer, bd=0)
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
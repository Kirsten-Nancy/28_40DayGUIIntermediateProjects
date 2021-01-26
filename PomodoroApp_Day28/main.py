from tkinter import *
from PIL import ImageTk, Image
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
done_mark = ''
window_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_btn.configure(state='normal')
    reset_btn.configure(state='disabled')
    global reps, done_mark
    window.after_cancel(window_timer)
    reps = 1
    done_mark = ''
    session_title.configure(text='Session')
    canvas.itemconfig(timer_text, text='00:00')
    checkmark.configure(text=done_mark)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_btn.configure(state='disabled')
    reset_btn.configure(state='normal')
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps

    if reps == 8:
        session_title.configure(text='Long break')
        countdown(long_break)
    elif reps % 2 == 0:
        session_title.configure(text='Short break')
        countdown(short_break)
    elif reps < 8:
        session_title.configure(text='WORK')
        countdown(work_time)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def raise_window(win):
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)

def countdown(count):
    # Convert seconds to min(division), seconds-modulo,the remainder
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d} : {seconds:02d}")
    if count < 1:
        pygame.init()
        pygame.mixer.music.load("pomo_sound.mp3")
        pygame.mixer.music.play(0)
        raise_window(window)
    if count > 0:
        # Prevent it from going to negatives
        global window_timer
        window_timer = window.after(1000, countdown, count-1)
    else:
        global done_mark
        # Add a mark after every work session, since the reps are incremented
        # before this, add a check after thus work rep+1
        if reps in (2, 4, 6, 8):
            done_mark += '✔'
            checkmark.configure(text=done_mark)
            # When it reaches zero, a different session starts
        print(reps)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.configure(bg='#221F32', padx=58, pady=-50)
window.geometry('500x500')
window.resizable(0, 0)
# Resize the image
# image = Image.open("tomato.png")
# image.thumbnail((300, 300))
# image.save("tomato_bg.png")

session_title = Label(text='Session', pady=20, fg='white', bg='#221F32', font=('Helvetica', 18, 'bold'))
session_title.grid(column=1, row=0)

canvas = Canvas(width=250, height=300, bg='white', highlightthickness=0)
bg_img = ImageTk.PhotoImage(Image.open('tomato_bg.png'))
canvas.create_image(150, 150, image=bg_img)

timer_text = canvas.create_text(150, 170, text='00:00', fill='white', font=('Helvetica', 24, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', command=start_timer, padx=15)
start_btn.grid(column=0, row=3)

reset_btn = Button(text='Reset', padx=15, command=reset_timer)
reset_btn.grid(column=2, row=3)

checkmark = Label(bg='#221F32', fg='green', font=('Helvetica', 16), pady=15)
checkmark.grid(column=1, row=4)

window.mainloop()


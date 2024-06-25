from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def restart_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Title")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


window.after(1000)

label1 = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "bold"), fg=GREEN, highlightthickness=0)
label1.grid(column=1, row=0)

label2 = Label( fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

button1 = Button(text="Start", bg=YELLOW, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", bg=YELLOW, command=restart_timer)
button2.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
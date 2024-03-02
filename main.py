
from tkinter import *
import random
import time

# Sets the timer to x minutes.
minutes = 1
timer = minutes * 60
currentTime = 0
formatted_time = timer

numbers = []
score = 0

root = Tk()

root.title("Mental Maths")
root.geometry("500x500")

main = Frame(root)
main.pack()
main.place(relx=.5, rely=.5, anchor=CENTER)

timer_lbl = Label(root, text="Time left: " + str(formatted_time), font=("Arial", 10))
timer_lbl.pack()

score_lbl = Label(root, text="Score: " + str(score), font=("Arial", 10))
score_lbl.pack(side = TOP)

expression_lbl = Label(main, font=("Arial", 15))
expression_lbl.grid(column=3,row=1)

feedback_lbl = Label(main)
feedback_lbl.grid(column=3, row=5)

question_review_lbl = Label(main)
question_review_lbl.grid(column=3, row=6)

true_btn = Button(main, text="True", height=3, width=10, font=("Arial",10), fg="green", command=lambda: btn_click(True))
true_btn.grid(column=2, row=3)

false_btn = Button(main, text="False", height=3, width=10, font=("Arial",10), fg="red",command=lambda: btn_click(False))
false_btn.grid(column=4, row=3)

def create_expression():
    global numbers
    numbers = []
    for count in range(4):
        numbers.append(random.randint(0,10))

    expression = str(numbers[0]) + " + " + str(numbers[1]) + " > " + str(numbers[2]) + " + " + str(numbers[3])

    expression_lbl.configure(text=expression)
    
    

def btn_click(answer):
    global numbers, score
    review_expression = str(numbers[0]) + " + " + str(numbers[1]) + " > " + str(numbers[2]) + " + " + str(numbers[3]) + "\n"
    if answer:
        if (numbers[0] + numbers[1]) > (numbers[2] + numbers[3]):
            feedback_lbl.configure(text="Correct", fg="green")
            score += 1
            review_expression += str(numbers[0] + numbers[1]) + " is greater than " + str(numbers[2] + numbers[3])
        elif (numbers[0] + numbers[1]) == (numbers[2] + numbers[3]):
            feedback_lbl.configure(text="Wrong",fg="red")
            review_expression += str(numbers[0] + numbers[1]) + " is EQUAL to " + str(numbers[2] + numbers[3]) + ". Not greater."
        else:
            feedback_lbl.configure(text="Wrong",fg="red")
            review_expression += str(numbers[0] + numbers[1]) + " is less than " + str(numbers[2] + numbers[3])
    else:
        if (numbers[0] + numbers[1]) < (numbers[2] + numbers[3]):
            feedback_lbl.configure(text="Correct", fg="green")
            score += 1
            review_expression += str(numbers[0] + numbers[1]) + " is less than " + str(numbers[2] + numbers[3])
        elif (numbers[0] + numbers[1]) == (numbers[2] + numbers[3]):
            feedback_lbl.configure(text="Correct",fg="green")
            score += 1
            review_expression += str(numbers[0] + numbers[1]) + " is EQUAL to " + str(numbers[2] + numbers[3]) + ". Not greater."
        else:
            feedback_lbl.configure(text="Wrong",fg="red")
            review_expression += str(numbers[0] + numbers[1]) + " is greater than " + str(numbers[2] + numbers[3])
          
    question_review_lbl.configure(text=review_expression)
  
    score_lbl.configure(text="Score: " + str(score))
    create_expression()

def updateTimer():
  global timer, currentTime, score
  currentTime += 1
  formatted_time = "Time left: " + str(timer - currentTime)
  timer_lbl.configure(text=formatted_time)
  
  if currentTime < timer:
    root.after(1000, updateTimer)
  else:
    message = "Time's up! Your finale score is: " + str(score)
    score_lbl.configure(text=message)
    main.destroy()
  


create_expression()
root.after(1000, updateTimer)
  
root.mainloop()

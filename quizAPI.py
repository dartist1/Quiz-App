import json
import random
import html


import requests
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

API_URLCall = "https://opentdb.com/api.php?amount=25"

response = requests.get(API_URLCall)
data = json.loads(response.text)

questions = data['results']
print(questions)


def check_answer(choice):
    question = questions[currentQuestion]
    selectedOption = choiceButtons[choice].cget('text')

    print(selectedOption)
    print(question["correct_answer"])

    if str(selectedOption) == str(question["correct_answer"]):
        feedbackLabel.config(text="Correct!!", foreground="green")
    else:
        feedbackLabel.config(text="Incorrect!!", foreground="red")

    for button in choiceButtons:
        button.config(state="disabled")
    nextButton.config(state="normal")

def nextQuestion():
    global currentQuestion
    currentQuestion += 1

    if currentQuestion < len(questions):
        showQuestion()
    else:
        messsgebox.showinfo("Quiz Completed")
        root.destroy()


def showQuestion():
    question = questions[currentQuestion]
    questionLabel.config(text=html.unescape(question["question"]))

    choice = question["incorrect_answers"].copy()
    choice.append(question["correct_answer"])
    random.shuffle(choice)

    # html.unescape(choice)
    for i in range(4):
        choiceButtons[i].config(text=choice[i], state="normal")

    feedbackLabel.config(text="")
    nextButton.config(state="disabled")


root = tk.Tk()
root.title("Family Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

questionLabel = ttk.Label(
    root,
    text="Questions",
    anchor="center",
    wraplength=500,
    padding=10
)
questionLabel.pack(pady=10)
choiceButtons = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choiceButtons.append(button)

feedbackLabel = ttk.Label(
    root,
    anchor="center",
    padding=10
)

feedbackLabel.pack(pady=10)


nextButton = ttk.Button(
    root,
    text="Next",
    command = nextQuestion,
    state="disabled"
)

nextButton.pack()

currentQuestion = 0

showQuestion()

root.mainloop()
#
# for question in questions:
#     print(question['question'])
#     print("Options:")
#     for i in range(len(question['incorrect_answers'])):
#         print(f"{i+1}. {question['incorrect_answers'][i]}")
#     print(f"{len(question['incorrect_answers']) + 1}. {question['correct_answer']}")
#     user_answer = int(input("Enter your the number of your answer: "))
#     if user_answer == len(question['incorrect_answers']) + 1:
#         print("Correct!")
#         correct_answers += 1
#     else:
#         print("Incorrect!")
#
#random.randint(0, len(questions) - 1)
# print(f"You got {correct_answers} out of {len(questions)} questions correct.")
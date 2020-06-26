import tkinter as tk
from random import randint
from time import sleep


##generating elements
lbl_questNum = tk.Label()
ent_submit = tk.Entry()
btn_submit = tk.Button()
lbl_question = tk.Label()







###question geneartor
def genQuestion():
    #random number generating
    num1 = randint(100, 1000)
    num2 = randint(100, 1000)
    #(operators 1=+ 2=- 3=* 4=/)#
    operator = randint(1,3)

    #answer generation
    if operator == 1:
        answer = num1 + num2
    elif operator == 2:
        answer = num1 - num2
    elif operator == 3:
        answer = num1 * num2
    elif operator == 4:
        answer = num1 / num2

        

    return [num1, num2, operator, answer]



score = 0
def begin():
    quizWin = tk.Tk()
    #quizWin.title("Quiz")
    
    questNum = 1
    global score
    

    ###event handeling
    def nextQuest(event):

        global score

        quizWin.quit()

        #checking if answer was correct
        userAns = str(ent_submit.get())

        if userAns == str(question[3]):
            score += 1

        ent_submit.delete(0, tk.END)

        
    
    
    #nextQuest(0)
    for i in range(10):
        questNum = i + 1

        question = genQuestion()
        
        lbl_questNum.configure(text="Question {}".format(str(questNum)))
        btn_submit.configure(text = "Next Question")
        #generating question label
        if question[2] == 1:
            opText = '+'
        elif question[2] == 2:
            opText = '-'
        elif question[2] == 3:
            opText = '*'
        elif question[2] == 4:
            opText = '/'

        lbl_question.configure(text="What is {} {} {}".format(str(question[0]), opText, str(question[1])))

        ##rendering elements
        lbl_questNum.pack()
        lbl_question.pack()
        ent_submit.pack()
        btn_submit.pack()

        btn_submit.bind("<Button-1>", nextQuest)

        
        
        quizWin.mainloop()

    quizWin.destroy()
    

    #saving score
    f = open("score.txt", mode='w')
    f.write(str(score))
    f.close()

    import score
    


            

        
        
    

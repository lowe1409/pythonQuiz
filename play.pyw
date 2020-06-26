import tkinter as tk


###menu
#event handeling
def start(event):
    window.destroy()
    import quiz
    quiz.begin()

window = tk.Tk()
window.title("Maths Quiz")

lbl_intro = tk.Label(text="Welcome to Jlowe's supreme quiz \n of the year!!!", width=50, height=10)
lbl_intro2 = tk.Label(text="Test your maths knowledge now!", width=50, height=10)
btn_intro = tk.Button(text="Play!!", background="#20a0ff", width=10, height=2)

lbl_intro.pack()
lbl_intro2.pack()
btn_intro.pack()

btn_intro.bind("<Button-1>", start)

window.mainloop()




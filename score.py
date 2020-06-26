import tkinter as tk
from time import sleep

f = open("score.txt", mode='r')

win = tk.Tk()
win.title("End of quiz!!")

lbl_score = tk.Label(text="You got {} out of 10!!".format(str(f.read())), width=50, height=10)

lbl_score.pack()

win.mainloop()


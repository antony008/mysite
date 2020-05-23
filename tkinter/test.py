import tkinter as tk
base = tk.Tk()
def push():
    print('BOW')
button = tk.Button(base, text='RAIN', command=push, width="20").pack()

base.mainloop()
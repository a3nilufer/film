#import tkinter module
from tkinter import *

# create a tkinter window
root = Tk()			 

# Open window having dimension 100x100
root.geometry('150x150')

# print welcome to welcome user to program
print ('Welcome!')

welcome_label = Label(root, text="Welcome!", font=("Arial", 16), bg="lightblue", fg="black", padx=20, pady=20)
welcome_label.pack()

# Create a Button
btn = Button(root, text = 'Teacher Login', bd = '5',
						command = root.destroy) 

# Set the position of button on the top of window. 
btn.pack(side = 'top') 

btn = Button(root, text = 'Student Login', bd = '5',
						command = root.destroy) 

# Set the position of button on the top of window. 
btn.pack(side = 'top') 

root.mainloop()

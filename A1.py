# Import necessary 
from tkinter import *

# create Window
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

# create a frame to organize elements better
# fame = Frame(master=root, height=200, width=360, bg="#d0efff")

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]
for i in range(4):
    # CONFIGURE ROWS AND COLUMNS TO erise window
    root.columnconfigure(i, weight=1, minisize=75)
    root.rowconfigure(i, weight=1, minisize=50)

for i in range(4):
    
    for j in range(3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j, sticky='nsew')
        label = Label(master=frame, text=nums[i][j], bg='#d0efff')
        label.pack(expand =True, fill='both', padx=3, pady=3)

# the GUI event loop
root.mainloop()
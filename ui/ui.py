from tkinter import *

# Creates a blank window (constructor in Tk class)
root = Tk()

# Creates text
theLabel = Label(root, text="This is too easy")

# Just pack it in there somewhere (no specific placement)
theLabel.pack()

# So that window is always open
# Computers are fast
# If this was not here window would be closed in .0000001 sec
root.mainloop()

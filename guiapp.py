#import tkinter module
import tkinter as tk

def Savetext():
    text_str = text_box.get()
    fx = open('files','w')
    fx.write(text_str)
    fx.close()

# create class for the widdgete to be used
window = tk.Tk()
text_box = tk.Entry(window)
btn = tk.Button(window,text="Save", command=Savetext)

#use created widget on wondow
text_box.pack()
btn.pack()
window.mainloop()

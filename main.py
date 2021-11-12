from tkinter import *
import pyttsx3
root = Tk()
root.title("Text Synthesizer")
root.geometry("800x500")
root.iconbitmap('c:/users/yashu/PycharmProjects/synthesizer')

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

root.mainloop()
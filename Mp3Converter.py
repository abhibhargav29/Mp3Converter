import moviepy.editor as mp
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as font
import time
import threading

#Conversion Function
def convertToAudio():
    result.configure(text="......")
    window.update()
    time.sleep(1)
    try:
        f1 = Video.get()
        f2 = Audio.get()
        clip = mp.VideoFileClip(f1)    
        clip.audio.write_audiofile(f2)
        result.configure(text="DONE")
    except:
        result.configure(text="FAILED")
        

#Main Window
#Basic
window = Tk()
window.geometry("500x200")
window.title("MP3 CONVERTER")
window.configure(bg = "grey")
Myfont = font.Font(family="Calibri", size=16)

#Variables
Video = StringVar()
Audio = StringVar()

#Video
L1 = Label(window, font =Myfont, text="VIDEO FILE :", background="grey")
L1.place(x=100, y=40)
E1 = Entry(window, textvariable = Video)
E1.place(x=215, y=45, width=200)

#Audio
L2 = Label(window, font=Myfont, text="AUDIO FILE :", background="grey")
L2.place(x=98, y=70)
E2 = Entry(window, textvariable = Audio)
E2.place(x=215, y=75, width=200)

#Result Label
result = Label(window, font=Myfont, background="grey")
result.place(x=230, y=150)

#Main Button
convert = Button(window, text="Convert", font=Myfont, command=convertToAudio)
convert.place(x=334, y=105, height=25)

window.mainloop()

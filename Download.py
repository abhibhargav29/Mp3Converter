from pytube import YouTube
import os

#Saved in same location
SAVE_PATH = os.getcwd()

#User input for filename and link
fileName = input("Enter Save File Name:")
link = input("Enter link of You Tube video:")

#Create object of you tube class
yt = YouTube(link) 
mp4files = yt.streams.filter(progressive=True, file_extension="mp4") 
  
#Try downloading
try:
    mp4files.get_highest_resolution().download(output_path=SAVE_PATH, filename=fileName) 
    print("Task Completed!")
except:
    print("Failed")

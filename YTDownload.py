from pytube import YouTube
import os

SAVE_PATH = os.getcwd()
fileName = input("Enter Save File Name:")
link = input("Enter link of You Tube video:")

yt = YouTube(link) 
mp4files = yt.streams.filter(progressive=True, file_extension="mp4") 
  
try:
    mp4files.get_highest_resolution().download(output_path=SAVE_PATH, filename=fileName) 
    print("Task Completed!")
except:
    print("Failed")

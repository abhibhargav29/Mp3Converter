import moviepy.editor as mp

#Conversion Function
def convertToAudio(f1,f2):
    try:
        clip = mp.VideoFileClip(f1)    
        clip.audio.write_audiofile(f2)
        print("DONE")
    except:
        print("FAILED")
        
if __name__=="__main__":
    Video = input("Enter video file Name(must be in same folder)(with extension):")
    Audio = input("New audio file Name(with extension):")

    convertToAudio(Video, Audio)

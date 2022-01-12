# ************************** Speak the text *************************************
#************************************By Rohan Movva*************************************
#*******************************************************************************************

from gtts import gTTS
import os

# Plays the message from a connected speaker. 
def play_sound(message):
    #Call the Google library to convert the text to mp3 file. 
    tts = gTTS(text=message, lang='en')
    filename = '/tmp/temp.mp3'
    tts.save(filename)

    # Playing the converted file
    os.system("mpg321 /tmp/temp.mp3")
    #remove temperory file
    os.remove(filename)
    


    

# **************************Raspberry Pi Button Input Reader *************************************
#************************************By Rohan Movva*************************************
#*******************************************************************************************

#Imports
#GPIO module to get inputs from the Pi
import RPi.GPIO as GPIO


#This method sets the mode for the GPIO pins to input mode. 
def init():

    #Green
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Blue
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Red
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Yellow
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #White
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    

#This method waits for the user input and checks if any of the input buttons are
#selected.
#Yellow = GPIO 10 = Answer A
#Red = GPIO 22 = Answer B
#Blue = GPIO 27 = Answer C
#Green = GPIO 17 = Answer D
#White = GPIO 20 = Home = Answer E
    
def getAnswer():
    
    try:
        answer = '';
        #Wait till the user provides input
        while True:
            if (GPIO.input(17) == 1) :
                answer = "d";
                break;

            elif (GPIO.input(27) == 1) :
                answer = "c";
                break;            

            elif (GPIO.input(22) == 1) :
                answer = "b";
                break;            

            elif (GPIO.input(10) == 1) :
                answer = "a";
                break;

            elif (GPIO.input(20) == 1) :
                answer = "e"; 
                break;            
  
    except KeyboardInterrupt:
        GPIO.cleanup()

    print(answer);
    #return the answer to the calling program. 
    return answer;






# *****************************************Quiz Project*************************************
#****************************************By Rohan Movva*************************************
#*******************************************************************************************


#Imports

# Random API to get a random number within a Range. 
import random
# Time API is used to sleep/wait. 
import time
# Used to read the questions file. 
import configparser
#This is used to pass the parameters
import argparse

# This allows display the text on the LCD. 
import rohan_lcd
# Catches User Inputs with the buttons. 
import rohan_button
# Plays the text from the speaker. 
import rohan_play

import json
import urllib.request as ur
import urllib.parse as par

#Global Variables

#Category Selection 
selectedCategory = ''
#Level Selection
selectedLevel = ''

# Copied it from LCD code. This is needed to display on LCD. 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

#Used to Calculate the Score. 
correctAnswerCount = 0
#Total Questions asked. 
totalQuestionsCount = 0;

LCD = True

#This method is used to collect the initial answers from the user.
#What Category and what level.
#These answers are stored in global variables --
#"selectedCategory" has the Category selection
#"selectedLevel" has the level selection.

def askInitialQuestions():

    #Use Global Variables
    global selectedCategory
    global selectedLevel    
    global LCD;
    #If we are coming back again
    if selectedCategory != "":
        #Ask the user if they want to continue again or if they want to quit.
        if LCD == True:
            rohan_lcd.lcd_string("Yellow = Quit",LCD_LINE_1)
            rohan_lcd.lcd_string("Any Other = Continue",LCD_LINE_2)

        rohan_play.play_sound("Yellow = Quit")
        rohan_play.play_sound("Any Other = Continue")
        #Get the answer
        answer = rohan_button.getAnswer();
        
        if(answer == "a"):
            selectedCategory = "q";
        elif(answer == "b"):
            selectedCategory = "s";

    #If the user selected anything other than Quit
    if selectedCategory != "q":
        
        #Ask Questions
        if LCD == True:
            rohan_lcd.lcd_string("Select Catogory",LCD_LINE_1)
            
        rohan_play.play_sound("Select Catogory")
        
        if LCD == True:
            time.sleep(1);
            rohan_lcd.lcd_string("Yellow = Math",LCD_LINE_1)
            rohan_lcd.lcd_string("Red = Presidents",LCD_LINE_2)
            time.sleep(2);
            rohan_lcd.lcd_string("Blue = General Knowledge",LCD_LINE_1)
            rohan_lcd.lcd_string("Green = Sports",LCD_LINE_2)
            
        rohan_play.play_sound("Yellow = Math")
        rohan_play.play_sound("Red = Presidents")
        rohan_play.play_sound("Blue = General Knowledge")
        rohan_play.play_sound("Green = Sports")        



        #Get the Answer
        answer = rohan_button.getAnswer();

        print("User Answered {}".format(answer));

        #If the user selected Yellow button, then it would be Math. 
        if(answer == "a"):
            selectedCategory = "m";
            if LCD == True:
                rohan_lcd.lcd_string("Selected Math",LCD_LINE_1)
                
            rohan_play.play_sound("Selected Math")
        #If the user selected Red, it would be Presidents. 
        elif(answer == "b"):
            selectedCategory = "p";
            selectedLevel = "e";
            if LCD == True:
                rohan_lcd.lcd_string("Selected Presidents",LCD_LINE_1)
                
            rohan_play.play_sound("Selected Presidents")
        elif(answer == "c"):
            selectedCategory = "g";
            selectedLevel = "e";   
            if LCD == True:
                rohan_lcd.lcd_string("Selected General Knowledge",LCD_LINE_1)
                
            rohan_play.play_sound("Selected General Knowledge")
        elif(answer == "d"):
            selectedCategory = "s";
            selectedLevel = "e";   
            if LCD == True:
                rohan_lcd.lcd_string("Selected Sports",LCD_LINE_1)
                
            rohan_play.play_sound("Selected Sports")
        #Clear the value    
        answer = '';

        if(selectedCategory != "p") :
            #Ask user to select the level
            if LCD == True:
                rohan_lcd.lcd_string("Choose a level",LCD_LINE_1)
                rohan_lcd.lcd_string("",LCD_LINE_2)
                
            rohan_play.play_sound("Choose a level")
            if LCD == True:
                time.sleep(2);
                rohan_lcd.lcd_string("Yellow = Easy",LCD_LINE_1)
                rohan_lcd.lcd_string("Red = Hard",LCD_LINE_2)
                
            rohan_play.play_sound("Yellow = Easy")
            rohan_play.play_sound("Red = Hard")
            #Get the answer
            answer = rohan_button.getAnswer();
            if(answer == "a"):
                selectedLevel = "e";
                if LCD == True:
                    rohan_lcd.lcd_string("Selected Easy",LCD_LINE_1)
                    rohan_lcd.lcd_string("",LCD_LINE_2)
                    
                rohan_play.play_sound("Selected Easy")
                
            elif(answer == "b"):
                selectedLevel = "h";
                if LCD == True:
                    rohan_lcd.lcd_string("Selected Hard",LCD_LINE_1)
                    rohan_lcd.lcd_string("",LCD_LINE_2)

                rohan_play.play_sound("Selected Hard")
                

        time.sleep(2);
    

#This method is used to ask General Knowledge and Sports category questions. 
def askAPIQuestions():
    global correctAnswerCount;
    global totalQuestionsCount;
    global selectedCategory;
    global selectedLevel;
    #URL to get the questions. 
    url = "https://opentdb.com/api_983ab18d07.php?amount=10&type=multiple&"
    if(selectedCategory == "g"):
        url = url + "category=9&"
    elif(selectedCategory == "s"):
        url = url + "category=21&"

    if(selectedLevel == "h"):
        url = url + "difficulty=medium"
    else:
        url = url + "difficulty=easy"
    print (url)
    html = ur.urlopen(url).read()
    data = json.loads(html.decode('utf-8'))    
    
    time.sleep(1);
    count = 0;
    rohan_play.play_sound(data["results"][count]["category"])
    while count < 5:

        rohan_play.play_sound (data["results"][count]["question"])
        if LCD == True:
                rohan_lcd.lcd_string(data["results"][count]["question"],LCD_LINE_1);
        time.sleep(1);        

        answerNum = random.randint(0,3)
        if(answerNum == 0):
            rohan_play.play_sound ("Option A {}".format(data["results"][count]["correct_answer"]))
            if LCD == True:
                rohan_lcd.lcd_string("Option A {}".format(data["results"][count]["correct_answer"]),LCD_LINE_1);
            time.sleep(1);
            rohan_play.play_sound ("Option B {}".format(data["results"][count]["incorrect_answers"][0]))
            if LCD == True:
                rohan_lcd.lcd_string("Option B {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option C {}".format(data["results"][count]["incorrect_answers"][1]))
            if LCD == True:
                rohan_lcd.lcd_string("Option C {}".format(data["results"][count]["incorrect_answers"][1]),LCD_LINE_1);
            time.sleep(1);
            rohan_play.play_sound ("Option D {}".format(data["results"][count]["incorrect_answers"][2]))
            if LCD == True:
                rohan_lcd.lcd_string("Option D {}".format(data["results"][count]["incorrect_answers"][2]),LCD_LINE_2);
            correctAnswer = "a"            
        elif(answerNum == 1):
            rohan_play.play_sound ("Option A {}".format(data["results"][count]["incorrect_answers"][0]))            
            if LCD == True:
                rohan_lcd.lcd_string("Option A {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);            
            time.sleep(1);
            rohan_play.play_sound ("Option B {}".format(data["results"][count]["correct_answer"]))
            if LCD == True:
                rohan_lcd.lcd_string("Option B {}".format(data["results"][count]["correct_answer"]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option C {}".format(data["results"][count]["incorrect_answers"][1]))
            if LCD == True:
                rohan_lcd.lcd_string("Option C {}".format(data["results"][count]["incorrect_answers"][1]),LCD_LINE_1);
            time.sleep(1);
            rohan_play.play_sound ("Option D {}".format(data["results"][count]["incorrect_answers"][2]))
            if LCD == True:
                rohan_lcd.lcd_string("Option D {}".format(data["results"][count]["incorrect_answers"][2]),LCD_LINE_2);
            correctAnswer = "b"
        elif(answerNum == 2):
            rohan_play.play_sound ("Option A {}".format(data["results"][count]["incorrect_answers"][0]))
            if LCD == True:
                rohan_lcd.lcd_string("Option A {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option B {}".format(data["results"][count]["incorrect_answers"][1]))
            if LCD == True:
                rohan_lcd.lcd_string("Option B {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option C {}".format(data["results"][count]["correct_answer"]))
            time.sleep(1);
            if LCD == True:
                rohan_lcd.lcd_string("Option C {}".format(data["results"][count]["incorrect_answers"][1]),LCD_LINE_1);
                
            rohan_play.play_sound ("Option D {}".format(data["results"][count]["incorrect_answers"][2]))
            if LCD == True:
                rohan_lcd.lcd_string("Option D {}".format(data["results"][count]["incorrect_answers"][2]),LCD_LINE_2);
            correctAnswer = "c"
        elif(answerNum == 3):
            rohan_play.play_sound ("Option A {}".format(data["results"][count]["incorrect_answers"][0]))
            if LCD == True:
                rohan_lcd.lcd_string("Option A {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option B {}".format(data["results"][count]["incorrect_answers"][1]))
            if LCD == True:
                rohan_lcd.lcd_string("Option B {}".format(data["results"][count]["incorrect_answers"][0]),LCD_LINE_2);
            time.sleep(1);
            rohan_play.play_sound ("Option C {}".format(data["results"][count]["incorrect_answers"][2]))
            if LCD == True:
                rohan_lcd.lcd_string("Option C {}".format(data["results"][count]["incorrect_answers"][1]),LCD_LINE_1);
            time.sleep(1);
            rohan_play.play_sound ("Option D {}".format(data["results"][count]["correct_answer"]))
            if LCD == True:
                rohan_lcd.lcd_string("Option D {}".format(data["results"][count]["correct_answer"]),LCD_LINE_2);
            correctAnswer = "d"
            
        totalQuestionsCount = totalQuestionsCount +1;
        #Get the answer from the user. 
        answer = rohan_button.getAnswer();
        #Check if the user answered correctly.
        if answer == "e":
            restart();
            break;
        elif answer == correctAnswer:
            correctAnswerCount = correctAnswerCount + 1
            if LCD == True:
                rohan_lcd.lcd_string("Correct!",LCD_LINE_1);
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);
                
            rohan_play.play_sound("Correct!")
            
            print("Your answer is correct. Your current score is {}/{}".format(correctAnswerCount, totalQuestionsCount));
        #If the user answered incorrectly. 
        else:
            if LCD == True:
                rohan_lcd.lcd_string("Incorrect!",LCD_LINE_1);
            rohan_play.play_sound("Incorrect! The correct answer is {}".format(data["results"][count]["correct_answer"]))
            if LCD == True:
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);            
            print("Your answer is incorrect. The correct Answer is {}. Your current score is {}/{} ".format(correctAnswer,correctAnswerCount, totalQuestionsCount))

        time.sleep(2);
        count = count +1;

        
#This method is used to ask presidents category questions. 
def askPresidentQuestions():
    
    #Use global variables for score.     
    global correctAnswerCount;
    global totalQuestionsCount;
    global LCD;    
    
    #Read the presidents.txt file for all the questions. 
    
    #This method is used to ask presidents category questions. 
    #Read the presidents.txt file for all the questions.     
    presidentQuestions = configparser.ConfigParser();
    presidentQuestions._interpolation = configparser.ExtendedInterpolation();
    presidentQuestions.read('presidents.txt');


    count = 0;
    while count < 5:
        #Select a random number for the question selection. 
        num1 = random.randint(1,10)
        if LCD == True:
            rohan_lcd.lcd_string("",LCD_LINE_2);
        #Display the question. 
        rohan_play.play_sound("{}".format(presidentQuestions.get('questions', 'question_{}'.format(num1))))
        #rohan_lcd.lcd_string("{}".format(presidentQuestions.get('questions', 'question_{}'.format(num1))),LCD_LINE_1);
        
        
        #Display the options. 
        if LCD == True:
            rohan_lcd.lcd_string("A: {}".format(presidentQuestions.get('questions', 'question_{}_a'.format(num1))),LCD_LINE_1);

        rohan_play.play_sound("A: {}".format(presidentQuestions.get('questions', 'question_{}_a'.format(num1))))
        time.sleep(1);

        if LCD == True:
            rohan_lcd.lcd_string("B: {}".format(presidentQuestions.get('questions', 'question_{}_b'.format(num1))),LCD_LINE_2);

        rohan_play.play_sound("B: {}".format(presidentQuestions.get('questions', 'question_{}_b'.format(num1))))
        time.sleep(1);
        if LCD == True:
            rohan_lcd.lcd_string("C: {}".format(presidentQuestions.get('questions', 'question_{}_c'.format(num1))),LCD_LINE_1);

        rohan_play.play_sound("C: {}".format(presidentQuestions.get('questions', 'question_{}_c'.format(num1))))
        time.sleep(1);
        if LCD == True:
            rohan_lcd.lcd_string("D: {}".format(presidentQuestions.get('questions', 'question_{}_d'.format(num1))),LCD_LINE_2);

        rohan_play.play_sound("D: {}".format(presidentQuestions.get('questions', 'question_{}_d'.format(num1))))
        #Get the answer from the user. 
        answer = rohan_button.getAnswer();            

        print("You answered {}".format(answer));
        correctAnswer = presidentQuestions.get('questions', 'question_{}_answer'.format(num1));

        totalQuestionsCount = totalQuestionsCount +1;

        #Check if the user answered correctly.
        if answer == "e":
            restart();
            break;
        elif answer == correctAnswer:
            correctAnswerCount = correctAnswerCount + 1
            if LCD == True:
                rohan_lcd.lcd_string("Correct!",LCD_LINE_1);
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);
                
            rohan_play.play_sound("Correct!")
            
            print("Your answer is correct. Your current score is {}/{}".format(correctAnswerCount, totalQuestionsCount));
        #If the user answered incorrectly. 
        else:
            if LCD == True:
                rohan_lcd.lcd_string("Incorrect!",LCD_LINE_1);
            rohan_play.play_sound("Incorrect! The correct answer is {}".format((presidentQuestions.get('questions', 'question_{}_{}'.format(num1, correctAnswer)))))
            if LCD == True:
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);            
            print("Your answer is incorrect. The correct Answer is {}. Your current score is {}/{} ".format(correctAnswer,correctAnswerCount, totalQuestionsCount))

        time.sleep(2);
        count = count +1;


#This method is used to ask Math Categoty questions. 
def askMathQuestion():

    #Collect the score values in a global variable.
    global correctAnswerCount;
    global totalQuestionsCount;
    global LCD;
    
    count = 0;
    #Ask 5 questions
    while count < 5:
        operatorNum = random.randint(0,1)
        correctAnswer = 0
        correctInputAnswer = ''

        #Did the user select easy level?
        if(selectedLevel == "e"):
            #Get 2 random numbers. 
            num1 = random.randint(1,10)
            #Make the second number bigger than the first one. 
            num2 = random.randint(num1,20)

            #Calculate some incorrect values to display them to the user. 
            a = int(num2-num1-1);
            b = int(num2+num1+num1);
            c = int(num2/(num1+1));
            d = int(num2+(num1-1));
            
            #Pick the operator randomly + or - for easy. 
            if(operatorNum == 0):
                operator = "+";
                operatorName = "Plus";
                correctAnswer = num1+num2;
            elif(operatorNum == 1):
                operator = "-";
                operatorName = "Minus";
                correctAnswer = num2 - num1;

        #is the level Hard?
        elif(selectedLevel == "h"):
            #get 2 random numbers
            num1 = random.randint(1,5)
            num2 = random.randint(num1,10)

            #Calculate some incorrect values to display them to the user. 
            a = int(num2+num1+2);
            b = int(num2*(num1+1));
            c = int(num2/(num1+2));
            d = int(num2+num1+23);
            #Pick the operator randomly * or / for hard. 
            if(operatorNum == 0):
                operator = "*";
                operatorName = "Times";
                correctAnswer = num1*num2;
            elif(operatorNum == 1):
                operator = "/";
                operatorName = "Divided by";
                correctAnswer = num2 / num1;

        #Set one of the answers to the correct answer. Pick the option Randomly.     
        answerNum = random.randint(0,3)
        if(answerNum == 0):
            a = correctAnswer
            correctInputAnswer = "a";
        elif (answerNum == 1):
            b = correctAnswer
            correctInputAnswer = "b";
        elif (answerNum == 2):
            c = correctAnswer
            correctInputAnswer = "c";
        elif (answerNum == 3):
            d = correctAnswer
            correctInputAnswer = "d";

        #format the question and options. 
        question = "{} {} {} ?".format(num2, operator, num1);        
        options = "A={}B={}C={}D={}".format(a, b, c, d);

        #display the question and options on the LCD. 
        if LCD == True:
            rohan_lcd.lcd_string(question,LCD_LINE_1);
        #play the question
        rohan_play.play_sound("{}".format(num2));
        time.sleep(.1)
        rohan_play.play_sound("{}".format(operatorName));
        time.sleep(.1)
        rohan_play.play_sound("{}".format(num1));

        #Play the answers
        time.sleep(.5)
        rohan_play.play_sound("Option A={}".format(a));
        time.sleep(.5)
        rohan_play.play_sound("B={}".format(b));
        time.sleep(.5)
        rohan_play.play_sound("C={}".format(c));
        time.sleep(.5)
        rohan_play.play_sound("D={}".format(d));
        time.sleep(.5)
        if LCD == True:
            rohan_lcd.lcd_string(options,LCD_LINE_2);
        #get the answer from the user. 
        answer = rohan_button.getAnswer();            
        #Increase the total questions count. 
        totalQuestionsCount = totalQuestionsCount +1;
        #Validate the answer and if its correct, increase the score. 
        if answer == "e":
            restart();
            break;
        elif answer == correctInputAnswer:
            correctAnswerCount = correctAnswerCount + 1
            if LCD == True:
                rohan_lcd.lcd_string("Correct!",LCD_LINE_1);
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);            

            rohan_play.play_sound("Correct!");
            print("Your answer is correct. Your current score is {}/{}".format(correctAnswerCount, totalQuestionsCount));
        #If the answer is incorrect, let the user know. 
        else:
            if LCD == True:
                rohan_lcd.lcd_string("Incorrect!",LCD_LINE_1);
                rohan_lcd.lcd_string("Score = {}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_2);
                
            rohan_play.play_sound("Incorrect! The correct answer is {}".format((correctAnswer)))
            print("Your answer is incorrect. The correct Answer is {}. Your current score is {}/{} ".format(correctAnswer,correctAnswerCount, totalQuestionsCount))

        time.sleep(2);
        count = count +1;



def processAnswers():
    global LCD;
    global selectedCategory;
    
    if selectedCategory == "m":
        askMathQuestion();
    elif selectedCategory == "p":
        askPresidentQuestions();
    elif selectedCategory == "g" or selectedCategory == "s":
        askAPIQuestions();

    print("***********************************")
    print("Your FINAL score is {}/{}".format(correctAnswerCount, totalQuestionsCount))
    print("***********************************")
    if LCD == True:
        rohan_lcd.lcd_string("FINAL Score={}/{}".format(correctAnswerCount, totalQuestionsCount),LCD_LINE_1);

    rohan_play.play_sound("FINAL Score={}".format(correctAnswerCount));
    time.sleep(2);

def restart():
    global selectedCategory
    global selectedLevel
    global LCD;

    if LCD == True:
        rohan_lcd.lcd_string("Ok Restarting ..",LCD_LINE_2);

    rohan_play.play_sound("Ok .. Restarting ..");
    selectedCategory = "";  
    

#*****Starting Point***********

#Only Run the init methods once.
rohan_lcd.lcd_init();
rohan_button.init();

parser = argparse.ArgumentParser();
parser.add_argument('LCD', default='False', help = 'True will enable LCD')

if(parser.parse_args().LCD == 'True'):
    LCD = True
else:
    LCD = False

#print LCD;


#Go forever till the user quits
while True:
    askInitialQuestions();
    #The user selected to end the game.
    #Show the final score and do the cleanup.
    #Keep the program running for someone to play again.
    print (selectedCategory);
    if selectedCategory == "q":
        rohan_lcd.lcd_string("Final Score={}".format(correctAnswerCount),LCD_LINE_1);
        rohan_lcd.lcd_string("Goodbye",LCD_LINE_2);
        time.sleep(5);
        selectedCategory = "";
        correctAnswerCount = 0;
        totalQuestionsCount = 0;
        rohan_lcd.lcd_string("",LCD_LINE_1);
        rohan_lcd.lcd_string("",LCD_LINE_2);
        time.sleep(5);

    processAnswers();


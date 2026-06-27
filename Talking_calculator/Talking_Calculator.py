import pyttsx3
from simpleeval import simple_eval
def speak(text):
    engine=pyttsx3.init() 
    voices=engine.getProperty('voices')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate',160)
    engine.setProperty('voice',voices[1].id)
    engine.say(text) 
    print(text) 
    engine.runAndWait() 

def speak1(emoji,text):
    engine=pyttsx3.init() 
    voices=engine.getProperty('voices')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate',160)
    engine.setProperty('voice',voices[1].id)
    engine.say(text) 
    print(emoji,text) 
    engine.runAndWait() 
    
speak1("📟","welcome to our easiest calculator to access") 
def see(m):
    speak("do you want to continue , answer in yes or no") 
    c=input("").lower() 
    if(c=="yes"): 
        speak("continue the calculation")
        d=input()
        m+=d   
        return m
    elif(c=='no'):
        speak("thank you , for using our calculator for calculation") 
        return None
    else:
        speak("answer in yes or no only")
        see(m)
def calculator(s): 
    while(True):  
        try:
            v=str(simple_eval(s))
            speak("the answer for the given expression: "+v) 
            result=see(v) 
            if result is None:
                break
            else:
                s=result
        except Exception as e:
            speak("error found"+str(e))
            s=""   
            break
def main():
    speak("are you interested to do the mathematical calculations ,answer in yes or no:") 
    b=input("").lower() 
    if(b=="yes"): 
        speak("enter the expression:") 
        a=input()
        s=""
        s+=a
        calculator(s) 
    elif(b=='no'):
        speak("thank you , if you need to access again just run the program")
    else:
        speak("answer in yes or no only")
        main()
main()

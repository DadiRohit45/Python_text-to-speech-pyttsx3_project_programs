import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
speak("welcome to ai cartoon recomender")
speak("enter your age")
age=input()
speak("specify your mood (happy,sad,bored,excited)?")
mood=input()
speak("what type of cartoons you like basically (action,funny,adventure)")
type=input()
speak("Ai Recomendations")
if(age>=18):
    if(mood=="happy" and type=="action"):
        speak(" you should watch : jakiechan ")
    elif(mood=="sad" and type=="funny"):
        speak(" you should watch : Shinchan ")
    elif(mood=="bored" and type=="adventure"):
        speak(" you should watch : doreamon ")
else:
    speak("just see anime this cartoons are all for kids")

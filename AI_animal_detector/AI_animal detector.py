import pyttsx3

def speak(text):
    engine=pyttsx3.init() 
    voices=engine.getProperty('voices')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate',160)
    engine.setProperty('voice',voices[1].id)
    engine.say(text) 
    print("♀ Sokuladi:",text) 
    engine.runAndWait() 

def speak1(emoji,text):
    engine=pyttsx3.init() 
    voices=engine.getProperty('voices')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate',160)
    engine.setProperty('voice',voices[1].id)
    engine.say(text) 
    print("♀ Sokuladi:",emoji,text) 
    engine.runAndWait() 
    
speak1("🐾","lets find the animals")
speak("does the animal has 4 legs")
legs=input()
speak("does the animal swim")
swim=input()
speak("does the animal barks")
bark=input()
speak("is it a pet animal")
pet=input()
if(legs=="yes" and swim=="yes" and bark=="yes" and pet=="yes"):
    speak1("🐕","I think it is a Dog")
elif(legs=="yes" and swim=="no" and bark=="no" and pet=="yes"):
    speak1("🐈","I think it is a cat")
elif(legs=="yes" and swim=="no" and bark=="yes" and pet=="no"):
    speak1("🦁","I think it is a Lion")
elif(legs=="yes" and swim=="yes" and bark=="yes" and pet=="no"):
    speak1("🐅","I think it is a Tiger")
elif(legs=="no" and swim=="yes" and bark=="no" and pet=="yes"):
    speak1("🐬","I think it is a Fish")
elif(legs=="no" and swim=="yes" and bark=="no" and pet=="no"):
    speak1("𖨆","I think it is a human")
else:
    speak("there is no such animal")

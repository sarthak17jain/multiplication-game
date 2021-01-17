import random,easygui
easygui.msgbox("Muliplication Game.Made by Sarthak Jain. Are you ready to start?")
chances = easygui.integerbox("How many questions do you want to practise?")
tries = 0
score = 0
c = easygui.integerbox("Select your multiplicand range 1", argLowerBound=0, argUpperBound=999 )
cc = easygui.integerbox("Select your multiplicand range 2" , argLowerBound=0, argUpperBound=999 )
e = easygui.integerbox("Select your multiplier range 1" , argLowerBound=0, argUpperBound=999 )
ee = easygui.integerbox("Select your multiplier range 2" , argLowerBound=0, argUpperBound=999 )

for i in range(0, chances):
    t = random.randint (c, cc)
    u = random.randint (e, ee)
   
    answer = easygui.integerbox (str (t) + "*" + str (u), argLowerBound=0, argUpperBound=9999 )
    if answer == 0:
        easygui.msgbox("Sorry, that's the wrong answer")
        continue
    if not answer: break
    correctanswer = t*u
    if answer == correctanswer:
        easygui.msgbox("Great Job! That's the correct answer")
        score = score + 1
    else:
        easygui.msgbox("Sorry, that's the wrong answer. The correct answer was " + str (correctanswer) )        
        tries = tries + 1
    
    
    
easygui.msgbox("Your score is " + str (score) + " out of " + str (chances) )


#Jakub Novak

#prepare the question that you'll have to answer to get your temperature.
temp = round((int(input("What is the temperature outside? "))),1)

#define our function.
def convert(C):
    F = (C * 9/5)+32
    return F
F = convert(temp)

#use if and elif to get printed clothing recomendation.
def evaluator(F):
    if F <= 30:
        print(f"Temp is {F}. Take your coat, it's freezing.")
    elif F <= 50:
        print(f"Temp is {F}. You can leave your coat home.")
    elif F <= 80:
        print(f"Temp is {F}. Take your shorts.")
    else:
        print(f"Temp is {F}. We're going to swim today.")
evaluator(F)
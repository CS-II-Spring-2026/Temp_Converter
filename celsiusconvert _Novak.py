#Jakub Novak
#define our function.
def convert(C):
    return (C * 9/5)+32
#prepare the question that you'll have to answer to get your temperature.
temp = round(convert(int(input("What is the temperature outside? "))),1)

#use if and elif to get printed clothing recomendation.
if temp <= 30:
    print(f"Temp is {temp}. Take your coat, it's freezing.")
elif temp <= 50:
    print(f"Temp is {temp}. You can leave your coat home.")
elif temp <= 80:
    print(f"Temp is {temp}. Take your shorts.")
else:
    print(f"Temp is {temp}. We're going to swim today.")

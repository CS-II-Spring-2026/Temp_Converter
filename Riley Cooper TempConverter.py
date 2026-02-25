#convert C to F
#uses the F result to return clothing advice
C = float (input( "What is the temp outside in Celcius?: "))

F = round(((C * 9/5 ) + 32), 1)

print(F)

if F >= 80:
    print(f"The temp outside is {F}F so you should wear a shirt")
elif F >= 50:
    print(f"The temp outside is {F}F so you should wear a jacket")
elif F >= 32:
    print(f"The temp outside is {F}F so you should wear a coat")
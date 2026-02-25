F = float(input("Input temp in Fahrenheit: "))

def c_to_f(f):
    return (f - 32) * 5/9

def weather_advice(fahrenheit):
    C = c_to_f(fahrenheit)
    print("Temperature in Celsius:", C)
    
    if C >= 24:
        print("Super warm outside, you only need short sleeves and shorts.")
    elif 8 <= C < 24:
        print("It is nice, but bring a sweatshirt and maybe even a coat.")
    else:
        print("You need a coat, it is cold outside.")

weather_advice(F)

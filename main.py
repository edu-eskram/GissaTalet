import random
tal = random.randint(1,10)
x = 1
while x <= 3:
    gissning = int(input(f"Försök {x}: Gissa Talet: "))
    if gissning == tal:
        print("Rätt gissat!")
    else:
        print("Fel gissat")
    x = x + 1
    

    
   


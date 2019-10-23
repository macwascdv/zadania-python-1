import math
print("""Witam w programie 'magiczna delta'.
Wykorzystujemy tutaj postać 'delta = b^2-4ac'.
Postępuj zgodnie z instrukcjami zamieszczonymi na ekranie""")
a =int(input("Wartość a wynosi = "))
b =int(input("Wartość b wynosi = "))
c=int(input("Wartość c wynosi = "))

Delta = b**2-(4*a*c)
print(Delta)
if Delta>0:
    print("Twoje równanie posiada 2 rozwiązania")
    DT=math.sqrt(Delta)
    x1 = (-b-DT)/(2*a)
    x2=  (-b+DT)/(2*a)
    print("x1 wynosi = "+str(x1)+" x2 wynosi = "+str(x2))
    input("Naciśnij enter by wyjść")
elif Delta==0:
    DT=math.sqrt(Delta)
    print("Twoje równanie posiada 1 rozwiązanie")
    x1 = (-b-DT)/(2*a)
    print("x1 wynosi = "+str(x1))
    input("Naciśnij enter by wyjść")
else:
    print("Delta jest mniejsze od zera")
    print("Twoje równanie nie posiada rozwiązań") 
    input("Naciśnij enter by wyjść")

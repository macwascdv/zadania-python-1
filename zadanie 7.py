from fractions import Fraction

def sumowanie (x,y):
    return x+y
print("Witam w programie dodawania ulamkow zwyklych")
x= Fraction(input("Podaj pierwszy ulamek: "))
y= Fraction(input("Podaj drugi ulamek: "))
x2=sumowanie(x,y)
print("Twoj wynik to: " + str(x2))
input("Wcisnij dowolny klawisz, by zakonczyc prace programu")
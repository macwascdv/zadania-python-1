decyzja= "t"

print("Program do liczenia objetosc prostopadloscianu")
while(decyzja=="t"):
    try:
         
       a=float(input("wpisz bok a= "))
       b=float(input("wpisz bok b="))
       c=float(input("wpisz bok c="))
       objetosc=a*b*c
       print(objetosc)
    except ValueError:
         print("wporawdzona zla wartosc")
    print("Czy wykonać jeszcze raz? t/n")
    decyzja=input()
     
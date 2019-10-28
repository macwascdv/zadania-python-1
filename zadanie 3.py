print("Ten program zamień temperaturę na inna skale")
decyzja="t"
while(decyzja=="t"):
 try:
    temperatura = input("Wybierz skalę początkową - f/c: ")
    if (temperatura=="f"):
           x= int(input("wpisz temperaturę: "))
           y=(x-32)*(5/9)
           print("Twoja temperatura w Celsjuszach wynosi: ")
           print("{:.2f} stopni Celsjusza".format(y))
           decyzja=input("Czy chcesz ponownie uruchomic program? t/n ")
    elif (temperatura=="c"):
        x= int(input("wpisz temperaturę: "))
        y=(x*9/5)+32
        print("Twoja temperatura wynosi: ")
        print("{:.2f} Fahrenheit".format(y))
        decyzja=input("Czy chcesz ponownie uruchomic program? t/n ")
    else:
        print("Musisz wpisac f lub c")
        decyzja=input("Czy chcesz sprobowac ponownie? t/n ")
 except ValueError:
     print("Podano inną wartosc niz liczba")
     input("Czy chcesz sprobowac ponownie? t/n ")

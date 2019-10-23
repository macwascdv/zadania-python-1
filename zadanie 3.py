print("Ten program zamień temperaturę na inna skale")
temperatura = input("Wybierz skalę początkową - f/c: ")
x= int(input("wpisz temperaturę: "))
if (temperatura=="f"):
    y=(x-32)*(5/9)
    print("Twoja temperatura w Celsjuszach wynosi: ")
    print("{} stopni Celsjusza".format(y))
    input()
elif (temperatura=="c"):
    y=(x*9/5)+32
    print("Twoja temperatura wynosi: ")
    print("{} Fahrenheit".format(y))
    input()

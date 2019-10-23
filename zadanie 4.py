def km_m(k):
    return k*0.62137
def m_km(m):
    return m*1.60934
print("Witam w programie zmiany kilometrów na mile oraz mil na kilometry")
decyzja = input("Wybierz szukaną jednostkę - k/m  ")
if (decyzja=="m"):
    x=int(input("Wpisz ilosc kilometrow: "))
    x1=km_m(float(x))
    print("Twoja odleglosc to {} mil".format(x1))
if (decyzja=="k"):
    x=int(input("Wpisz ilosc mil: "))
    x1=m_km(float(x))
    print("Twoja odleglosc to {} kilometrow".format(x1))
    
input("Wcisnij dowolny klawisz")

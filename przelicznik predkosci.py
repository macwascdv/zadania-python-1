def km_ms(vk):
    return vk*1000/3600
def ms_km(vm):
    return vm*3.6
print("Ten program sluzy do przeliczenia km/h na m/s, oraz m/s na km/h")
decyzja=input("Wybierz predkosc, jaka chcesz uzyskac - kmh/ms: ")
if (decyzja=="kmh"):
    x=int(input("wpisz wartosc predkosci m/s: "))
    x1=ms_km(float(x))
    print("Twoja predkosc wynosi {}km/h".format(x1))
   
if (decyzja=="ms"):
     x=int(input("wpisz wartosc predkosci km/h: "))
     x1=km_ms(float(x))
     print("Twoja predkosc wynosi {}m/s".format(x1))
input("Nacisnij dowolny klawisz, aby zakonczyc prace")

decyzja="t"
while(decyzja=="t"):
    try:
         x=int(input("Wprowadz liczbe: "))
         for i in range (1, x+1):
             if((x%i)==0):
                 print(i)
    except ValueError:
        print("Musisz wprowadzić liczbę")
        decyzja=input("Czy chcesz powtórzyć? t/n ")

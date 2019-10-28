print("Program do...Nie wiem własciwie po co")
decyzja="t"
while(decyzja=="t"):
    try:
        x=int(input("wprowadz liczbe:"))
        for i in range(0, 11):
            x1=float(x)
            a=x1*i
            print("{}x{}={}".format(x1,i,a))
    except ValueError:
        print("Musisz podac liczbe")
        decyzja=input("Czy chcesz powtorzyc? t/n ")
        

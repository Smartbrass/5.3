Minimal_Funds = input("Минимальный кеш:")
Ivan_Funds = input("Накопления Ивана:")
Mike_Funds = input("Накопления Майка:")

if int(Ivan_Funds) >= int(Minimal_Funds) and int(Mike_Funds) >= int(Minimal_Funds):
    print("2")
elif int(Ivan_Funds) >= int(Minimal_Funds) and int(Mike_Funds) <= int(Minimal_Funds):
     print("Ivan")   
elif int(Ivan_Funds) <= int(Minimal_Funds) and int(Mike_Funds) >= int(Minimal_Funds):
     print("Mike")
elif int(Ivan_Funds) <= int(Minimal_Funds) and int(Mike_Funds) <= int(Minimal_Funds) and (int(Mike_Funds) + int(Ivan_Funds)) >= int(Minimal_Funds):
     print("1") 
else:
    print("0")
import math

optionList = ["Soma","Subtração","Multiplicação","Divisão","Potenciação","Radiciação","Sair"]
optionIndex = 0
valA = 0
valB = 0
valC = 0

while optionList[optionIndex-1] != 7:
    for i, val in enumerate(optionList,start=1):
        print(f"{i} - {val}")
    optionIndex = int(input("Selecione a opção: \n"))

    print(f"Você selecionou {optionList[optionIndex-1]}")

    if optionList[optionIndex-1] == "Soma":
        valA = int(input("Informe valor 1: \n"))
        valB = int(input("Informe valor 2: \n"))
        print(f"\n{valA} + {valB} = {valA + valB}")
    elif optionList[optionIndex-1] == "Subtração":
        valA = int(input("Informe valor 1: \n"))
        valB = int(input("Informe valor 2: \n"))
        print(f"\n{valA} - {valB} = {valA - valB}")
    elif optionList[optionIndex-1] == "Multiplicação":
        valA = int(input("Informe valor 1: \n"))
        valB = int(input("Informe valor 2: \n"))
        print(f"\n{valA} * {valB} = {valA * valB}")
    elif optionList[optionIndex-1] == "Divisão":
        valA = int(input("Informe valor 1: \n"))
        valB = int(input("Informe valor 2: \n"))
        if valB == 0:
            print("\nNão é possivel dividir por 0")
        else:
            print(f"\n{valA} / {valB} = {valA / valB}")
    elif optionList[optionIndex-1] == "Potenciação":
        valA = int(input("Informe valor 1: \n"))
        valB = int(input("Informe valor 2: \n"))
        print(f"\n{valA} ^ {valB} = {valA ** valB}")
    elif optionList[optionIndex-1] == "Radiciação":
        valA = int(input("Informe o valor: \n"))
        print(f"\nRaiz de {valA} = {math.sqrt(float(valA))}")
    elif optionList[optionIndex-1] == "Sair":
        break
    print("\n")
def inverterString(string):
    inverterS = ""
    for i in range(len(string)-1, -1, -1):
        inverterS += string[i]
    return inverterS


stringOficial = input("Digite uma string: ")
stringInvertida = inverterString(stringOficial)
print(stringInvertida)
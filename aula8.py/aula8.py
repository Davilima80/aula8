#4

medidasDosLadosX = input("Digite uma medida para o triângulo: ")
medidasDosLadosY = input("Digite uma medida para o triângulo: ")
medidasDosLadosZ = input("Digite uma medida para o triângulo: ")


if medidasDosLadosX == medidasDosLadosY == medidasDosLadosZ:
    print("o seu triângulo é equilatero")
elif medidasDosLadosX == medidasDosLadosY or medidasDosLadosX == medidasDosLadosZ or medidasDosLadosZ == medidasDosLadosY:
     print("o seu triângulo é isoceles")
else:
     print("o seu triângulo é escaleno")

#5

num = 10

if num % 5 == 0 and num % 7 == 0:
    print("o", num,"é múltiplo de 5 ou 7")
else:
    print("o", num,"não é múltiplo de 5 ou 7")

#6

if num >= 10:
    print("o número", num ,"é maior que 10 e não é negativo")
else:
    print("o número", num ,"é menor que 10 ou negativo")

#7

if num % 3 == 0 or num % 5 == 0:
    print("o número",num,"é divisível por 3 ou 5")
else:
    print("o número",num,"não é divisível por 3 ou 5")
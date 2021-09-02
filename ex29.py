nota1 = float(input("Digite a 1 nota : "))
nota2 = float(input("Digite a 2 nota : "))
nota3 = float(input("Digite a 3 nota : "))
nota4 = float(input("Digite a 4 nota : "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >7 :
    print("Parabéns você passou com as nota : {} , {} , {} , {} e a média de : {}".format(nota1,nota2,nota3,nota4,media))

elif media >=5 and media <=7 :
    print("Dependencia com a média de : {}".format(media))    
elif media <5:
    print("Você ficou em recuperação com as notas = {} , {} , {} , {} e a media = {}".format(nota1, nota2,nota3,nota4,media))
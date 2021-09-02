altura = float(input("Informe a Altura da sua parede : "))
comprimento = float(input("Informe o Comprimento de sua Parede : "))

metrosquad = altura * comprimento
tinta = metrosquad / 3

tinta2 = metrosquad // 3.6 #Quantidade de latas que ele tera que comprar
restotinta = metrosquad% 3.6 #o resto da divisao que vai somar

valor1 = tinta2 * 107


valortudo = (tinta2 + restotinta) * 107

print("A quantidade de latas que você vai precisar para printar um parede de área de : {} vai ser de : {}".format(metrosquad , tinta2))
print("O preço total com a tinta a mais que deverá ser comprada de : {} será de : {}".format(restotinta,valortudo))

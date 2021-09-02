premio = float(input("Qual o valor do prêmio da loteria : "))

cofresestaduais = (premio * 7)/100 #VALOR DO IMPOSTO PAGO PARA OS COFRES ESTADUAIS

premiodescontado = premio * 0.93

primeiro =(premiodescontado * 46) /100
segundo = (premiodescontado * 32) /100
terceiro = (premiodescontado * 22)/100

print ("O valor do prêmio com desconto é de : {} $".format(cofresestaduais))
print ("O primeiro ganhador tem direito a {} o segundo tem direito à {} o terceiro tem direito à {}".format(primeiro,segundo,terceiro))
print("O prêmio descontado é de : {}".format(premiodescontado))
print("O imposto foi de 7%")
#10) Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
#valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias).

val = float(input("Insira o valor, por favor:R$"))
temp = float(input("Agora, o tempo em dias:"))
tax = float(input("Por fim, coloque a taxa de juros:R$"))



pres = val +(val*(tax/100)*temp)

print("Com bases nesses dados, o valor da sua prestação em atraso equivale a R$",pres)


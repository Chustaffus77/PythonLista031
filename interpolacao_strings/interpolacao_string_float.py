valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

#formatação apenas como valor float
#print("valor 1: {:f}".format(valor1))

#formatação float com decimal em 2 dígitos
#print("valor 1: {:.2f}".format(valor1))
#print("valor 2: {:.2f}".format(valor2))
#print("valor 3: {:.2f}".format(valor3))


#formatação float com separador de milhares e decimal em 2 dígitos
#print("valor 2: {:,.2f}".format(valor2))

#-----------------------------------------------------------------------------------------------------------------------

#formatação float, com total de 10 digitos (númeos e ponto), sendo 2 decimais

print("Valor 1: {:10.2f}".format(valor1))
print("Valor 2: {:10.2f}".format(valor2))
print("Valor 3: {:10.2f}".format(valor3))



#semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessário.

print("Valor 1: {:010.2f}".format(valor1))
print("Valor 2: {:010.2f}".format(valor2))
print("Valor 3: {:010.2f}".format(valor3))
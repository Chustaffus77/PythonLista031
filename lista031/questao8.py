#Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
#programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
#valor do consumo médio do automóvel, em quilômetros por litro.

#média = km/l

print("Vamos lá! Para evitar infortúnios, respondas as perguntas a seguir para você saber a quantia exata de gasolina pra sua viagem!")

d = float(input("Qual é a distância que será percorrida (em km)?"))
cm = float(input("Por fim, qual é o valor do consumo médio do seu automóvel(em km/l)?"))

l = d / cm

print(f"Com base nos dados apresentados, serão necessários {l:.0f} litros de gasolina para chegar ao local de destino! Espero ter sido útil!")

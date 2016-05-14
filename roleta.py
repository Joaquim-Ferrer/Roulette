import random

numeros_ganhar = input("insira o numero de numeros em que ganhas")
hipoteses = [x for x in range(0,37)]

banca_inicial = input("insira a banca inicial")
aposta_inicial = input("insira a aposta inicial")
aposta = aposta_inicial
banca = banca_inicial

max_money = banca_inicial
min_money = 10000

sum0 = 0
sum1 = 0

n=0

for n in range(2000) :

	banca = banca_inicial
	aposta = aposta_inicial
	numero_de_vezes = 0
	max_money = banca_inicial
	
	while banca > 0:
	
		numero_que_saiu = random.choice(hipoteses)
		numero_de_vezes = numero_de_vezes +1
	
		if( numero_que_saiu <= numeros_ganhar and numero_que_saiu != 0):
			banca = banca + aposta
			if(banca > max_money):
				max_money = banca
		else:	
			banca = banca - aposta
			aposta = min(100, aposta * 36/numeros_ganhar)
	if(max_money < 550):
		min_money = max_money
		n +=1
	
	sum0 = sum0 + max_money
	sum1 = sum1 + numero_de_vezes

media = sum0 / 2000.0
media1 = sum1 / 2000.0

print("voce chegou em media aos " + str(media) + "euros! E jogaste em media" + str(media1) + " vezes!")
print("vezes menor 550 min = " + str(n))

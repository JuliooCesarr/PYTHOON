print('Alunos-PLP Unifavip 2022.2')

número = input('escolha um número qualquer')
print(f'O número informado foi {número}')

número1 = float(input("diga o primeiro número: "))
número2 = float(input("diga o segundo número: "))
soma = número1 + número2
print(f'a soma de {número1} e {número2} é: {soma}')

nota1 = float(input('diga sua primeira nota: '))
nota2 = float(input('diga a segunda: '))
nota3 = float(input('a terceira: '))
nota4 = float(input('e por último, a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é: {media}")

metros = float(input("digite o valor em metros: "))
cm = metros * 100
print(f"{metros} metros é igual a {cm} centímetros")

import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo com raio {raio} é: {area}")

lado = float(input("Digite o tamanho do lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print(f"A área do quadrado com lado {lado} é: {area}")
print(f"O dobro da área é: {dobro_area}")

valor_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_total = valor_por_hora * horas_trabalhadas
print(f"O seu salário total neste mês é: R${salario_total:.2f}")

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius")

celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit = 9 / 5 * ((celsius + 32))
print(f"{celsius} graus Celsius é igual a {fahrenheit:.}")

num1_int = int(input("Digite o primeiro número inteiro: "))
num2_int = int(input("Digite o segundo número inteiro: "))
num3_real = float(input("Digite o número real: "))
produto = (2 * num1_int) * (num2_int / 2)
print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
soma = (3 * num1_int) + num3_real
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
cubo = num3_real ** 3
print(f"O terceiro número elevado ao cubo é: {cubo}")

altura = float(input("Digite a altura da pessoa em metros: "))
peso_ideal = (72.7 * altura) - 58
print(f"Para uma altura de {altura:.2f} metros, o peso ideal é: {peso_ideal:.2f} kg")

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Para um homem com altura de {altura:.2f} metros, o peso ideal é: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Para uma mulher com altura de {altura:.2f} metros, o peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")

peso = float(input("Digite o peso total de peixes (em quilos): "))
limite = 50
excesso = 0
multa = 0
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
    print(f"Peso excedente: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R${multa:.2f}")
else:
    print("Peso dentro do limite estabelecido.")

valor_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 3
capacidade_lata = 18
preco_lata = 80.00
litros_necessarios = area / cobertura_por_litro
latas_necessarias = (litros_necessarios / capacidade_lata)
import math
latas_comprar = math.ceil(latas_necessarias)
preco_total = latas_comprar * preco_lata
print(f"Para pintar uma área de {area:.2f} m², você precisará de:")
print(f"- {latas_comprar} lata(s) de tinta")
print(f"- O preço total será de R${preco_total:.2f}")

area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6
folga = 0.1
litros_base = area_a_pintar / cobertura_por_litro
litros_totais = litros_base * (1 + folga)
print(f"Quantidade total de litros necessários (com folga de 10%): {litros_totais:.2f} litros")

print(f"Opção 1: Apenas latas de 18 litros")
capacidade_lata = 18
preco_lata = 80.00
litros_necessarios_latas = litros_totais
latas_necessarias_exato = litros_necessarios_latas / capacidade_lata
preco_total_latas = latas_comprar * preco_lata
import math
latas_comprar = math.ceil(latas_necessarias_exato)
print(f"- Quantidade de latas a comprar: {latas_comprar}")
print(f"- Preço total: R${preco_total_latas:.2f}")

capacidade_galao = 3.6
preco_galao = 25.00
galoes_necessarios_exato = litros_totais / capacidade_galao
galoes_comprar = math.ceil(galoes_necessarios_exato)
preco_total_galoes = galoes_comprar * preco_galao
print(f"\nOpção 2: Apenas galões de 3,6 litros")
print(f"- Quantidade de galões a comprar: {galoes_comprar}")
print(f"- Preço total: R${preco_total_galoes:.2f}")
num_latas_misto = int(litros_totais / capacidade_lata)
litros_restantes = litros_totais - (num_latas_misto * capacidade_lata)
num_galoes_misto = math.ceil(litros_restantes / capacidade_galao)
preco_total_misto = (num_latas_misto * preco_lata) + (num_galoes_misto * preco_galao)
print(f"\nOpção 3: Mistura de latas e galões (para minimizar desperdício e custo)")
print(f"- Quantidade de latas a comprar: {num_latas_misto}")
print(f"- Quantidade de galões a comprar: {num_galoes_misto}")
print(f"- Preço total: R${preco_total_misto:.2f}")
print("\n--- Resultados das Opções de Compra ---")
print(f"\nOpção 1: Apenas latas de 18 litros")
print(f"- Quantidade de latas a comprar: {latas_comprar}")
print(f"- Preço total: R${preco_total_latas:.2f}")
print(f"\nOpção 2: Apenas galões de 3,6 litros")
print(f"- Quantidade de galões a comprar: {galoes_comprar}")
print(f"- Preço total: R${preco_total_galoes:.2f}")
print(f"\nOpção 3: Mistura de latas e galões (para minimizar desperdício e custo)")
print(f"- Quantidade de latas a comprar: {num_latas_misto}")
print(f"- Quantidade de galões a comprar: {num_galoes_misto}")
print(f"- Preço total: R${preco_total_misto:.2f}")

tamanho_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))
tamanho_bits = tamanho_mb * 8
velocidade_bps = velocidade_mbps * 1_000_000
tempo_segundos = tamanho_bits / velocidade_bps
tempo_minutos = tempo_segundos / 60
print(f"\nTempo aproximado de download: {tempo_minutos:.2f} minutos")


vetor = []
quantidade_elementos = int(input("Digite quantos números inteiros deseja adicionar ao vetor: "))
for i in range(quantidade_elementos):
  while True:
    try:
      numero = int(input(f"Digite o {i+1}º número inteiro: "))
      vetor.append(numero)
      break
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")
print(f"\nVetor preenchido: {vetor}")
while True:
  try:
    numero_pesquisa = int(input("\nDigite um número inteiro para pesquisar no vetor: "))
    break
  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
if numero_pesquisa in vetor:
  posicao = vetor.index(numero_pesquisa)
  print(f"O número {numero_pesquisa} existe no vetor e foi digitado na posição: {posicao}")
else:
  print(f"O número {numero_pesquisa} não existe no vetor.")


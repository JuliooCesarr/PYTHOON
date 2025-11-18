for i in range(1, 11, +1):
  print(i)

x = 2
while x < 52:
  print(x)
  x += 2

numero = int(input("Digite um número inteiro: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

soma = 0
for i in range(1, 101):
  soma += i
print(f"A soma de todos os números de 1 a 100 é: {soma}")

for i in range(10, 0, -1):
  print(i)
else:
  print("fogo!")

programação = ["p","r","o","g","r","a","m","a","ç","ã","o" ]
for n in programação:
  print(n)

nota1 = float(input('diga sua primeira nota: '))
nota2 = float(input('diga a segunda: '))
nota3 = float(input('a terceira: '))
nota4 = float(input('a quarta nota: '))
nota5 = float(input('a quinta e última: '))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"A média das notas é: {media}")

maior_numero = float('-inf')
for i in range(1, 11):
  numero = float(input(f"Digite o {i}º número: "))
  if numero > maior_numero:
    maior_numero = numero
print(f"O maior número digitado é: {maior_numero}")

senha_correta = "senha123"
senha_digitada = ""
while senha_digitada != senha_correta:
  senha_digitada = input("Digite a senha: ")
  if senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
print("Senha correta! Acesso concedido.")

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
vogais = "aeiou"
contador_vogais = 0
for letra in palavra:
  if letra in vogais:
    contador_vogais += 1
print(f"A palavra '{palavra}' possui {contador_vogais} vogais.")

numer1 = float(input('primeiro número: '))
numer2 = float(input('segundo número: '))
numer3 = float(input('terceiro número: '))
numer4 = float(input('quarto número: '))
numer5 = float(input('quinto número: '))
multiplicação = (numer1 * numer2 * numer3 * numer4 * numer5 )
print(f'A multiplicação dos números é: {multiplicação}')

for i in range(1, 21):
  quadrado = i * i
  print(f"O quadrado de {i} é {quadrado}")

numero = int(input("Digite um número inteiro não negativo: "))
if numero < 0:
  print("Fatorial não é definido para números negativos.")
elif numero == 0:
  print("O fatorial de 0 é 1.")
else:
  fatorial = 1
  for i in range(1, numero + 1):
    fatorial *= i
  print(f"O fatorial de {numero} é {fatorial}")

limite = int(input("Digite um número inteiro: "))
print(f"Números ímpares de 1 até {limite}:")
for i in range(1, limite + 1, 2):
  print(i)

print("Números entre 1 e 100 que são múltiplos de 3 e 5:")
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print(i)
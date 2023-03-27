a =2
b =1

equaçao = input("Digite a formula geral da equaçao çinear (a * x + b):")
print(f"\n A entrada do usuario {equaçao} e do tipo {type(equaçao)}")

for x in range(5):
    y = eval(equaçao)
    print(f'\n Resultado da equaçao para x = {x} é {y}')

def imprimir_mensagem(disciplina,curso):

    print(f"Minha primeira funçao m Pyrhon na disiplina : {disciplina}, no curso:{curso}")

imprimir_mensagem("Python", "ADS")

def calcular_desconto(valor, desconto=0):
    # o valor desconto possui 0 de valr default
    valor_com_desconto = valor - (valor* desconto)
    return valor_com_desconto
valor1 = calcular_desconto(100)# nenhum desconto
valor2 = calcular_desconto(100 ,0.25) #aplica 25% de desconto

print(f"\n Primeiro valor: {valor1}")
print(f"\n Segundo valor: {valor2}")


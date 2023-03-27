#ESTRUTURAS CONDICIONAIS
nome ="juan";
number1 = 2;
number2 = 4 

if (nome == 0 ):
    print('a variavel esa vazia');
elif ( number1 < number2 ):
    print(nome)
    print(f'numero1: {number1}, numero2: {number2}, o maior valor e {number2}')
else :
    print(nome)

#FOR IN
for i,c in enumerate(nome):
     print(f'posisao {i}, valor {c}')
for c in nome :
     print(c)
#WHILE
Number = 1;
while Number != 0 :
        Number = int(input("digite um numero: "));
        if Number % 2 == 0 :
             print("Numero par");
        elif Number % 2 == 1 :
             print("Numero impar");
        else : 
             print("clicou em 0");
# BREAK, CONTINUE 

disciplina ="linguagem de programação";
tsest = "programaçao";

for c in disciplina:
    if c =='a':
         break
    else:
         print(c)


for c in tsest :
     if c == 'm':
          continue 
     else :
          print(c)       
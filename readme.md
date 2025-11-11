# Atividade 1: Verificador de Maioridade

Esse projeto foi feito para praticar o uso do `input()`, do `int()` e da estrutura `if/else` em Python. O programa pede para o usuário digitar o nome e a idade. Depois ele verifica se a pessoa é maior ou menor de idade e mostra uma mensagem com o nome dela.

Quando o programa pede a idade, ele recebe o valor como texto. Por isso, é preciso converter esse texto para número usando a função `int()`. Assim o Python consegue comparar o valor da idade com o número 18. Se a idade for 18 ou mais, o programa mostra que a pessoa é maior de idade, se for menor que 18, mostra que é menor de idade.

## Exemplo de execução:
Por exemplo, se o usuário digitar o nome “Ana” e a idade “17”, o programa vai responder:  
`Olá, Ana, você é menor de idade.`  



# Atividade 2: A Tabuada

Esse projeto foi feito para treinar o uso do `input()`, do `int()` e do loop `for` com `range()` em Python. O programa pede que o usuário digite um número e mostra a tabuada completa desse número, indo de 1 até 10.

Depois que o usuário digita o número, o programa transforma o que foi digitado (que é texto) em um número inteiro usando o `int()`. Em seguida, ele usa um `for` para repetir as contas da tabuada. A cada repetição, o código multiplica o número digitado por um valor que vai de 1 a 10 e mostra o resultado na tela de forma organizada.

## Exemplo de execução:
Por exemplo, se o usuário digitar o número 7, o programa vai mostrar:  

7 x 1 = 7

7 x 2 = 14

7 x 3 = 21

7 x 4 = 28

7 x 5 = 35

7 x 6 = 42

7 x 7 = 49

7 x 8 = 56

7 x 9 = 63

7 x 10 = 70



# Atividade 3: Função Calculadora

Este projeto é uma atividade simples feita em Python para praticar o uso de funções. O objetivo foi criar um arquivo chamado funcao_calculadora.py que contém uma função chamada calculadora(). Essa função recebe três parâmetros: dois números e uma operação matemática (como soma, subtração, multiplicação ou divisão). O código lê os valores informados pelo usuário e retorna o resultado da operação escolhida. 

## Exemplo de execução: 
Ao digitar dois números e a operação desejada, como “+” ou “*”, o programa mostra o resultado final diretamente no terminal, permitindo que o usuário veja o cálculo feito pela função.


# Atividade 4: Orientação a Objetos com Herança

Esta atividade foi feita para praticar os conceitos básicos de programação orientada a objetos em Python, com foco em herança. O arquivo criado se chama heranca_veiculos.py e nele foram definidas duas classes: Veiculo e Carro. A classe Veiculo é a classe principal (ou “pai”), que contém atributos simples como marca e modelo. Já a classe Carro é uma classe “filha” que herda os atributos da classe Veiculo e ainda adiciona um novo atributo chamado numero_portas. O objetivo é entender como a herança permite reaproveitar código e evitar repetições. 

## Exemplo de execução:
Ao executar o código, é possível criar um objeto da classe Carro, informar a marca, o modelo e o número de portas, e depois exibir essas informações no terminal, mostrando como os atributos herdados e novos funcionam juntos.
